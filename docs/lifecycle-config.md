# S3 Lifecycle Rule — Archive Logs to Glacier

1. Open S3 → Bucket → Management tab → Lifecycle rules
2. Create rule: `Move-to-Glacier`
3. Scope: Apply to all objects
4. Transition settings:
5. (Optional) Expiration: Delete after 365 days

📌 Purpose: Reduce long-term storage cost by ~70–80%.
