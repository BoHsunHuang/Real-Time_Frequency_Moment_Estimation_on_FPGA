# **Hardware Architecture**
We use the NetFPGA-PlUS framework for the development and validation of network performance features.

## **Section I: System Requirement Dependency**
Please refer to the [NetFPGA Wiki](<https://github.com/NetFPGA/NetFPGA-PLUS/wiki/Reference-Operating-System-Setup-Guide>) for instructions on building the experimental environment.
### Operating Systems
For detailed configuration steps, please refer to the [NetFPGA-PLUS operating system](<https://github.com/NetFPGA/NetFPGA-PLUS/wiki/Reference-Operating-System-Setup-Guide>) setup or [open-nic-driver](<https://github.com/Xilinx/open-nic-driver> "Title").
* Ubuntu 20.04 
* Linux Kernel 5.3.0-050300
* open-nic-driver

### Xilinx Tools
* Vivado 2020.2
* [Alveo U200 Data Center Accelerator Card](<https://www.xilinx.com/products/boards-and-kits/alveo/u200.html> "Title")
* 100GbE Ethernet Subsystem
* QDMA

### Xilinx Design and Xilinx IP License
The NetFPGA-PlUS using Xilinx CMAC IP, a license would be required. Please see this [License Information page](<https://www.xilinx.com/products/intellectual-property/cmac_usplus.html> "Title") or [open-nic-shell](<https://github.com/Xilinx/open-nic-shell> "Title") page.

### Python Environment

The requirements.txt file should list all Python libraries that our dashboard depend on, and you will be installed using:
* Python 3.8.10
``` bash
pip install -r requirements.txt
```

### Section II: Get the code base for Real-Time_Frequency_Moment_Estimation_on_FPGA and Build up!!!
We provide automated testing scripts; please use `make` for automated testing. Please follow the instructions below for configuration.

```bash
$ git clone git@github.com:BoHsunHuang/Real-Time_Frequency_Moment_Estimation_on_FPGA.git    # Change the path to "hardware"
$ cd ./hardware             # Change the path to "hardware"
$ make compile-hwtestlib    # Compile a C language shared library.
$ make compile-driver       # Compile the NetFPGA-PLUS framework system driver.
$ make bit                  # Progamming FPGA Bitstream and Auto Reboot
$ make Update               # Initialize the hash module function and update the table data.
$ make read                 # Launch the user dashboard interface.
```

### Section III: Replay Traffic for System Testing.

Please install the traffic replay tool `Tcpreplay`.
```bash
$ sudo tcpreplay -i <network card interface> --multiplier=1 <user_define>.pcap    # Replay the traffic using tcpreplay.
```


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
