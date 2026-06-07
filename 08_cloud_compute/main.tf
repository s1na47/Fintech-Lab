# 1. Connect to AWS London
provider "aws" {
  region = "eu-west-2"
}

# 2. Automatically grab the latest Ubuntu 22.04 image
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] 

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# 3. The Firewall: Allow SSH access
resource "aws_security_group" "bot_sg" {
  name        = "trading_bot_firewall_anis"
  description = "Allow SSH to control the server"

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

# 4. Launch the actual EC2 Server
resource "aws_instance" "fintech_bot_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro" 
  
  vpc_security_group_ids = [aws_security_group.bot_sg.id]

  tags = {
    Name = "Fintech-Production-Server"
  }
}

# 5. Print the IP address to the terminal when finished
output "server_public_ip" {
  value = aws_instance.fintech_bot_server.public_ip
}