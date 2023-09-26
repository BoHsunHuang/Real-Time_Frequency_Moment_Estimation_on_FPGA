# **Hardware Architecture**

## **Section I: System Requirement Dependency**
### Operating Systems
* Ubuntu 20.04 
* Linux Kernel 5.3.0-050300
* [open-nic-driver](<http://example.com/Hello World.html> "Title")

### Xilinx Tools
* Vivado 2020.2

### Xilinx Design and Xilinx IP License

### Development

### Section II: Get the code base for NetFPGA-PLUS

Vivado Ver


OS

Compile Script/

Only /bit file is available now

## NetFPGA-PLUS IP Core 
```sh
$NFPLUS_FOLDER/hw/lib/std/my_module
```
### Frequency Moments & Shannon Entropy Estimation Module:
Top Module：my_module.v
1. Hash Function
    * hash_ams_u.v (2-Universal Hash)
    * hash3.v (Hash3)
2. Frequency Moment
    * count_sketch.v
    * estimate_freq.v
    * find_median.v
3. Entropy
    * clifford_top.v
    * clifford_findx.v
    * clifford_interpolation.v
4. Distinct Count
    * pcsa.v
5. Header Parser
    * header_parser.v


## Project
Please reference to the Vivado docs.

## HDL Simulation
Please reference to the Reference_NIC project.
```sh
$NF_DESIGN_DIR/test/both_loopback_maxsize/run.py
```

## Real Traffic Test
Under the "real_test" directory, please recompile the application and driver codes.

```shell
$ make compile-hwtestlib
$ make compile-driver
```
## Program the FPGA bit file
```shell
$ make bit
```
Need to do a warm reboot.

## Update the table and parameters
```shell
$ make update
```
## Starts the dashboard 
```shell
$ make read
```
