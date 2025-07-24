## 💡 How to Import Alerting System in OpenSearch Dashboard

1. Click on the left panel and select Dev Tools at th bottom.

2. Go to Dev Tools.

3. Paste the above JSON in the left panel(without the cURL headers).

4. Ctrl+ A and Hit Play ▶️ to create the detector.

5. Some Configurations :

![Config](/Assests/Alerting_Config.png)
---

**Message subject:** 
``` bash
Alerting Notification action
```
**Message:**
``` bash
Monitor {{ctx.monitor.name}} just entered alert status. Please investigate the issue.
  - Trigger: {{ctx.trigger.name}}
  - Severity: {{ctx.trigger.severity}}
  - Period start: {{ctx.periodStart}}
  - Period end: {{ctx.periodEnd}}
```

![Configuration](/Assests/Alerting_Config1.png)