# Scenario2

## Overview 

Consider having a <b>frontend server</b> (Nginx or Apache) which is used for SSL offloading and proxies around 25000 requests per second. What metric would be interesting to monitor in that specific case and why and how would we acheive that?

<!--- BEGIN_TF_DOCS --->

## Requirements

| Name | Version |
|------|---------|
| Nginx | 1.17.0 |

## Server specs

```
● 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
● 64GB of ram
● 2 TB HDD disk space
● 2 x 10Gbit/s nics
```

## Required metrics to monitor

Suppose we have a high performance web server with aforesaid specs and proxying request 25K per second. The major factors to monitor for me would be describe below.

### Monitoring 
| Name | Info |
|------|---------|
| nginx_request | Monitor nginx request calls per second - metrics is imports |
| Number of connections | 1 layer Up ( LB->web ) and 1 layer down ( Web->App Server )-- Number of connection should be equal and which will confirm that all requests are passing thru without any delay |  
| CPU stats/Loadavg | How many cores are free and busy. Suppose if we have 8 cores then we can have 6 workers in nginx which will handle incoming requests |
| HDD/Swap Memory utilisation | During SSL offloading  to thread pools is implemented only for three essential operations: the read() syscall on most operating systems, sendfile() on Linux, and aio_write() on Linux which is used when writing some temporary files such as those for the cache |

| <b>worker_process/worker_thread</b> | Handles the incoming requests with SSLOffloading or zipping tasks. If we have 1 core then we can create 2 worker_process to handle requests and will have 2 running processes with the name of nginx: worker process. If we setup 8 value to worker_process then we will have more gates to serve incoming requests |

| <b>worker_connections </b> | This value defines the maximum number of TCP sessions per worker. Same as TPS connections- by default nginx run only 1 process with 512 connections means we will only be able to serve 512 clients. and If 2 processes with 512 connections each, we will be able to handle 2x512=1024 clients. The number of connections is limited by the maximum number of open files (RLIMIT_NOFILE) on our system |

| <b>worker_rlimit_nofile</b>  | Maximum number of open files can be opened by per worker process which will give another level of high throughput |
| meminfo | Memory related metrics of server to identify memory issues |

		
### SSL offloading
During SSL offloading to thread pools is implemented only for three essential operations: the read() syscall on most operating systems, sendfile() on Linux, and aio_write() on Linux which is used when writing some temporary files such as those for the cache.

### Benchmarking#####

So lets say we receive 25k requests per seconds 
(nginx default is 512 connections per worker, default thread 32 with max_queue=65536)

4 Intel® Xeon® Processor E7-4830 v4  (Core - 56, Thread - 112)

Network 
10GBPS x 2 Interfaces

Ram 64GB


-- 

So i can go with worker_process(CPU Cores) 40 and 600 worker_connections which will easilty take care of approx 25k requests per second and rest cores will be used for other OS operation tasks.

## Challenges:
- Upstream connections - We are not sure about how much data we receive during peak hours
- 3rd Party clients: We may have to connect to 3rd parties via HTTP calls which does not require HTTPS so how can we solve that.
- Key Sizes of Requests : As key sizes increases SSL processing will be CPU intensive. How to measure Key sizes?
- Public Facing Firewall Monitoring : Many hackers try to connect hardware firewell which consists Security Threats, DDoS attacks,Spoofing and that requires lot of security skill to take care of it


## Best Practice:
- We can create NIC bonding on server to achieve high Load balancing and Fault tolerance
- We can enable security by set buffer size limitations for all clients to prevent potential DoS attacks on nginx
- We can disable DELETE and TRACE HTTP methods, which are not going to be utilized and which are not required to be implemented on the web server
- Enable WAF security as well
- Add another LB infornt of Web server to load the requests from public

## Tools
There are opensource and paid tools available in market to capture and provide better visual of Nginx dashboard with lots of features.

| Name | Info |
|------|---------|
| Nagios | Montinor tools for system and service UP and running status |
| Grafana | Can create dashboards to have visual on nginx metrics i.e. Nignx request, nginx connections status, nginx success rates, nginx error |
| Datadog APM (FREE TRIAL) | Cloud monitoring software with monitoring for over 180 NGINX metrics, dashboards, graphs, charts, anomaly detection, and more |
| Dynatrace | Application performance monitoring software with auto-discovery for NGINX web servers, a dependency map, anomaly detection, and more |
| NGINX Amplify | NGINX monitoring software for NGINX Open Source and NGINX Plus with custom dashboards, recommendations, alerts, and more |
| ManageEngine Applications Manager  | Application monitoring software with NGINX and NGINX Plus monitoring with graphs, charts, alerts, reports, and more |
| AppDynamics | Application performance management platform with NGINX and NGINX Plus monitoring with a customizable dashboard, anomaly detection, alerts, and more. |
| New Relic | Application monitoring software with NGINX integration, dashboard, alerts, reports, graphs, charts
