resource "aws_db_instance" "testterraformrds" {
  identifier             = "testrdsterraform"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "13.7"
  username               = "userpostgres"
  password               = "v181652981987"
# vpc_security_group_ids = [aws_vpc.test.default_security_group_id]
  publicly_accessible    = true
  skip_final_snapshot    = false
}

