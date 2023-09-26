from unittest import result
from reg_defines_reference_nic import *
import time
from param import *
import math
#C + Python
from ctypes import *
import numpy as np
import os
dir = os.path.dirname(__file__)
sume = cdll.LoadLibrary(dir+'/libsume.so')

read = sume.regread
write = sume.regwrite
exp = math.exp
log = math.log

def read_entropy():
    k_value = K_VALUE()
    hash_cnt = HASH_CNT()
    distinct = np.zeros(4)
    entropy = np.zeros((k_value, 4,5))

    srcip=0
    dstip=0
    srcport=0
    dstport=0
    protocol=0


    srcip_tmp=0
    dstip_tmp=0
    srcport_tmp=0
    dstport_tmp=0
    protocol_tmp=0


    write(NFPLUS_MY_MODULE_0_STATUS(), 0xEEEEEEEE)
    for i in range(4):
        R = (read(NFPLUS_MY_MODULE_0_DISTINCT_COUNT()))/128
        if(R):
            distinct[i] = (2**R)/0.77351*128
    
    
    total_cnt = read(NFPLUS_MY_MODULE_0_PACKET_CNT())
    print("PKT COUNT = ", end=" ")
    print(total_cnt)
    print("\n")
    port_cnt = read(NFPLUS_MY_MODULE_0_PORT_CNT())
    #print('Port Count')
    #print(port_cnt)
    print('Distinct Count')
    for i in range(4):   
        print(distinct[i])
    for i in range(k_value):
        for j in range(hash_cnt):
            srcip_high = (read(NFPLUS_MY_MODULE_0_ENTROPY_SRCIP_Y()))
            dstip_high = (read(NFPLUS_MY_MODULE_0_ENTROPY_DSTIP_Y()))
            srcport_high = (read(NFPLUS_MY_MODULE_0_ENTROPY_SRCPORT_Y()))
            dstport_high = (read(NFPLUS_MY_MODULE_0_ENTROPY_DSTPORT_Y()))
            protocol_high = (read(NFPLUS_MY_MODULE_0_ENTROPY_PROTOCOL_Y()))

            if(srcip_high<0):
                srcip_high = srcip_high+(2**32)
            if(dstip_high<0):
                dstip_high = dstip_high+(2**32)
            if(srcport_high<0):
                srcport_high = srcport_high+(2**32)
            if(dstport_high<0):
                dstport_high = dstport_high+(2**32)
            if(protocol_high<0):
                protocol_high = protocol_high+(2**32)

            #print ('{:x}'.format(srcip_high))

            srcip_low=(read(NFPLUS_MY_MODULE_0_ENTROPY_SRCIP_Y()))
            dstip_low=(read(NFPLUS_MY_MODULE_0_ENTROPY_DSTIP_Y()))
            srcport_low=(read(NFPLUS_MY_MODULE_0_ENTROPY_SRCPORT_Y()))
            dstport_low=(read(NFPLUS_MY_MODULE_0_ENTROPY_DSTPORT_Y()))
            protocol_low=(read(NFPLUS_MY_MODULE_0_ENTROPY_PROTOCOL_Y()))
            if(srcip_low<0):
                srcip_low = srcip_low+(2**32)
            if(dstip_low<0):
                dstip_low = dstip_low+(2**32)
            if(srcport_low<0):
                srcport_low = srcport_low+(2**32)
            if(dstport_low<0):
                dstport_low = dstport_low+(2**32)
            if(protocol_low<0):
                protocol_low = protocol_low+(2**32)
            srcip_tmp = srcip_high*(2**32) + srcip_low
            dstip_tmp = dstip_high*(2**32) + dstip_low
            srcport_tmp = srcport_high*(2**32) + srcport_low
            dstport_tmp = dstport_high*(2**32) + dstport_low
            protocol_tmp = protocol_high*(2**32) + protocol_low
            # print(a)
            if(srcip_tmp>=2**63):
                srcip_tmp = srcip_tmp-(2**64)
            if(dstip_tmp>=2**63):
                dstip_tmp = dstip_tmp-(2**64)
            if(srcport_tmp>=2**63):
                srcport_tmp = srcport_tmp-(2**64)
            if(dstport_tmp>=2**63):
                dstport_tmp = dstport_tmp-(2**64)
            if(protocol_tmp>=2**63):
                protocol_tmp = protocol_tmp-(2**64)
            #print ('srcip') 
            #print ('{:d}'.format(srcip_tmp)) 
            #print ('dstip')
            #print ('{:d}'.format(dstip_tmp))

            srcip_tmp = srcip_tmp/4096
            dstip_tmp = dstip_tmp/4096
            srcport_tmp = srcport_tmp/4096
            dstport_tmp = dstport_tmp/4096
            protocol_tmp = protocol_tmp/4096

            entropy[i][j][0] = srcip_tmp
            entropy[i][j][1] = dstip_tmp
            entropy[i][j][2] = srcport_tmp
            entropy[i][j][3] = dstport_tmp
            entropy[i][j][4] = protocol_tmp

    write(NFPLUS_MY_MODULE_0_STATUS(), 0xFFFFFFFF)
    write(NFPLUS_MY_MODULE_0_STATUS(), 0x0)

    



    for i in range(k_value):
        for j in range(hash_cnt):
            srcip += exp(entropy[i][j][0]/total_cnt)
            dstip += exp(entropy[i][j][1]/total_cnt)
            srcport += exp(entropy[i][j][2]/port_cnt)
            dstport += exp(entropy[i][j][3]/port_cnt)
            protocol += exp(entropy[i][j][4]/total_cnt)
            #print ('srcip') 
            #print ('{:.8f}'.format(srcip)) 
            #print ('dstip')
            #print ('{:.8f}'.format(dstip))
            #print ('srcport')
            #print ('{:.8f}'.format(srcport))
            #print ('dstport')
            #print ('{:.8f}'.format(dstport))
            #print ('protocol')
            #print ('{:.8f}'.format(protocol))

    srcip = -log(srcip/k_value/hash_cnt)
    dstip = -log(dstip/k_value/hash_cnt)
    srcport = -log(srcport/k_value/hash_cnt)
    dstport = -log(dstport/k_value/hash_cnt)
    protocol = -log(protocol/k_value/hash_cnt)

    #print('')
    #print ('Original Entropy')

      
    #print ('SrcIP    = {:.3f}\nDstIP    = {:.3f}\nSrcPort  = {:.3f}\nDstPort  = {:.3f}\nProtocol = {:.3f}  '.format(srcip, dstip, srcport, dstport, protocol))
    #print('')
    if(total_cnt > 1):
        srcip /= log(distinct[0])
        dstip /= log(distinct[1])
        srcport /= log(distinct[2])
        dstport /= log(distinct[3])
        protocol /= log(total_cnt)

    #print ('Normalized Entropy')

    #print ('SrcIP    = {:.3f}\nDstIP    = {:.3f}\nSrcPort  = {:.3f}\nDstPort  = {:.3f}\nProtocol = {:.3f}  '.format(srcip, dstip, srcport, dstport, protocol))
    #print('')
    return srcip, dstip, srcport, dstport, protocol, distinct[0], distinct[1], distinct[2], distinct[3], total_cnt
 
