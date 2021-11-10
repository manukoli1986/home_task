#Scenario2

## Overview 

Consider having a frontend server (Nginx or Apache) which is used for SSL offloading and proxies around 25000 requests per second. What metric would be interesting to monitor in that specific case and why and how would we acheive that?

<!--- BEGIN_TF_DOCS --->

## Required metrics to monitor

| Name | Info |
|------|---------|
| netstat | Get key network metrics from SSL-offloading or proxy server |
| filesystem | To track the disk space of the server from different partitions|
| cpu stats | SSL Offloading is cpu sensitive process so its important to monitor CPU metrics (user,system,io,nice) |
| disk stats | To measure DISK IO of the server while performing Encrytion / Decryption |
| meminfo | Memory related metrics of server to identify memory issues |
| loadavg | Load averages can be useful for a quick and dirty idea if a machine has gotten busier (for some definition of busier) recently |

