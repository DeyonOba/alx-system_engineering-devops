# 0x19 Postmortem

## Task 1
### Issue Summary:

- **Duration**: The outage, caused by a misconfigured network switch, lasted from 10:00 AM to 1:00 PM on May 10th, 2024 (UTC-5).
- **Impact**: Luckily, only 30% of our users were affected by the outage, sparing us from potential disaster.
- **Root Cause**: It turns out that even seasoned engineers can sometimes overlook the most basic settings.

### Timeline:

- **10:00 AM**: Monitoring alerts rudely interrupted our morning coffee, indicating a significant drop in user activity.
- **10:10 AM**: Engineers, still groggy from caffeine deprivation, stumbled into action, suspecting a software bug.
- **10:30 AM**: Like detectives in a mystery novel, we delved into the depths of our application logs, searching for clues but finding only the mundane.
- **11:00 AM**: Fingers were pointed at the database, which, unsurprisingly, turned out to be innocent.
- **11:30 AM**: Panic briefly ensued as we entertained wild theories of a DDoS attack, but the evidence failed to materialize.
- **12:00 PM**: The cavalry arrived in the form of network infrastructure specialists, who promptly uncovered the culprit—a misconfigured network switch.
- **1:00 PM**: With a collective sigh of relief, the network switch was reconfigured, and our service sprung back to life like a phoenix from the ashes.

### Root Cause and Resolution:

- **Root Cause**: In a twist worthy of a sitcom plot, it was discovered that a simple misconfiguration of a network switch had caused the chaos.
- **Resolution**: The issue was swiftly remedied by correcting the network switch settings, proving once again that sometimes the simplest solutions are the most effective.

### Corrective and Preventative Measures:

- **Improvements/Fixes**: To prevent future mishaps, we'll be enhancing our monitoring systems to catch anomalies before they snowball into outages. Additionally, regular audits of network configurations will become as routine as our morning coffee.
 
### Tasks to Address the Issue:
- Implement automated network configuration checks to catch misconfigurations before they wreak havoc.
- Conduct a thorough review of all network infrastructure to ensure it's playing nice with each other.
- Bolster our incident response procedures to streamline the chaos when things inevitably go awry.
- Provide refresher courses for engineers on the basics of network troubleshooting—because sometimes it's the little things that trip us up.
- Develop a backup plan for network switch configurations, because as they say, "fool me once, shame on you; fool me twice, well, let's not find out."
