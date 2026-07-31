---
title: "Worklog"
date: 2026-07-31
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

# Internship Worklog (12-Week Journal)

Throughout the **12-week internship** under the **First Cloud AI Journey (FCAJ 2026)** program at **AWS Vietnam** (from **June 15, 2026** to **August 15, 2026**), I conducted research, cloud architecture design, and production deployment of **LifeSync AI Calendar** — a scientific AI-powered smart scheduling web platform.

Below is the weekly summary of tasks and milestones:

---

### 📅 12-Week Internship Outline:

- **[Week 1 (June 15 – June 21): On-boarding & AWS Service Fundamentals](1.1-Week1/)**  
  *On-site at AWS Office (June 15)*. Received AWS Credits, configured development environment, and studied core cloud services (IAM, EC2, S3, VPC).

- **[Week 2 (June 22 – June 28): Architecture Review & MySQL Database Schema Design](1.2-Week2/)**  
  *On-site at AWS Office (June 24)*. Architecture discussion with Mentor Tien Kha, tested LocalStack, and designed relational database schemas on MySQL.

- **[Week 3 (June 29 – July 05): Swinburne Cloud Mastery Seminar & Next.js 16 Bootstrap](1.3-Week3/)**  
  *On-site at AWS Office (July 04)*. Attended Swinburne Cloud Mastery seminar, bootstrapped LifeSync AI Calendar application with Next.js 16 and TailwindCSS.

- **[Week 4 (July 06 – July 12): Provisioning EC2, Elastic IP, Nginx & PM2](1.4-Week4/)**  
  *On-site at AWS Office (July 08 & July 11)*. Launched Ubuntu EC2 instance, attached Elastic IP `3.104.121.77`, configured Nginx Reverse Proxy, PM2 process manager, and presented Mid-term report.

- **[Week 5 (July 13 – July 19): AWS Account Incident & Deploying RDS MySQL + S3 Presigned URLs](1.5-Week5/)**  
  *Incident on July 15*: Resolved primary AWS account organization lock ➔ Migrated database & codebase to secondary AWS account. Configured RDS MySQL and S3 avatar upload via Presigned URLs.

- **[Week 6 (July 20 – July 26): AABW Hackathon Workshop & Deploying AWS WAF + CloudFront](1.6-Week6/)**  
  *On-site at AWS Office (July 25)*. Attended AABW AWS AI Build Week workshop, deployed CloudFront CDN, and configured AWS WAF (Core Rules + SQL Injection protection).

- **[Week 7 (July 27 – Aug 02): Bedrock Quota Incident & Dual-AI Engine + Lambda CGV Crawler](1.7-Week7/)**  
  *Incident on July 29*: Handled Bedrock quota error by integrating **Google Gemini 2.5 Flash** as a high-availability fallback AI engine. Deployed AWS Lambda + EventBridge for weekly CGV cinema scraping and **completed Workshop (July 31)**.

- **[Week 8 (Aug 03 – Aug 09): Haversine Geolocation Optimization & Bitmask Scientific Scheduler](1.8-Week8/)**  
  Programmed Haversine proximity algorithm with "Nam rước Nữ" weighting (80% Female / 20% Male) and Constraint Satisfaction Problem (CSP) solver with 68 time slots (15-min granularity).

- **[Week 9 (Aug 10 – Aug 16): Automated CI/CD Pipelines via GitHub Actions & Internship Completion](1.9-Week9/)**  
  Configured GitHub Actions CI/CD pipeline (`deploy.yml`) for automated build/deploy to EC2 upon code push. Official internship completion on August 15, 2026.

- **[Week 10 (Aug 17 – Aug 23): CloudWatch Alarms Optimization & Log Data Protection](1.10-Week10/)**  
  Configured CloudWatch Alarms using the "3-Right" model and set up CloudWatch Logs Data Protection rules to mask sensitive user data.

- **[Week 11 (Aug 24 – Aug 30): Workshop Documentation & Technical Blog Roundup](1.11-Week11/)**  
  Authored 9-step AWS production deployment workshop guide and finalized 4 technical blog posts.

- **[Week 12 (Aug 31 – Sep 06): Final Assessment, Feedback & Hugo Portfolio Publication](1.12-Week12/)**  
  Completed self-evaluation matrix, submitted program feedback, and published the FCAJ 2026 Internship Portfolio website on Hugo.
