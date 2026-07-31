---
title: "Week 6 Worklog"
date: 2026-07-26
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:
* Deploy Amazon CloudFront CDN distribution for global performance acceleration and IP masking.
* Configure AWS WAF (Web Application Firewall) to protect the application against OWASP Top 10 and SQL Injection.
* Attend the "FCAJ: Agentic AI Build Week" event on-site at the AWS office and present the project.

### Tasks carried out this week:
| Date | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 21/07/2026 | - Created Amazon CloudFront CDN distribution (`dbpvljmyvgnai.cloudfront.net`) pointing to custom domain `phuckhanh.id.vn`.<br>- Configured viewer protocol policy to redirect HTTP to HTTPS.<br>- Enabled HTTP methods `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`. | 21/07/2026 | 21/07/2026 | AWS CloudFront Developer Guide |
| 23/07/2026 | - Created AWS WAF Web ACL (`LifeSync-WAF`) attached directly to CloudFront.<br>- Enabled AWS Managed Rules: `AWSManagedRulesCommonRuleSet` (Core OWASP) and `AWSManagedRulesSQLiRuleSet` (SQL Injection protection for RDS). | 23/07/2026 | 23/07/2026 | AWS WAF Developer Guide |
| 25/07/2026 | - **On-site at AWS Office**: Attended the "FCAJ: Agentic AI Build Week" event.<br>- Presented the LifeSync AI Calendar architecture demo, receiving feedback from AWS Solution Architects and hackathon teams. | 25/07/2026 | 25/07/2026 | FCAJ Event Resources |

### Week 6 Achievements:
* Successfully deployed global CloudFront CDN for low-latency delivery and EC2 Elastic IP masking.
* Established multi-layer WAF security protection.
* Successfully presented the project at the FCAJ Agentic AI Build Week on-site event.
