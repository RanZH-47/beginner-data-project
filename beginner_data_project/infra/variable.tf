variable "bucket_prefix" {
  description = "Bucket prefix for data lake"
  type        = string
  default     = "sde-data-lake-"
}

variable "redshift_node_type" {
  description = "Node type for Redshift cluster"
  type        = string
  default     = "dc2.large"
}

variable "redshift_user" {
  description = "Username for Redshift cluster"
  type        = string
  default     = "sde-redshift"
}

variable "redshift_password" {
  description = "Password for Redshift cluster"
  type        = string
  default     = "sdePwd112233@"
}

## Key to allow connection to our EC2 instance
variable "key_name" {
  description = "EC2 key name"
  type        = string
  default     = "sde-key"
}

## AWS EMR node type and auto termination time (EMR is expensive!)
variable "instance_type" {
  description = "Instance type for EMR and EC2"
  type        = string
  default     = "m4.xlarge"
}

variable "auto_termination_timeoff" {
  description = "Auto EMR termination time(in idle seconds)"
  type        = number
  default     = 14400 # 4 hours
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-southeast-1"
}
