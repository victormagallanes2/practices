resource "aws_s3_bucket" "state" {
  bucket = "company"
  acl = "private"
  force_destroy = true

  # Enable versioning for the bucket
  versioning {
    enabled = true
  }
}