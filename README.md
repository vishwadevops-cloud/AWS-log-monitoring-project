# 🚀 AWS Event-Driven Log Monitoring & Alerting System

This project implements a real-time monitoring and alerting pipeline on AWS.  
It detects error patterns from application logs and sends instant notifications to the DevOps team.

---

## 📍 Architecture Overview

| AWS Service | Role |
|------------|------|
| EC2 | Application + log generation |
| CloudWatch Logs | Central log collection |
| CloudWatch Metric Filter | Scans for the keyword **"ERROR"** |
| CloudWatch Alarm | Triggers when error count threshold is crossed |
| SNS | Sends alert via email/SMS |
| IAM | Access permissions for EC2 to push logs |
| S3 + Lifecycle | Archives old logs → moves to Glacier to reduce cost |
| SSM | Log cleanup/maintenance automation |

---

## 🔥 Key Features
✔ EC2 application generates logs at `/var/log/app-error.log`  
✔ CloudWatch Agent streams logs automatically  
✔ Metric filter detects `"ERROR"` messages  
✔ SNS alert is triggered when errors ≥ 5 in 1 minute  
✔ Logs archived to S3 with **Lifecycle → Glacier** for cost optimisation  

---

## 📁 Project Files
| File | Purpose |
|------|---------|
| `setup.sh` | EC2 bootstrap script to install + configure CloudWatch Agent |
| `log_generator.py` | Generates continuous INFO + ERROR logs |
| `docs/cloudwatch-alert.md` | Alarm + SNS setup steps |
| `docs/lifecycle-config.md` | S3 lifecycle → Glacier costing rule |
| `screenshots/` | Proof of execution |

---

## 📷 Proof of Execution (Screenshots)

### 🔔 CloudWatch Alarm Trigger
![Alarm Trigger](https://raw.githubusercontent.com/vishwadevops-cloud/AWS-log-monitoring-project/main/Alarm-Graph.png)

### 📩 SNS Email Alert
![Email Alert](https://raw.githubusercontent.com/vishwadevops-cloud/AWS-log-monitoring-project/main/Email-Alert.png)

### 📊 CloudWatch Live Logs
![Live Logs](https://raw.githubusercontent.com/vishwadevops-cloud/AWS-log-monitoring-project/main/Live-Logs.png)

### 🧊 S3 Lifecycle Rule
![Lifecycle Rule](https://raw.githubusercontent.com/vishwadevops-cloud/AWS-log-monitoring-project/main/S3_Life_Cycle.png)
