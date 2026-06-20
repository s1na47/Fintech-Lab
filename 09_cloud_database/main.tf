provider "aws" {
  region = "eu-west-2" # London
}

# 1. The Firewall: Allow DBeaver to connect on Port 5432
resource "aws_security_group" "rds_sg" {
  name        = "fintech_db_firewall"
  description = "Allow PostgreSQL traffic from the internet"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Open to the world (For learning purposes only!)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 2. The Database: AWS Free Tier PostgreSQL
resource "aws_db_instance" "postgres_db" {
  identifier           = "fintech-production-db"
  allocated_storage    = 20               # 20 GB (Free Tier limit)
  engine               = "postgres"
  engine_version       = "15"           # Modern, stable version
  instance_class       = "db.t3.micro"    # AWS Free Tier Eligible
  
  # Database Credentials (What you will type into DBeaver)
  db_name              = "fintechdb"
  username             = "postgres"
  password             = "password123"    
  
  skip_final_snapshot  = true             # Allows us to destroy it instantly later
  publicly_accessible  = true             # CRITICAL: Lets your laptop connect to it
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "Fintech-Cloud-Database"
  }
}

# 3. Output the exact URL we need to connect DBeaver
output "db_endpoint" {
  value = aws_db_instance.postgres_db.endpoint
}