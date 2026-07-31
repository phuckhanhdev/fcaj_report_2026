---
title: "Week 7 Worklog"
date: 2026-08-02
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:
* Build AWS Lambda CGV crawler function and configure Amazon EventBridge weekly cron schedule.
* Handle AWS Bedrock API quota incident and integrate **Google Gemini 2.5 Flash** as a high-availability fallback engine.
* Complete the full 9-step AWS Production Deployment Workshop report by July 31, 2026.

### Tasks carried out this week:
| Date | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 27/07/2026 | - Developed AWS Lambda function (`cgv-movie-crawler`) running Node.js 20.x to scrape CGV movie and showtime data into Amazon RDS MySQL.<br>- Created Amazon EventBridge Schedule (`cgv-weekly-crawler`) with cron expression `cron(0 17 ? * SUN *)` running every Monday at 00:00 AM Vietnam time (UTC+7). | 27/07/2026 | 27/07/2026 | AWS Lambda & EventBridge Docs |
| 29/07/2026 | - ⚠️ **BEDROCK API INCIDENT & GEMINI FALLBACK**: AWS Bedrock API experienced quota limits / connection errors.<br>- Upgraded the AI Intent Parsing service to a **Dual-AI Engine architecture**, integrating **Google Gemini 2.5 Flash** as an instant fallback engine to ensure 99.9% uptime. | 29/07/2026 | 29/07/2026 | Google Gemini API Docs |
| 31/07/2026 | - 🎉 **COMPLETED AWS WORKSHOP**: Finalized the comprehensive 9-step AWS Production Deployment Workshop document (`docs/aws_full_production_deployment_report.md`) covering EC2, RDS, S3, CloudFront, WAF, Lambda, and EventBridge. | 31/07/2026 | 31/07/2026 | Project Workshop Documentation |

### Week 7 Achievements:
* Fully automated weekly CGV cinema data collection pipeline.
* Built resilient Dual-AI Engine architecture with automatic fallback to Google Gemini 2.5 Flash.
* Officially completed the comprehensive 9-step AWS deployment workshop documentation on July 31, 2026.
