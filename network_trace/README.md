# Traffic Traces Preparation

Due to copyright issues and the size of the trace files, the traffic traces are not available on GitHub. Users need to prepare these traces themselves.

## MAWI Traffic Traces

The traffic trace used for CCAN anomaly detection is available in the MAWI traffic archive:  
[https://mawi.wide.ad.jp/mawi/samplepoint-F/2022/202201101400.html](https://mawi.wide.ad.jp/mawi/samplepoint-F/2022/202201101400.html)

## Synthetic Trace 

We prepared the synthetic trace `Merged_MAWI19040918+CAIDAdual_oneway.pcap` for Weibull model parameters by merging selected sections of the attack period with chosen background traffic from the MAWI DITL 2019 trace archive.

### MAWI with CAIDA2007

1. **CAIDA 2007 DDoS Trace (Attacking):**  
   Four DDoS attack traffic traces were selected from the CAIDA 2007 DDoS dataset (to-victim):
   - 20070804_140436.pcap
   - 20070804_140936.pcap
   - 20070804_141436.pcap
   - 20070804_141936.pcap
   
   These four traces were merged to form an attack traffic dataset spanning 15 minutes, containing a total of 50,841,437 packets.

2. **MAWI DITL 2019 Trace (Background):**  
   The synthetic background trace spans a total time of 60 minutes. It consists of four selected MAWI DITL 2019 traces (15 minutes each):
   - 201904091800.pcap — 98,815,892 packets (69,564.48 MB)
   - 201904091815.pcap — 101,892,458 packets (73,789.79 MB)
   - 201904091830.pcap — 93,470,901 packets (65,392.17 MB)
   - 201904091845.pcap — 91,074,784 packets (65,364.02 MB)
   
   More details can be found at:  
   [https://mawi.wide.ad.jp/mawi/ditl/ditl2019/201904091800.html](https://mawi.wide.ad.jp/mawi/ditl/ditl2019/201904091800.html)

### MAWI with CICDDoS2019
We prepared several synthetic traces using methods described in lab senior's thesis. The process focused on extracting single-direction MAWI and CIC pcap files based on the source MAC address.

1. **Trace Extraction and Filtering:**
   - We used `count_mac.sh` to identify the two most common source MAC addresses in each MAWI pcap file.
   - `auto_filter_v2.sh` was then used to filter the MAWI files based on these MAC addresses.

2. **Packet Count Analysis and Visualization:**
   - Recognizing that a DDoS attack often leads to an increase in packet count, we analyzed the packet count distribution within the MAWI files using a C program (`PacketParing.C`).
   - The results were visualized using `plot.py`, highlighting the first quartile (Q1), second quartile (Q2), and third quartile (Q3).
   - Attack traffic was inserted for timestamps below Q1.

3. **CICDDoS2019 Trace Integration:**
   - The CICDDoS2019 trace was obtained from [the CIC dataset website](https://www.unb.ca/cic/datasets/ddos-2019.html). Each file is fixed at 200MB.
   - We used `CICshift.sh` to adjust Unix timestamps to match the attack times listed on the website.
   - `CIC1103ATK_v2.sh` was used to aggregate the attack traffic by specific types.

4. **Merging with MAWI Traces:**
   - `merge_CIC_MAWI_v2.sh` was used to merge the MAWI and CICDDoS2019 traffic.
   - Timestamps with packet counts below Q1 in the MAWI files were identified, and the corresponding timestamps were extracted.
   - Using the `RANDOM` Bash variable, random timestamps were selected to insert the attack traffic to minimize the human factor.
   - An attempt count was set to prevent exceeding the background MAWI traffic.
   - Finally, the attack traffic's Unix timestamps were shifted to align with the selected insertion points in the MAWI traffic.
5. **Synthetic Trace Details:**
   - **CICDDoS2019 Trace (Attacking):**
   - **MAWI DITL 2019 Trace (Background):**
