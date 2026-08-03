---
title: "Worklog Week 7"
date: 2026-07-29
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:
* Write AWS Lambda CGV movie crawler and configure weekly automated trigger using Amazon EventBridge Scheduler.
* Integrate **Google Gemini 2.5 Flash** as a high-availability fallback Dual-AI Engine alongside Bedrock.
* Perform full security audit across AWS resources (AWS WAF, IAM Roles, S3 Bucket Policies, RDS Security Groups) and finalize system architecture diagrams.

### Tasks Completed This Week:
| Date | Task Description | Start Date | Completion Date | Reference / Source |
| --- | --- | --- | --- | --- |
| 27/07/2026 | - Authored AWS Lambda function (`cgv-movie-crawler`) on Node.js 20.x to scrape CGV movie schedules and update Amazon RDS MySQL directly.<br>- Created Amazon EventBridge Schedule (`cgv-weekly-crawler`) with `cron(0 17 ? * SUN *)` running every Monday at 00:00 AM ICT (UTC+7). | 27/07/2026 | 27/07/2026 | AWS Lambda & EventBridge Docs |
| 28/07/2026 | - Configured AWS Cloud9 & AWS CloudShell remote cloud IDE environment.<br>- Conducted security audit (AWS WAF Core Rules, S3 Presigned URL expiration, RDS Security Group isolation). | 28/07/2026 | 28/07/2026 | AWS Security Best Practices |
| 29/07/2026 | - ⚠️ **BEDROCK API INCIDENT & GEMINI FALLBACK**: Upgraded natural language parsing engine to **Dual-AI Engine**, integrating **Google Gemini 2.5 Flash** as a fallback AI engine with automatic failover.<br>- Finalized official AWS production architecture diagram. | 29/07/2026 | 29/07/2026 | Google Gemini API & Architecture Docs |

### Production System Architecture Diagram:

![AWS Cloud Architecture Diagram LifeSync AI Calendar](/images/architecture.png)

### Week 7 Results:
* Fully automated weekly CGV movie data ingestion pipeline.
* Successfully implemented multi-tier Dual-AI Engine architecture with automatic failover to Google Gemini 2.5 Flash.
* Standardized development environment and enforced strict cloud security compliance.
