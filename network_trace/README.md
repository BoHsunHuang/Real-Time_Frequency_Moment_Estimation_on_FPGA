# Real-Time_Frequency_Moment_Estimation network trace

## Traffic Traces
(1)Scan anomaly detection
The traffic trace (202201101400) is available in the MAWI traffic archive. (https://mawi.wide.ad.jp/mawi/samplepoint-F/2022/202201101400.html)

(2)Weibull model parameters
We prepared the synthetic trace (Merged_MAWI19040918+CAIDAdual_oneway.pcap) by merging two sections of the attacking period with the chosen background traffic from MAWI DITL 2019 trace archive. 

(a)CAIDA 2007 DDoS trace (Attacking):
Four DDoS attacking traffic are selected from the CAIDA 2007 DDoS trace (to-victim).
20070804_140436.pcap
20070804_140936.pcap
20070804_141436.pcap
20070804_141936.pcap
 We merge those four traces and form an attacking traffic of 15 minutes with a total packet of 50,841,437.


(b) MAWI DITL 2019 trace (Background): 
The total time of the synthetic background trace is 60 minutes. 
The background traffic consists of four selected MAWI DITL2019 traces (15 min each), which are listed as follows.
201904091800.pcap # of packets: 98,815,892 (69564.48MB)
201904091815.pcap # of packets: 101892458 (73789.79MB)
201904091830.pcap # of packets: 93470901 (65392.17MB)
201904091845.pcap # of packets: 91074784 (65364.02MB)
https://mawi.wide.ad.jp/mawi/ditl/ditl2019/201904091800.html