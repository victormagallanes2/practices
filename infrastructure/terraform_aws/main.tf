terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.19.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
  profile = "company"
}



terraform {
  backend "s3" {
    bucket = "company-s3"
    key = "company/terraform.tfstate"
    region = "eu-west-1"
    encrypt = true
    dynamodb_table = "lock"
    profile = "company"
  }
}

Modules
module "VPC" {
    source = "./VPC"
}




