module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.20.0"

  cluster_name    = "my-eks"
  cluster_version = "1.24"

  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  enable_irsa = true

  eks_managed_node_group_defaults = {
    disk_size = 50
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
  }
}