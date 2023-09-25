# Real-Time_Frequency_Moment_Estimation_on_FPGA

This paper presents an implementation of the Frequency Moment estimation utilizing the 100Gbps Xilinx Alveo U200 acceleration card of the NetFPGA-PLUS platform. We further showcase its applications in scan anomaly detection and parameter estimation for the Weibull model of flow length distribution.

The frequency moment estimator is realized by Verilog HDL in the data plane of the NetFPGA-Plus framework in an UltraScale+ XCU200 FPGA.


The trace is re-played by using TCPReplay via Mellanox ConnectX-5 100G NIC to the Xilinx Alveo U200 FPGA card through a QSFP28 AOC Cable. 
