
# Troubleshooting Guide

## 1. ALB Health Checks Failing (502 Gateway Error)

**Symptoms:**
- Target group shows instances as "unhealthy"
- ASG keeps terminating and relaunching instances
- Browser shows 502 Bad Gateway

**Root Cause:** User Data script takes too long. ALB health check times out before web server starts.

**Solution:**
- Pre-bake AMI with all packages installed
- OR increase ASG health check grace period to 300+ seconds

---

## 2. Cannot SSH Into Instances (Permission Denied)

**Symptoms:**
- `Permission denied (publickey,gssapi-keyex,gssapi-with-mic)`

**Checks:**
1. Correct key file? (`chmod 400 <keyfile>.pem`)
2. Key pair matches what instance was launched with?
3. If using pre-baked AMI — the AMI carries the key pair from the ORIGINAL instance

**Solution:**
- Rebuild AMI from instance launched with correct key pair
- Use SSH agent forwarding (`ssh -A`) for bastion hops

---

## 3. NAT Gateway Not Working

**Symptoms:**
- Private instances can't reach internet
- `dnf install` or `wget` hangs/times out

**Checks:**
1. Is NAT Gateway in a PUBLIC subnet?
2. Does NAT Gateway have an Elastic IP?
3. Does private subnet route table have `0.0.0.0/0 → NAT Gateway`?

**Solution:**
- Recreate NAT Gateway in correct public subnet (use "Zonal" mode to select subnet)

---

## 4. Target Group Shows "Request Timed Out"

**Symptoms:**
- Health check status: "unhealthy"
- Reason: "Request timed out"

**Checks:**
1. Is the application running? (`curl http://localhost/health`)
2. Security group allows inbound from ALB SG on correct port?
3. ALB deployed in same AZ as instances?

**Solution:**
- Verify ALB subnet mapping matches instance AZs
- Check SG inbound rules allow traffic from ALB SG

---

## Useful Diagnostic Commands

```bash
# Check if web server is running
sudo systemctl status httpd

# Check if Flask is running
ps aux | grep python

# Test local connectivity
curl http://localhost
curl http://localhost/health

# Check User Data script output
cat /var/log/cloud-init-output.log | tail -50

# Check OS version
cat /etc/os-release

# Test database connectivity
mysql -h <rds-endpoint> -u <username> -p

# DNS resolution test
nslookup <alb-dns-name>
