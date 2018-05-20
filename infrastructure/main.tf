provider "aws" {}

terraform {
  backend "s3" {
    bucket = "practices-of-serverless"
    key    = "terraform/terraform.tfstate"
    region = "ap-northeast-1"
  }
}

resource "aws_dynamodb_table" "hello" {
  name           = "practices-of-serverless-hello"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "foo"

  attribute {
    name = "foo"
    type = "S"
  }
}
