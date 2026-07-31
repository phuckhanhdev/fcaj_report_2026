---
title: "Week 4 Worklog"
date: 2026-07-12
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Week 4 Objectives:
* Implement Strategy Pattern for AI scheduling strategies (`StudyStrategy`, `FitnessStrategy`, `DateStrategy`).
* Provision Amazon EC2 production server, configure Elastic IP, 2GB Swap memory, Nginx reverse proxy, and PM2.
* Report mid-term progress on-site with mentors and configure Security Group access rules.

### Tasks carried out this week:
| Date | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 06/07/2026 | - Developed Strategy Pattern architecture for the scheduling engine:<br>&emsp; + `StudyStrategy`: Pomodoro 50m work / 10m break, target golden hours 08:00–11:00.<br>&emsp; + `FitnessStrategy`: 30m recovery buffer.<br>&emsp; + `DateStrategy`: Hard 30m travel buffer constraint. | 06/07/2026 | 06/07/2026 | Design Patterns Documentation |
| 08/07/2026 | - **On-site at AWS Office**: Launched EC2 Ubuntu 24.04 LTS `t2.micro` instance (`LifeSync-Server`).<br>- Allocated static Elastic IP `3.104.121.77`.<br>- Configured 2GB Swap memory.<br>- Configured Nginx reverse proxy routing port 80 to port 3000 and setup PM2 process manager. | 08/07/2026 | 08/07/2026 | AWS EC2 Documentation, Nginx Docs |
| 11/07/2026 | - **On-site at AWS Office**: Presented mid-term project demo to mentors.<br>- Configured EC2 & RDS Security Groups to restrict direct MySQL public access and only accept connections from the EC2 security group. | 11/07/2026 | 11/07/2026 | AWS Security Best Practices |

### Week 4 Achievements:
* Successfully built the Strategy Pattern scheduling engine.
* Provisioned and configured the live EC2 production server with Nginx and PM2.
* Secured database access using EC2-to-RDS Security Group rules and completed mid-term demo.
