---
title: "Clean up Resources"
date: 2026-07-31
weight: 9
chapter: false
pre: " <b> 5.9. </b> "
---

## Clean up AWS Resources

After completing the workshop, you may want to clean up resources to avoid unexpected charges. Follow this guide to safely remove all AWS resources created during this workshop.

> **⚠️ Warning**: Deleting these resources is **permanent and irreversible**. Only proceed if you have finished using the LifeSync AI Calendar system and no longer need the data.

---

## Cleanup Order

**Important**: Delete resources in this specific order to avoid dependency errors.

### 1. Amazon EventBridge Scheduler

1. Go to **EventBridge** → **Scheduler** → **Schedules**
2. Select `cgv-weekly-crawler` → Click **Delete** → Confirm

### 2. AWS Lambda Function

1. Go to **Lambda** → **Functions**
2. Select `cgv-movie-crawler` → Click **Actions** → **Delete** → Confirm

### 3. AWS WAF — Web ACL

1. Go to **WAF & Shield** → **Protection packs (web ACLs)**
2. Change region to **Global (CloudFront)**
3. Select `LifeSync-WAF` → Click **Delete** → Confirm

### 4. Amazon CloudFront Distribution

1. Go to **CloudFront** → **Distributions**
2. Select your distribution → Click **Disable** first → Wait for status to change
3. After disabled, select again → Click **Delete** → Confirm

### 5. Amazon S3 Bucket

1. Go to **S3** → Click on `lifesync-avatar-bucket`
2. Select all objects → **Delete** (empty the bucket first)
3. Go back → Select the bucket → Click **Delete** → Type bucket name → Confirm

### 6. Amazon RDS Instance

1. Go to **RDS** → **Databases**
2. Select `lifesync-calendar` → Click **Actions** → **Delete**
3. Uncheck **Create final snapshot** (if you don't need a backup)
4. Type `delete me` → Click **Delete**

### 7. Amazon EC2 Instance & Elastic IP

1. **Elastic IP first**: Go to **EC2** → **Elastic IPs**
   - Select your Elastic IP → Click **Actions** → **Disassociate** → then **Release**
   
   > Elastic IPs cost $0.005/hour if allocated but NOT attached to a running instance. Release it immediately.

2. **Terminate EC2**: Go to **EC2** → **Instances**
   - Select `LifeSync-Server` → Click **Instance state** → **Terminate instance** → Confirm

### 8. Security Groups

1. Go to **EC2** → **Security Groups**
2. Delete `lifesync-rds-sg` and any workshop-specific security groups
   - Note: Cannot delete if still in use by other resources

### 9. IAM User (Optional)

1. Go to **IAM** → **Users**
2. Select the IAM user created for S3 Presigned URL access
3. Click **Delete** → Confirm

---

## Cost After Cleanup

After completing cleanup, your monthly AWS bill should return to **$0.00** (assuming no other AWS resources are running in your account under Free Tier limits).

| Service | Monthly Cost After Cleanup |
|---|---|
| EC2 | $0.00 (terminated) |
| RDS | $0.00 (deleted) |
| S3 | $0.00 (deleted) |
| CloudFront | $0.00 (deleted) |
| WAF | $0.00 (deleted) |
| Lambda | $0.00 (deleted) |
| EventBridge | $0.00 (deleted) |

---

## Keep for Reference

Before deleting, consider saving:
- The `.env.local` file with all configuration values
- Database backup: `mysqldump -h <RDS_HOST> -u admin -p lifesync_db > backup.sql`
- The GitHub repository (code is preserved regardless of AWS cleanup)

---

### ✅ Workshop Complete

Congratulations! You have successfully:
1. ✅ Set up a production **Amazon EC2** server with Next.js 16, Nginx, and PM2
2. ✅ Configured **Amazon RDS MySQL** with proper security groups and schema
3. ✅ Created an **Amazon S3** bucket with CORS and Presigned URL for avatar upload
4. ✅ Deployed **Amazon CloudFront** CDN for global performance and IP masking
5. ✅ Secured the application with **AWS WAF** (Core Rules + SQL Injection protection)
6. ✅ Automated weekly CGV cinema crawling with **AWS Lambda + EventBridge**
7. ✅ Integrated non-AWS services: custom domain, SSL, Google Gemini AI, and NextAuth

**This is a complete, production-grade AWS architecture for a full-stack AI web application!**
