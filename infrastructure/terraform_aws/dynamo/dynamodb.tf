resource "aws_dynamodb_table" "lock" {
  name = "terraform-lock"
  hash_key = "lock_id"
  range_key = "lock_version"
  read_capacity = 1
  write_capacity = 1

  # Set the TTL for the lock
  time_to_live = 300
}