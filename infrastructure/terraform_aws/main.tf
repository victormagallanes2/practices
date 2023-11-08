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
    dynamodb_table = "terraform-locks"
    profile = "company"
  }
}

#Modules
module "VPC" {
  source = "./VPC"
}

module "SecurityGroup" {
  source = "./SecurityGroup"
  public_subnet_id_a = module.VPC.public-eu-west-1a-id
  public_subnet_id_b = module.VPC.public-eu-west-1b-id
  private_subnet_id_a = module.VPC.private-eu-west-1a-id
  private_subnet_id_b = module.VPC.private-eu-west-1b-id
  vpc_id = module.VPC.vpc_id
}

module "SecretManager" {
  source = "./SecretManager"
}


