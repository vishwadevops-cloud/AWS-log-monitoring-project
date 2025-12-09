# AWS-log-monitoring-project
Automated Log Monitoring &amp; Alerting System using AWS CloudWatch, SNS, and EC2
# 🚀 Event-Driven Log Monitoring & Alerting System (AWS)

## 🎯 Project Goal

Build a real-time **event-driven log monitoring** system on AWS that:

- Collects application logs from EC2
- Sends alerts when error patterns appear
- Processes logs asynchronously
- Archives old logs cost-effectively (S3 → Glacier)
- Scales automatically when load increases

---

## 🏗 Architecture Overview

**Flow:**

1. Application running on **EC2 instances** generates log files.
2. **CloudWatch Agent** on EC2 streams log file `/var/log/app-error.log` to **CloudWatch Logs**.
3. A **metric filter** in CloudWatch detects lines containing `ERROR`.
4. When errors exceed a threshold, a **CloudWatch Alarm → SNS topic** sends Email/SMS alerts.
5. The app also pushes critical error events to **SQS**, which triggers a **Lambda** function for async processing.
6. Logs are exported/archived to **S3** and automatically transitioned to **S3 Glacier** via **Lifecycle rules** for cost optimisation.
7. **CloudTrail** tracks security-related changes (IAM, EC2, S3).
8. **Systems Manager (SSM)** runs log cleanup and patching commands on EC2.
9. **ALB + Auto Scaling Group** scale the log-generating application based on load.

---

## 🔧 AWS Services Used

- **Compute & Networking**
  - EC2 (app servers)
  - VPC (public + private subnets, NAT)
  - Elastic Load Balancer (ALB)
  - Auto Scaling Group

- **Monitoring & Logging**
  - CloudWatch Logs
  - CloudWatch Metric Filters & Alarms

- **Messaging & Processing**
  - SNS (alerts)
  - SQS (log events queue)
  - Lambda (process log events)

- **Storage & Cost Optimisation**
  - S3 (log archive)
  - S3 Lifecycle → Glacier Flexible Retrieval

- **Security & Management**
  - IAM Roles (EC2 → CloudWatch, S3, SSM)
  - CloudTrail (audit)
  - Systems Manager (Session Manager + Run Command)

---
├─ docs/
│   ├─ lifecycle-config.md
│   └─ cloudwatch-alert.md
└─ screenshots/
    └─ (add screenshots: s3-lifecycle.png, cloudwatch-logs.png, sns-email.png, etc.)
