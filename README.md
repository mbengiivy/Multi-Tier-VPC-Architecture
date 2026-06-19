
# Multi-Tier VPC Architecture | Week 1

A production-style, 3-tier AWS VPC architecture built with a Solutions Architect mindset. This project demonstrates end-to-end traffic flow from the public internet through web, application, and database tiers with full high availability and defense-in-depth security.

## Architecture Overview

![Multi-Tier VPC Architecture](/aws_multi_tier_vpc_architecture.png)

## Traffic Flow
Internet → Web ALB → Web Tier (Apache/PHP) → Internal ALB → App Tier (Flask) → Aurora MySQL


## Components

| Component | Configuration |
|-----------|--------------|
| VPC | [IP_ADDRESS] |
| Subnets | 6 (/24 each) — 3 tiers × 2 AZs |
| Web Tier | Public subnets, Apache + PHP, Auto Scaling Group |
| App Tier | Private subnets, Flask + Python, Auto Scaling Group |
| DB Tier | Private subnets, Aurora MySQL Multi-AZ |
| Load Balancers | External ALB (web), Internal ALB (app) |
| NAT Gateway | Public subnet (AZ-1), enables private outbound |
| Security | SG chaining by reference, defense in depth |

## Security Design

Each tier only accepts traffic from the tier directly before it:

Internet (0.0.0.0/0) → Web ALB SG (HTTP/HTTPS) → Web Instance SG (HTTP from Web ALB SG) → App ALB SG (HTTP from Web Instance SG) → App Instance SG (HTTP from App ALB SG) → DB SG (MySQL 3306 from App Instance SG)


## Lessons Learned

1. **Health Check Race Condition** — User Data scripts that install packages at boot can cause ALB health check failures. Solution: pre-baked AMIs.
2. **AMI Key Pair Baking** — The SSH key pair is embedded in the AMI's authorized_keys. Always document which key pair an AMI was built with.
3. **NAT Gateway Placement** — Must live in a public subnet with an Elastic IP. Without IGW access, the NAT Gateway can't forward traffic.
4. **Pre-baked AMIs** — Production pattern: install software in the AMI, use User Data only for lightweight configuration.

## Tech Stack

- AWS VPC, EC2, ALB, Auto Scaling, Aurora MySQL, NAT Gateway
- Python (Flask + PyMySQL)
- PHP (Apache proxy)
- Amazon Linux 2023

## Series

This is **Week 1** of *"Thinking Like a Solutions Architect: A 16-Week Cloud Engineering Journey"*

---

Built by Ivy | Cloud & DevOps 
