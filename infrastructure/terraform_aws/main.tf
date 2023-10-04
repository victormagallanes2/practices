terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
  profile = "company"
}

terraform {
  backend "s3" {
    bucket = "company"
    key = "company/terraform.tfstate"
    region = "eu-west-1"
    encrypt = true
    dynamodb_table = "lock"
    profile = "company"
  }
}

#Modules
module "s3" {
    source = "./s3"
    cluster_version = var.cluster_version
    cluster_name = var.cluster_name
}

# module "dynamo" {
#     source = "./dynamo"
#     cluster_version = var.cluster_version
#     cluster_name = var.cluster_name
# }



