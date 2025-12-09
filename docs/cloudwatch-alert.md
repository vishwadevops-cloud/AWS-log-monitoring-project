# CloudWatch Metric Filter & SNS Alert

1. Create Metric Filter on `App-Error-Logs`
   Pattern: ERROR
   Metric namespace: LogMonitoring
   Metric name: ErrorCount

2. Create CloudWatch Alarm
   Condition: Sum ≥ 5 in 1 minute
   Action: SNS → Email alert
3. Test
   Run: for i in {1..20}; do echo "$(date) ERROR TEST" | sudo tee -a /var/log/app-error.log; done
   Alarm triggers  →  Email received via SNS.