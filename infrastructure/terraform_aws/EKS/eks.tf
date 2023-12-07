module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.20.0"

  cluster_name    = "my-eks"
  cluster_version = "1.24"

  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = true

  vpc_id     = [var.vpc_id]
  subnet_ids = [var.public_subnet_id_a,var.public_subnet_id_b, var.private_subnet_id_a,var.private_subnet_id_b]

  enable_irsa = true

  eks_managed_node_group_defaults = {
    disk_size = 50
  }


  node_security_group_additional_rules = {
    ingress_allow_access_from_control_panel = {
      type = "ingress"
      protocol = "tcp"
      from_port = 9443
      to_port = 9443
      souce_cluster_security_group = true
      description = "access aws load balancer"
    }
  }

  eks_managed_node_groups = {
    group1 = {
      desired_size = 1
      min_size     = 1
      max_size     = 3

      instance_types = ["t3.small"]
      capacity_type  = "ON_DEMAND"

      labels = {
        role = "group1"
      }
    }

  }

  fargate_profile = {
    fg-developers = {
        name = "fg-developers"
        selectors = [
            {
                namespace = "fg-developers"
            }
        ]
    }
  }

  tags = {
    Environment = "staging"
    Terraform = true
  }
}