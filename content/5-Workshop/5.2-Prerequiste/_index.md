---
title: "Prerequisites"
date: 2026-07-31
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

## Prerequisites

Before starting the workshop, ensure you have the following ready:

### 1. AWS Account

- An active **AWS Account** with sufficient permissions (AdministratorAccess or at minimum: EC2, RDS, S3, CloudFront, WAF, Lambda, EventBridge, IAM full access)
- **AWS Credits** recommended — this workshop uses services that may exceed Free Tier limits (e.g., AWS WAF ~$7/month)
- Recommended region: **ap-southeast-2 (Sydney)** — closest to Vietnam for low latency

### 2. Source Code

- Fork or clone the LifeSync AI Calendar repository:
  ```bash
  git clone https://github.com/<your-username>/ai_calendar_fcaj.git
  ```
- You will need a **GitHub account** and a **GitHub repository** to configure GitHub Actions CI/CD

### 3. Local Tools Required

| Tool | Version | Purpose |
|---|---|---|
| **Node.js** | 20.x LTS | Runtime for Next.js |
| **npm** | 10.x | Package manager |
| **Git** | Latest | Source code versioning |
| **SSH client** | Built-in (Mac/Linux) or PuTTY (Windows) | Connect to EC2 |
| **AWS CLI** | v2 (optional) | Command-line AWS management |

### 4. Environment Variables

Prepare the following environment variables to configure in your `.env.local` and as GitHub Secrets:

| Variable | Description |
|---|---|
| `DATABASE_URL` | MySQL connection string from RDS endpoint |
| `NEXTAUTH_SECRET` | Random string for NextAuth session encryption |
| `NEXTAUTH_URL` | Your production URL (e.g., `https://phuckhanh.id.vn`) |
| `GOOGLE_AI_API_KEY` | Google Gemini API key from Google AI Studio |
| `AWS_ACCESS_KEY_ID` | IAM user access key for S3 Presigned URL |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key for S3 Presigned URL |
| `AWS_REGION` | AWS region (e.g., `ap-southeast-2`) |
| `S3_BUCKET_NAME` | S3 bucket name for avatar storage |
| `RDS_HOST` | RDS MySQL endpoint hostname |
| `RDS_USER` | RDS database username |
| `RDS_PASSWORD` | RDS database password |
| `RDS_DATABASE` | RDS database name |

### 5. IAM User for Application

Create an IAM user with **Programmatic Access** and attach the following inline policy for S3 Presigned URL:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::lifesync-avatar-bucket/*"
    }
  ]
}
```

### 6. Key Pair for EC2

1. Go to **EC2 Console** → **Key Pairs** → **Create key pair**
2. Name: `lifesync-key`
3. Format: `.pem` (for Mac/Linux) or `.ppk` (for Windows PuTTY)
4. Download and store securely — **you cannot download it again**
5. Set correct permissions: `chmod 400 lifesync-key.pem`