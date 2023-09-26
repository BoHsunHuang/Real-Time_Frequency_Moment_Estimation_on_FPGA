#!/usr/bin/python
# /-
# / Copyright (c) 2015,2021 University of Cambridge
# / All rights reserved.
# /
# / This software was developed by Stanford University and the University of Cambridge Computer Laboratory 
# / under National Science Foundation under Grant No. CNS-0855268,
# / the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and
# / by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"), 
# / as part of the DARPA MRC research programme,
# / and by the University of Cambridge Computer Laboratory under EPSRC EARL Project
# / EP/P025374/1 alongside support from Xilinx Inc.
# /
# / @NETFPGA_LICENSE_HEADER_START@
# /
# / Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor
# / license agreements.  See the NOTICE file distributed with this work for
# / additional information regarding copyright ownership.  NetFPGA licenses this
# / file to you under the NetFPGA Hardware-Software License, Version 1.0 (the
# / "License"); you may not use this file except in compliance with the
# / License.  You may obtain a copy of the License at:
# /
# /   http://www.netfpga-cic.org
# /
# / Unless required by applicable law or agreed to in writing, Work distributed
# / under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# / CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# / specific language governing permissions and limitations under the License.
# /
# / @NETFPGA_LICENSE_HEADER_END@
# ////////////////////////////////////////////////////////////////////////////////
# / This is an automatically generated header definitions file
# ////////////////////////////////////////////////////////////////////////////////

# /######################################################
# /# Definitions for INPUT_ARBITER
# /######################################################
def NFPLUS_INPUT_ARBITER_BASEADDR():
    return 0x00010000
def NFPLUS_INPUT_ARBITER_HIGHADDR():
    return 0x00010FFF
def NFPLUS_INPUT_ARBITER_SIZEADDR():
    return 0x1000

def NFPLUS_INPUT_ARBITER_0_ID():
    return 0x10000
def NFPLUS_INPUT_ARBITER_0_ID_DEFAULT():
    return 0x0000DA01
def NFPLUS_INPUT_ARBITER_0_ID_WIDTH():
    return 32
def NFPLUS_INPUT_ARBITER_0_VERSION():
    return 0x10004
def NFPLUS_INPUT_ARBITER_0_VERSION_DEFAULT():
    return 0x1
def NFPLUS_INPUT_ARBITER_0_VERSION_WIDTH():
    return 32
def NFPLUS_INPUT_ARBITER_0_RESET():
    return 0x10008
def NFPLUS_INPUT_ARBITER_0_RESET_DEFAULT():
    return 0x0
def NFPLUS_INPUT_ARBITER_0_RESET_WIDTH():
    return 16
def NFPLUS_INPUT_ARBITER_0_FLIP():
    return 0x1000c
def NFPLUS_INPUT_ARBITER_0_FLIP_DEFAULT():
    return 0x0
def NFPLUS_INPUT_ARBITER_0_FLIP_WIDTH():
    return 32
def NFPLUS_INPUT_ARBITER_0_DEBUG():
    return 0x10010
def NFPLUS_INPUT_ARBITER_0_DEBUG_DEFAULT():
    return 0x0
def NFPLUS_INPUT_ARBITER_0_DEBUG_WIDTH():
    return 32
def NFPLUS_INPUT_ARBITER_0_PKTIN():
    return 0x10014
def NFPLUS_INPUT_ARBITER_0_PKTIN_DEFAULT():
    return 0x0
def NFPLUS_INPUT_ARBITER_0_PKTIN_WIDTH():
    return 32
def NFPLUS_INPUT_ARBITER_0_PKTOUT():
    return 0x10018
def NFPLUS_INPUT_ARBITER_0_PKTOUT_DEFAULT():
    return 0x0
def NFPLUS_INPUT_ARBITER_0_PKTOUT_WIDTH():
    return 32

# /######################################################
# /# Definitions for OUTPUT_QUEUES
# /######################################################
def NFPLUS_OUTPUT_QUEUES_BASEADDR():
    return 0x00030000
def NFPLUS_OUTPUT_QUEUES_HIGHADDR():
    return 0x00030FFF
def NFPLUS_OUTPUT_QUEUES_SIZEADDR():
    return 0x1000

def NFPLUS_OUTPUT_QUEUES_0_ID():
    return 0x30000
def NFPLUS_OUTPUT_QUEUES_0_ID_DEFAULT():
    return 0x0000DA03
def NFPLUS_OUTPUT_QUEUES_0_ID_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_VERSION():
    return 0x30004
def NFPLUS_OUTPUT_QUEUES_0_VERSION_DEFAULT():
    return 0x1
def NFPLUS_OUTPUT_QUEUES_0_VERSION_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_RESET():
    return 0x30008
def NFPLUS_OUTPUT_QUEUES_0_RESET_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_RESET_WIDTH():
    return 16
def NFPLUS_OUTPUT_QUEUES_0_FLIP():
    return 0x3000c
def NFPLUS_OUTPUT_QUEUES_0_FLIP_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_FLIP_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_DEBUG():
    return 0x30010
def NFPLUS_OUTPUT_QUEUES_0_DEBUG_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_DEBUG_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTIN():
    return 0x30014
def NFPLUS_OUTPUT_QUEUES_0_PKTIN_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTIN_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTOUT():
    return 0x30018
def NFPLUS_OUTPUT_QUEUES_0_PKTOUT_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTOUT_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT0():
    return 0x3001c
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT0():
    return 0x30020
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT0():
    return 0x30024
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT0():
    return 0x30028
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT0():
    return 0x3002c
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT0():
    return 0x30030
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT0():
    return 0x30034
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT0_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT0_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT1():
    return 0x30038
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT1():
    return 0x3003c
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT1():
    return 0x30040
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT1():
    return 0x30044
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT1():
    return 0x30048
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT1():
    return 0x3004c
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT1():
    return 0x30050
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT1_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT1_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT2():
    return 0x30054
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTSTOREDPORT2_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT2():
    return 0x30058
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESSTOREDPORT2_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT2():
    return 0x3005c
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTREMOVEDPORT2_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT2():
    return 0x30060
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESREMOVEDPORT2_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT2():
    return 0x30064
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTDROPPEDPORT2_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT2():
    return 0x30068
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_BYTESDROPPEDPORT2_WIDTH():
    return 32
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT2():
    return 0x3006c
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT2_DEFAULT():
    return 0x0
def NFPLUS_OUTPUT_QUEUES_0_PKTINQUEUEPORT2_WIDTH():
    return 32

# /######################################################
# /# Definitions for MY_MODULE
# /######################################################
def NFPLUS_MY_MODULE_BASEADDR():
    return 0x00020000
def NFPLUS_MY_MODULE_HIGHADDR():
    return 0x00020FFF
def NFPLUS_MY_MODULE_SIZEADDR():
    return 0x1000

def NFPLUS_MY_MODULE_0_TABLE_ID():
    return 0x20000
def NFPLUS_MY_MODULE_0_TABLE_ID_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_TABLE_ID_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_TABLE_VALUE_W():
    return 0x20004
def NFPLUS_MY_MODULE_0_TABLE_VALUE_W_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_TABLE_VALUE_W_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_TABLE_VALID_W():
    return 0x20008
def NFPLUS_MY_MODULE_0_TABLE_VALID_W_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_TABLE_VALID_W_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_TABLE_VALUE_R():
    return 0x2000c
def NFPLUS_MY_MODULE_0_TABLE_VALUE_R_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_TABLE_VALUE_R_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_TABLE_VALID_R():
    return 0x20010
def NFPLUS_MY_MODULE_0_TABLE_VALID_R_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_TABLE_VALID_R_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_READ_AND_CLEAR():
    return 0x20014
def NFPLUS_MY_MODULE_0_READ_AND_CLEAR_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_READ_AND_CLEAR_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F2_SRCIP():
    return 0x20018
def NFPLUS_MY_MODULE_0_F2_SRCIP_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F2_SRCIP_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F3_SRCIP():
    return 0x2001c
def NFPLUS_MY_MODULE_0_F3_SRCIP_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F3_SRCIP_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F4_SRCIP():
    return 0x20020
def NFPLUS_MY_MODULE_0_F4_SRCIP_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F4_SRCIP_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F2_DSTIP():
    return 0x20024
def NFPLUS_MY_MODULE_0_F2_DSTIP_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F2_DSTIP_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F3_DSTIP():
    return 0x20028
def NFPLUS_MY_MODULE_0_F3_DSTIP_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F3_DSTIP_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F4_DSTIP():
    return 0x2002c
def NFPLUS_MY_MODULE_0_F4_DSTIP_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F4_DSTIP_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F2_SRCPORT():
    return 0x20030
def NFPLUS_MY_MODULE_0_F2_SRCPORT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F2_SRCPORT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F3_SRCPORT():
    return 0x20034
def NFPLUS_MY_MODULE_0_F3_SRCPORT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F3_SRCPORT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F4_SRCPORT():
    return 0x20038
def NFPLUS_MY_MODULE_0_F4_SRCPORT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F4_SRCPORT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F2_DSTPORT():
    return 0x2003c
def NFPLUS_MY_MODULE_0_F2_DSTPORT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F2_DSTPORT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F3_DSTPORT():
    return 0x20040
def NFPLUS_MY_MODULE_0_F3_DSTPORT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F3_DSTPORT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F4_DSTPORT():
    return 0x20044
def NFPLUS_MY_MODULE_0_F4_DSTPORT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F4_DSTPORT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F2_PROTOCOL():
    return 0x20048
def NFPLUS_MY_MODULE_0_F2_PROTOCOL_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F2_PROTOCOL_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F3_PROTOCOL():
    return 0x2004c
def NFPLUS_MY_MODULE_0_F3_PROTOCOL_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F3_PROTOCOL_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_F4_PROTOCOL():
    return 0x20050
def NFPLUS_MY_MODULE_0_F4_PROTOCOL_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_F4_PROTOCOL_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_PACKET_CNT():
    return 0x20054
def NFPLUS_MY_MODULE_0_PACKET_CNT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_PACKET_CNT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_STATUS():
    return 0x20058
def NFPLUS_MY_MODULE_0_STATUS_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_STATUS_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_ENTROPY_SRCIP_Y():
    return 0x2005c
def NFPLUS_MY_MODULE_0_ENTROPY_SRCIP_Y_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_ENTROPY_SRCIP_Y_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_ENTROPY_DSTIP_Y():
    return 0x20060
def NFPLUS_MY_MODULE_0_ENTROPY_DSTIP_Y_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_ENTROPY_DSTIP_Y_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_ENTROPY_SRCPORT_Y():
    return 0x20064
def NFPLUS_MY_MODULE_0_ENTROPY_SRCPORT_Y_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_ENTROPY_SRCPORT_Y_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_ENTROPY_DSTPORT_Y():
    return 0x20068
def NFPLUS_MY_MODULE_0_ENTROPY_DSTPORT_Y_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_ENTROPY_DSTPORT_Y_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_ENTROPY_PROTOCOL_Y():
    return 0x2006c
def NFPLUS_MY_MODULE_0_ENTROPY_PROTOCOL_Y_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_ENTROPY_PROTOCOL_Y_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_READ_FREQ_PTR():
    return 0x20070
def NFPLUS_MY_MODULE_0_READ_FREQ_PTR_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_READ_FREQ_PTR_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_DISTINCT_COUNT():
    return 0x20074
def NFPLUS_MY_MODULE_0_DISTINCT_COUNT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_DISTINCT_COUNT_WIDTH():
    return 32
def NFPLUS_MY_MODULE_0_PORT_CNT():
    return 0x20078
def NFPLUS_MY_MODULE_0_PORT_CNT_DEFAULT():
    return 0x0
def NFPLUS_MY_MODULE_0_PORT_CNT_WIDTH():
    return 32
