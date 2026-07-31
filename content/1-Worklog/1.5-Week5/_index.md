---
title: "Week 5 Worklog"
date: 2026-07-19
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:
* Provision Amazon S3 bucket for storing user avatar images.
* Resolve major AWS primary account incident and complete infrastructure migration to backup AWS account.
* Implement direct browser-to-S3 avatar uploading using S3 Presigned URLs.

### Tasks carried out this week:
| Date | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 13/07/2026 | - Provisioned Amazon S3 bucket (`lifesync-avatar-bucket`) in `ap-southeast-2` region.<br>- Configured CORS policy allowing `PUT` and `GET` requests from domain `https://phuckhanh.id.vn`. | 13/07/2026 | 13/07/2026 | AWS S3 Developer Guide |
| 15/07/2026 | - ⚠️ **ACCOUNT INCIDENT & MIGRATION**: Primary AWS account encountered an organization lock issue.<br>- Provisioned a new secondary AWS account.<br>- Re-migrated RDS MySQL database schema, EC2 configuration, and S3 bucket to the new AWS account to maintain project continuity. | 15/07/2026 | 15/07/2026 | AWS Account & Migration Docs |
| 18/07/2026 | - Built Next.js API route `/api/upload/presign` to generate short-lived S3 Presigned URLs.<br>- Integrated frontend avatar upload component to upload images directly to S3 without server overhead. | 18/07/2026 | 18/07/2026 | AWS SDK v3 S3 Presigned URL Docs |

### Week 5 Achievements:
* Successfully handled the primary AWS account incident with zero data loss by executing quick cloud resource migration.
* Established secure S3 avatar storage infrastructure.
* Implemented zero-server-overhead avatar upload mechanism via Presigned URLs.
