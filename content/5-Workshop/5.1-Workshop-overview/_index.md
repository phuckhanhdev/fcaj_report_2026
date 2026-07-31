---
title: "Workshop Overview"
date: 2026-07-31
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

## LifeSync AI Calendar — Workshop Overview

### What You Will Build

By the end of this workshop, you will have a **fully deployed production system** on AWS cloud that mirrors the architecture used at [https://phuckhanh.id.vn](https://phuckhanh.id.vn), including:

- An **Amazon EC2** instance running Next.js 16 with Nginx reverse proxy and PM2 process manager
- An **Amazon RDS MySQL** database storing user accounts, calendar events, and AI chat history
- An **Amazon S3** bucket for storing user avatar images via Presigned URL
- An **Amazon CloudFront** CDN distribution accelerating global delivery with IP masking
- An **AWS WAF** Web Application Firewall with Core Rules and SQL Injection protection
- An **AWS Lambda** function + **Amazon EventBridge** Scheduler for weekly CGV cinema data crawling

---

### AWS Cloud Architecture Overview

![AWS Cloud Architecture Diagram LifeSync AI Calendar Workshop](/images/architecture.png)

<!-- System Demo Video Embed -->
<div align="center" style="margin: 25px 0;">
  <h4>📹 System Demo Video: LifeSync AI Calendar</h4>
  <iframe width="100%" height="450" style="max-width: 800px; border-radius: 8px; border: 1px solid #ddd;" src="YOUR_DEMO_VIDEO_EMBED_URL" frameborder="0" allowfullscreen></iframe>
  <p><i>(Paste your video embed link above)</i></p>
</div>

### Key Technologies

| Technology | Purpose |
|---|---|
| **Next.js 16** | Full-stack React framework (App Router + Server Actions) |
| **PM2** | Node.js production process manager (auto-restart, logs) |
| **Nginx** | High-performance reverse proxy routing port 80/443 → 3000 |
| **Ubuntu 24.04 LTS** | Stable Linux OS for EC2 instance |
| **MySQL 8.0** | Production relational database on Amazon RDS |
| **Google Gemini 2.5 Flash** | AI model for natural language scheduling intent parsing |
| **GitHub Actions** | CI/CD pipeline for automated deployment on every `git push` |

### Workshop Scope

This workshop is divided into **AWS Services** (Sections 3–7) and **Other Services** (Section 8):

**AWS Services covered in detail:**
- Amazon EC2 — Server provisioning, security groups, Elastic IP, swap memory
- Amazon RDS — MySQL database setup, security group, schema migration
- Amazon S3 — Bucket creation, CORS policy, Presigned URL mechanism
- Amazon CloudFront — Distribution creation, origin settings, cache behavior
- AWS WAF — Web ACL creation, managed rules selection, CloudFront attachment
- AWS Lambda — Function creation, environment variables, deployment package
- Amazon EventBridge — Cron scheduler targeting Lambda

**Other services (Section 8 — brief setup notes only):**
- Mắt Bão domain & DNS A Records configuration
- Let's Encrypt SSL/TLS with Certbot
- Google Gemini API key management

### Estimated Time

| Section | Estimated Time |
|---|---|
| Prerequisites | 15 minutes |
| EC2 Setup | 20 minutes |
| RDS & S3 Setup | 20 minutes |
| CloudFront Setup | 15 minutes |
| WAF Setup | 10 minutes |
| Lambda + EventBridge | 20 minutes |
| Other Services | 15 minutes |
| **Total** | **~2 hours** |