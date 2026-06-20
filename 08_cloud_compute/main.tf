provider "aws" {
  region = "eu-west-2"
}

# 1. Get the latest Ubuntu image
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# 2. Upload your Laptop's Public Key to AWS
resource "aws_key_pair" "anis_key" {
  key_name   = "anis-xps-key"
  public_key = file("~/.ssh/aws_key.pub") # Pulls your local key automatically!
}

# 3. Create the Firewall
resource "aws_security_group" "bot_sg" {
  name        = "trading_bot_firewall_v2"
  description = "Allow SSH from the world"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 4. Launch the Server and Install Docker automatically (Bootstrap)
resource "aws_instance" "fintech_bot_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  key_name      = aws_key_pair.anis_key.key_name # Attaches your key!
  
  vpc_security_group_ids = [aws_security_group.bot_sg.id]

  # USER DATA: This script runs automatically on boot to install Docker!
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo usermod -aG docker ubuntu
              EOF

  tags = {
    Name = "Fintech-Production-Server"
  }
}

output "server_public_ip" {
  value = aws_instance.fintech_bot_server.public_ip
}