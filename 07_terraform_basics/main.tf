# 1. Tell Terraform we want to use AWS in London
provider "aws" {
  region = "eu-west-2"
}

# 2. Tell Terraform to build an S3 Bucket (A Data Lake for our Crypto prices)
resource "aws_s3_bucket" "fintech_data_bucket" {
  
  # CRITICAL: This name MUST be globally unique across all of Amazon.
  # Change the numbers at the end to something random like your birthdate or phone digits!
  bucket = "anis-fintech-data-lake-230204" 
}