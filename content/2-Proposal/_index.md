---
title: "Proposal"
date: 2026-07-31
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# LifeSync AI Calendar
## A Scientific AI-Powered Smart Scheduling System on AWS Cloud Infrastructure

---

### 1. Executive Summary

**LifeSync AI Calendar** is a full-stack intelligent scheduling application built with **Next.js 16** and deployed on **Amazon Web Services (AWS)**. The platform leverages **Google Gemini 2.5 Flash AI** for natural language scheduling intent parsing, a custom **Haversine Algorithm** for CGV cinema geolocation recommendations, and a **Scientific Scheduling Engine** based on Constraint Satisfaction Problem (CSP) solving with Bitmask optimization.

The system is deployed on a production-grade AWS infrastructure stack including Amazon EC2 (t2.micro Free Tier), Amazon RDS MySQL, Amazon S3, Amazon CloudFront CDN, AWS WAF, AWS Lambda, and Amazon EventBridge Scheduler — all accessible at the custom domain **[https://phuckhanh.id.vn](https://phuckhanh.id.vn)**.

<!-- System Demo Video Embed -->
<div align="center" style="margin: 25px 0;">
  <h4>📹 System Demo Video: LifeSync AI Calendar</h4>
  <iframe width="100%" height="450" style="max-width: 800px; border-radius: 8px; border: 1px solid #ddd;" src="YOUR_DEMO_VIDEO_EMBED_URL" frameborder="0" allowfullscreen></iframe>
  <p><i>(Paste your video embed link above)</i></p>
</div>

---

### 2. Problem Statement

#### What's the Problem?
Traditional calendar applications lack intelligent automation — users must manually create each event without receiving context-aware scheduling recommendations. There is no scientific approach to suggest optimal time slots based on a user's existing calendar, productivity science (Pomodoro, golden hours), or group location for outings.

#### The Solution
LifeSync AI Calendar solves this by:
- Parsing natural language requests via **Google Gemini AI** to extract scheduling intent (study, fitness, date, etc.)
- Applying a **Scientific Scheduling Engine** with 68 time slots (15-minute granularity) from 06:00–23:00 using CSP-based Bitmask solving
- Recommending the **Top 3 CGV Cinemas nearest to a group** using the Haversine geolocation formula with a special "**Nam rước Nữ**" weighting algorithm (80% Female, 20% Male proximity for couple dates)
- Automating event creation and calendar insertion with a single button click

---

### 3. AWS Cloud Architecture

#### System Infrastructure Architecture Diagram

![AWS Cloud Architecture Diagram LifeSync AI Calendar](/images/2-Proposal/architecture.png)
[Internet User]
      │
      ▼
[Custom Domain: phuckhanh.id.vn (Mắt Bão DNS)]
      │
      ▼ (Let's Encrypt SSL/TLS 1.3)
[Amazon CloudFront CDN] (Global Content Delivery Network)
      │
      ▼ (AWS WAF: LifeSync-WAF — Blocks SQLi, XSS, DDoS)
[Nginx Reverse Proxy: Port 80/443]
      │
      ▼ (Proxy Pass → http://localhost:3000)
[AWS EC2 t2.micro] (Ubuntu 24.04 LTS + PM2 + Next.js 16)
      │
      ├──► [Amazon RDS MySQL] (Relational Database — Users, Events, Chat)
      ├──► [AWS Lambda + EventBridge] (Weekly CGV Cinema Crawler Scheduler)
      ├──► [Google Gemini 2.5 Flash] (AI NLP Intent Parsing & Slot Filling)
      └──► [Amazon S3 Bucket] (User Avatar Storage via Presigned URL)
```

#### AWS Services Used

| Service | Role |
|---|---|
| **Amazon EC2 (t2.micro)** | Application server running Next.js 16 + PM2 + Nginx |
| **Amazon RDS MySQL** | Cloud relational database for users, events, and chat history |
| **Amazon S3** | Avatar file storage with Presigned URL upload mechanism |
| **Amazon CloudFront** | Global CDN for performance acceleration and IP masking |
| **AWS WAF** | Web Application Firewall (Core Rules + SQL Injection protection) |
| **AWS Lambda** | Serverless function for CGV cinema weekly crawler |
| **Amazon EventBridge** | Cron scheduler triggering Lambda at 00:00 every Monday |
| **GitHub Actions CI/CD** | Automated build & deploy pipeline on `git push origin main` |

---

### 4. Technical Implementation

#### AI Scheduling Engine Architecture
- **Strategy Pattern**: `StudyStrategy` (Pomodoro 50m/10m + Golden Hours 08:00–11:00), `FitnessStrategy` (30m recovery buffer post-workout), `DateStrategy` (30m travel buffer Hard Constraint)
- **CSP Bitmask Solver**: 68 slots × 15min from 06:00–23:00, running 100% native JavaScript
- **NLP Intent Parsing**: Google Gemini 2.5 Flash with Tool Calling format

#### Scientific CGV Cinema Recommendation Algorithm
- **Haversine Formula**: Calculates precise km distances between GPS coordinates
- **"Nam rước Nữ" Weighting**: For couple (1M+1F): `avgLat = female.lat × 0.8 + male.lat × 0.2` — prioritizes cinema location near the Female's home (80% weight)
- **Group Centroid**: For 3+ people or same-gender groups — standard weighted average

#### Key Features
- Zodiac-based avatar color system (12 signs × deterministic hash from User_ID)
- AI chat history auto-pruned after 3 days
- Real-time friend invitation & group scheduling with voting polls
- CGV cinema geolocation with Google Maps direct navigation links

---

### 5. Timeline & Milestones

| Phase | Period | Activity |
|---|---|---|
| **Phase 1** | Month 1 | Architecture design, AWS setup (EC2, RDS, S3), Next.js scaffolding |
| **Phase 2** | Month 2 | Core features (auth, calendar, scheduling engine), AI integration |
| **Phase 3** | Month 3 | CloudFront + WAF deployment, CGV geolocation, production hardening |
| **Post-launch** | Ongoing | CI/CD automation, monitoring, feature iterations |

---

### 6. Budget Estimation & Commercial Production Cost

#### Scenario 1: With AWS Credits & Free Tier (Actual Internship Period)
| AWS Service | Cost (Free Tier / Credits) |
|---|---|
| **Amazon EC2 t2.micro** (750h/mo Free Tier + 20GB EBS) | $0.00/month |
| **Amazon RDS db.t3.micro** (750h/mo Free Tier + 20GB SSD) | $0.00/month |
| **Amazon S3 Standard** (< 5GB Free Tier + Presigned URLs) | $0.00/month |
| **Amazon CloudFront** (1TB Free Tier Data Transfer) | ~$0.01/month |
| **AWS WAF** ($5 Web ACL + $2 Managed Rule Sets) | ~$7.00/month *(Covered by AWS Credits)* |
| **AWS Lambda & EventBridge** (< 1M requests Free Tier) | $0.00/month |
| **Actual Out-of-Pocket Expense**: | **$0.00 / month** |

#### Scenario 2: Commercial Production Cost (WITHOUT AWS Credits & WITHOUT Free Tier)
| AWS Service | On-Demand Configuration | Monthly Cost ($) | Monthly Cost (VND ~25k/$) |
|---|---|---|---|
| **Amazon EC2** | `t3.micro` (730 hrs) + 20GB EBS gp3 SSD | **$10.07** | ~251,750 VND |
| **Amazon RDS** | MySQL `db.t3.micro` Single-AZ + 20GB gp3 | **$14.71** | ~367,750 VND |
| **AWS WAF** | 1 Web ACL ($5) + 2 Rule Sets ($2) + Traffic | **$7.60** | ~190,000 VND |
| **Amazon CloudFront** | CDN Data Transfer Out (10GB) + HTTPS requests | **$0.95** | ~23,750 VND |
| **Amazon S3** | Standard Storage (5GB) + PUT/GET Presigned URLs | **$0.19** | ~4,750 VND |
| **AWS Lambda & EventBridge** | `cgv-movie-crawler` weekly cron job | **$0.20** | ~5,000 VND |
| **AI Engine API** | Google Gemini 2.5 Flash / Amazon Bedrock | **$1.00** | ~25,000 VND |
| **Domain & SSL** | Custom Domain `phuckhanh.id.vn` + Let's Encrypt SSL | **$0.40** | ~10,000 VND |
| **TOTAL ACTUAL MONTHLY COST** | **24/7 Production System Infrastructure** | **~$35.12 / month** | **~878,000 VND / month** |

---

### 7. Risk Assessment

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| EC2 instance downtime | High | Low | PM2 auto-restart + Elastic IP |
| AI API rate limit | Medium | Medium | AWS Bedrock Claude fallback |
| Database connection loss | High | Low | Connection pooling + retry logic |
| Cost overrun | Medium | Low | AWS Budget Alerts + Free Tier monitoring |

---

### 8. Expected Outcomes

#### Technical Achievements
- Production-grade AWS cloud infrastructure serving real user traffic 24/7
- Sub-second AI scheduling suggestions via Google Gemini 2.5 Flash
- Mathematical geolocation optimization for group cinema outings
- Enterprise-level security: SSL/TLS 1.3 + AWS WAF multi-layer protection

#### Long-term Value
- Reusable AWS architecture blueprint for future projects
- Demonstrated competency in full-stack deployment on AWS cloud
- Practical application of AI/NLP in real-world scheduling problems