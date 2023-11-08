output "database_vars" {
  value       = aws_secretsmanager_secret.database_vars.id
  description = "database_vars_id"
}

output "rds_company" {
  value       = aws_security_group.rds_company.id
  description = "rds_company_id"
}
