# 0x19 Postmortem

## Task 1
### Issue Summary:

- **Duration**: The outage occurred from 10:00 AM to 1:00 PM on May 10th, 2024 (UTC-5).
- **Impact**: The outage affected 30% of our users, resulting in complete unavailability of our primary service.
- **Root Cause**: The root cause was identified as a misconfigured network switch.

### Timeline:

- **10:00 AM**: Issue detected through monitoring alerts showing a sudden drop in user activity.
- **10:10 AM**: Engineers investigated application logs assuming a software bug but found no abnormalities.
- **10:30 AM**: Initial suspicion turned to the database, leading to a thorough investigation of database servers.
- **11:00 AM**: With no issues found in the database, attention shifted to load balancers and networking components.
- **11:30 AM**: Misleading assumption about a DDoS attack explored, but no evidence found to support this theory.
- **12:00 PM**: Incident escalated to network infrastructure specialists and senior engineers.
- **12:30 PM**: Root cause identified as a misconfigured network switch.
- **1:00 PM**: Issue resolved by reconfiguring the network switch and restoring normal service.
- 
### Root Cause and Resolution:

- **Root Cause**: The misconfigured network switch caused a disruption in traffic routing, leading to service unavailability.
- **Resolution**: The issue was fixed by reconfiguring the network switch to its intended settings, restoring proper traffic flow.

### Corrective and Preventative Measures:

- **Improvements/Fixes**: Enhance monitoring systems to promptly detect network anomalies, conduct regular audits of network configurations to prevent similar issues in the future.

### Tasks to Address the Issue:
- Implement automated network configuration checks to detect discrepancies.
- Conduct a comprehensive review of network infrastructure to identify and rectify any other potential misconfigurations.
- Enhance incident response procedures to streamline escalation and resolution processes.
- Provide additional training for engineers on troubleshooting network-related issues.
- Develop and implement a backup plan for network switch configurations to expedite recovery in case of future incidents.
