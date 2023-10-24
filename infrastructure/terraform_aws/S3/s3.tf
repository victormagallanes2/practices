resource "aws_s3_bucket" "state" {
  bucket = "company"
  block_public_access = true

  versioning {
    enabled = true
  }
}