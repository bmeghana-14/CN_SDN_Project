# CN_SDN_Project
# Network Delay Measurement Tool using SDN

## Problem Statement
Measure and analyze latency (delay) between hosts in a network using Software Defined Networking (SDN).

---

## Objective
- Measure delay using ping
- Record RTT (Round Trip Time) values
- Compare delays across different paths
- Analyze delay variation (jitter)

---

## Tools Used
- Mininet
- POX Controller
- Ubuntu (VMware)

---

## Project Architecture
- Linear topology with 3 hosts and 3 switches
- Remote SDN controller (POX)
- OpenFlow-based packet forwarding

---

## Setup Instructions

### 1. Start POX Controller
```bash
cd ~/pox
./pox.py log.level --DEBUG misc.delay_monitor
