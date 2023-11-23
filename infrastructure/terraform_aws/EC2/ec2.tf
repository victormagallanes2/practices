resource "aws_instance" "terraform-ec2" {
  ami           = "ami-0097e4945b2d15c30"
  instance_type = "t2.micro"
  key_name = "my-key-terraform-ec2"
  vpc_security_group_ids  = [var.ssh-access]
  subnet_id = [var.public_subnet_id_a,var.public_subnet_id_b]


  tags = {
    Name = "ubuntu20.04"
  }
}


