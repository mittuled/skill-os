resource "aws_organizations_organization" "org" {
  aws_service_access_principals = [
    "cloudtrail.amazonaws.com",
    "sso.amazonaws.com",
  ]
  feature_set = "ALL"
}

resource "aws_organizations_account" "dev" {
  name      = "dev"
  email     = "aws-dev@company.com"
  parent_id = aws_organizations_organization.org.roots[0].id
  tags      = { Environment = "dev" }
}

resource "aws_organizations_account" "staging" {
  name      = "staging"
  email     = "aws-staging@company.com"
  parent_id = aws_organizations_organization.org.roots[0].id
  tags      = { Environment = "staging" }
}

resource "aws_organizations_account" "production" {
  name      = "production"
  email     = "aws-production@company.com"
  parent_id = aws_organizations_organization.org.roots[0].id
  tags      = { Environment = "production" }
}

resource "aws_cloudtrail" "org_trail" {
  name                       = "org-trail"
  s3_bucket_name             = aws_s3_bucket.trail_logs.id
  is_organization_trail      = true
  is_multi_region_trail      = true
  enable_log_file_validation = true
}

resource "aws_s3_bucket" "trail_logs" {
  bucket        = "company-org-cloudtrail-logs"
  force_destroy = false
}

resource "aws_organizations_policy" "deny_root" {
  name    = "deny-root-actions"
  type    = "SERVICE_CONTROL_POLICY"
  content = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "DenyRootActions"
      Effect    = "Deny"
      Action    = "*"
      Resource  = "*"
      Condition = {
        StringLike = { "aws:PrincipalArn" = "arn:aws:iam::*:root" }
      }
    }]
  })
}

resource "aws_organizations_policy" "restrict_regions" {
  name    = "restrict-regions"
  type    = "SERVICE_CONTROL_POLICY"
  content = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "DenyOutsideAllowedRegions"
      Effect    = "Deny"
      Action    = "*"
      Resource  = "*"
      Condition = {
        StringNotEquals = {
          "aws:RequestedRegion" = ["us-east-1", "us-west-2", "eu-west-1"]
        }
      }
    }]
  })
}
