# 0x19. Postmortem
## Postmortem: Apache 500 Error OUtage

![web stack debugging](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png)

### Issue Summary:

##### - Duration:  
- Start Time: November 07, 2023, 4:00 AM
- End Time: November 09, 2023, 4:00 AM  
##### - Impact:  
- The apache 500 Error resulted in a service outage affecting users attempting to access the web applicaion
- Approximately 30% of users experience were affected during the outage.
### Timeline:
##### - Issue Detection:
- Detected at November 08 2023, 3:00 AM through monitoring alert
##### - Actions Taken:  
  -Investigation: Engaged strace using tmux to trace system calls in one window and simultane ran curl in another to replicate the issue.
  -Assumption: misconfiguration in the apache process.
##### - Misleading Paths:
- Investigated configuration network
##### - Escalation:
- The incident was the system administration and Devlopement team for the initial troubleshooting.  
##### - Resolution:  
- By using strace identified incorrect file permissions on a critical apache configuration file.  
- Corrected file permissions manually and restarted apache to restore service
- Fix the file permission by using puppet.
### Root cause and Resolution:
##### - Root Cause:
- Incorrect file permissions prevented apache from accessing the configuration file
- To read the configuration file, strace repeated EACCES errors indicating Apache inability
##### - Resolution:
- Adjust the permission file manualy on the configuration file to grant the necessary read access.
- Automated the correction using puppet.
### Corrective and Preventative Measures:
##### - Improvement/Fixes:
- Enhance documentations on configuration file and required permissions.
##### - Tasks:
- Conduct a comprehensive review of the configuration file to identify potentiel vulnerabilities.
- Enhance puppet manifests to include a boarder range of configuration checks.
### Conclusion:
The apache 500 Error outage was addressed by identifying and correcting the file permission issues using strace and puppet, The incident highlighted and documentation implemented to prevent similar incidents.
