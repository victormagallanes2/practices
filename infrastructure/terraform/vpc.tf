resource "aws_vpc" "terraform-vpc" {
  cidr_block       = "172.31.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "terraform-vpc"
  }
}

resource "aws_subnet" "my_subnet" {
  vpc_id            = aws_vpc.terraform-vpc.id
  cidr_block        = "172.31.0.0/16"

  tags = {
    Name = "tf-example"
  }
}

resource "aws_network_interface" "foo" {
  subnet_id   = aws_subnet.my_subnet.id
  private_ips = ["172.31.7.90"]

  tags = {
    Name = "primary_network_interface"
  }
}

