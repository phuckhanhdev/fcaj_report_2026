---
title: "Workshop"
date: 2026-07-31
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Deploy LifeSync AI Calendar on AWS

#### Overview

**LifeSync AI Calendar** is a production-grade AI-powered scheduling application built with Next.js 16, deployed on a complete AWS infrastructure stack. In this workshop, you will learn to set up each AWS service from scratch following the same steps used to build the real production system at [https://phuckhanh.id.vn](https://phuckhanh.id.vn).

This workshop focuses on setting up **AWS services only**. For other services (Google Gemini AI, Mắt Bão domain, Certbot SSL), refer to the dedicated section at the end of the workshop.

#### Architecture

```
[Internet User]
      │
      ▼
[Amazon CloudFront CDN] ← [AWS WAF Protection]
      │
      ▼
[AWS EC2 t2.micro — Next.js 16 + Nginx + PM2]
      │
      ├──► [Amazon RDS MySQL]
      ├──► [Amazon S3 — Avatar Storage]
      └──► [AWS Lambda + EventBridge — CGV Crawler]
```

#### Content

1. [Workshop Overview](5.1-Workshop-overview)
2. [Prerequisites](5.2-Prerequiste/)
3. [Setup Amazon EC2](5.3-EC2/)
4. [Setup Amazon RDS & S3](5.4-RDS-S3/)
5. [Setup Amazon CloudFront](5.5-CloudFront/)
6. [Setup AWS WAF](5.6-WAF/)
7. [Setup AWS Lambda & EventBridge](5.7-Lambda-EventBridge/)
8. [Other Services Setup](5.8-OtherServices/)
9. [Clean up Resources](5.9-Cleanup/)