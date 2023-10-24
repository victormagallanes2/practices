resource "aws_instance" "terraform-ec2" {
  ami           = "ami-0097e4945b2d15c30"
  instance_type = "t3.micro"

  network_interface {
    network_interface_id = aws_network_interface.foo.id
    device_index         = 0
  }


  tags = {
    Name = "ubuntu20.04"
  }
}


