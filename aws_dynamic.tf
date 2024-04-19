data "aws_iam_policy_document" "example" {

  statement {
    actions = [
      "s3:ListBucket",
    ]

    resources = [
      "arn:aws:s3:::prod-*",
    ]
  }

  dynamic "statement" {
    for_each = var.is_prod ? [1] : [] 
    content {
      actions = [
      "s3:*",
    ]

    resources = [
      "arn:aws:s3:::dev-*",
    ]
    }
  }
}

resource "aws_iam_policy" "example" {
  name   = "example_policy"
  path   = "/"
  policy = data.aws_iam_policy_document.example.json
}


variable "is_prod" {
  type = bool
  default = true
}
