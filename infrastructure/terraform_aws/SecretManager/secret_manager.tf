data "aws_secretsmanager_secret" "database_vars" {
  name = "db_vars"
}

data "aws_secretsmanager_secret_version" "current" {
  secret_id = data.aws_secretsmanager_secret.database_vars.id
}
