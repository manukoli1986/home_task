# Scenario2

## Overview 

Consider having a <b>frontend server</b> (Nginx or Apache) which is used for SSL offloading and proxies around 25000 requests per second. What metric would be interesting to monitor in that specific case and why and how would we acheive that?

<!--- BEGIN_TF_DOCS --->

## Required metrics to monitor

| Name | Info |
|------|---------|
| nginx requests | Will figure out max and average request we get |
| netstat | Get key network metrics from SSL-offloading or proxy server |
| uptime | Uptime will share information for how long server is UP | 
| Number of process | how many concurrently process are running |
| filesystem | To track the disk space of the server from different partitions|
| cpu stats | SSL Offloading is cpu sensitive process so its important to monitor CPU metrics (user,system,io,nice) |
| disk stats | To measure DISK IO of the server while performing Encrytion / Decryption |
| meminfo | Memory related metrics of server to identify memory issues |
| loadavg | Load averages can be useful for a quick and dirty idea if a machine has gotten busier (for some definition of busier) recently |



## Server specs

```
● 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
● 64GB of ram
● 2 TB HDD disk space
● 2 x 10Gbit/s nics
```

## Solution 