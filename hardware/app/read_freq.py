from reg_defines_reference_nic import *
from param import *
import time

#C + Python
from ctypes import *
import os
dir = os.path.dirname(__file__)
sume = cdll.LoadLibrary(dir+'/libsume.so')

read = sume.regread
write = sume.regwrite

def read_freq():
    #write(NFPLUS_MY_MODULE_0_READ_AND_CLEAR(), 0x1)
    #time.sleep(1/1000)
    f2_srcip = 0
    f2_dstip = 0
    f2_srcport = 0
    f2_dstport = 0
    f2_protocol = 0
    f3_srcip = 0
    f3_dstip = 0
    f3_srcport = 0
    f3_dstport = 0
    f3_protocol = 0
    f4_srcip = 0
    f4_dstip = 0
    f4_srcport = 0
    f4_dstport = 0
    f4_protocol = 0
    #read srcip f2~f4
    freq = 0
    for j in range(2):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (2-j))
        freq = read(NFPLUS_MY_MODULE_0_F2_SRCIP())
        if(freq<0):
            freq=freq+(2**32)  
        f2_srcip = (f2_srcip * (2**32)) + freq
    print ('---  SrcIP    F2 = {:<15d}  ---  '.format(f2_srcip),end='')
    freq = 0
    for j in range(3):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (3-j))
        freq = read(NFPLUS_MY_MODULE_0_F3_SRCIP()) 
        if(freq<0):
            freq=freq+(2**32) 
        f3_srcip = (f3_srcip * (2**32)) + freq
    print ('SrcIP    F3 = {:<20d}  ---  '.format(f3_srcip),end='')
    freq = 0
    for j in range(4):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (4-j))
        freq = read(NFPLUS_MY_MODULE_0_F4_SRCIP()) 
        if(freq<0):
            freq=freq+(2**32) 
        f4_srcip = (f4_srcip * (2**32)) + freq
    print ('SrcIP    F4 = {:<20d}\n'.format(f4_srcip))

    #read dstip f2~f4
    freq = 0
    for j in range(2):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (2-j))
        freq = read(NFPLUS_MY_MODULE_0_F2_DSTIP()) 
        if(freq<0):
            freq=freq+(2**32) 
        f2_dstip = (f2_dstip * (2**32)) + freq
    print ('---  DstIP    F2 = {:<15d}  ---  '.format(f2_dstip),end='')
    freq = 0
    for j in range(3):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (3-j))
        freq = read(NFPLUS_MY_MODULE_0_F3_DSTIP()) 
        if(freq<0):
            freq=freq+(2**32) 
        f3_dstip = (f3_dstip * (2**32)) + freq
    print ('DstIP    F3 = {:<20d}  ---  '.format(f3_dstip),end='')
    freq = 0
    for j in range(4):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (4-j))
        freq = read(NFPLUS_MY_MODULE_0_F4_DSTIP()) 
        if(freq<0):
            freq=freq+(2**32) 
        f4_dstip = (f4_dstip * (2**32)) + freq
    print ('DstIP    F4 = {:<20d}\n'.format(f4_dstip))

    #read SrcPort f2~f4
    freq = 0
    for j in range(2):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (2-j))
        freq = read(NFPLUS_MY_MODULE_0_F2_SRCPORT()) 
        if(freq<0):
            freq=freq+(2**32) 
        f2_srcport = (f2_srcport * (2**32)) + freq
    print ('---  SrcPort  F2 = {:<15d}  ---  '.format(f2_srcport),end='')
    freq = 0
    for j in range(3):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (3-j))
        freq = read(NFPLUS_MY_MODULE_0_F3_SRCPORT()) 
        if(freq<0):
            freq=freq+(2**32) 
        f3_srcport = (f3_srcport * (2**32)) + freq
    print ('SrcPort  F3 = {:<20d}  ---  '.format(f3_srcport),end='')
    freq = 0
    for j in range(4):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (4-j))
        freq = read(NFPLUS_MY_MODULE_0_F4_SRCPORT()) 
        if(freq<0):
            freq=freq+(2**32) 
        f4_srcport = (f4_srcport * (2**32)) + freq
    print ('SrcPort  F4 = {:<20d}\n'.format(f4_srcport))

    #read DstPort f2~f4
    freq = 0
    for j in range(2):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (2-j))
        freq = read(NFPLUS_MY_MODULE_0_F2_DSTPORT()) 
        if(freq<0):
            freq=freq+(2**32) 
        f2_dstport = (f2_dstport * (2**32)) + freq
    print ('---  DstPort  F2 = {:<15d}  ---  '.format(f2_dstport),end='')
    freq = 0
    for j in range(3):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (3-j))
        freq = read(NFPLUS_MY_MODULE_0_F3_DSTPORT()) 
        if(freq<0):
            freq=freq+(2**32) 
        f3_dstport = (f3_dstport * (2**32)) + freq
    print ('DstPort  F3 = {:<20d}  ---  '.format(f3_dstport),end='')
    freq = 0
    for j in range(4):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (4-j))
        freq = read(NFPLUS_MY_MODULE_0_F4_DSTPORT()) 
        if(freq<0):
            freq=freq+(2**32) 
        f4_dstport = (f4_dstport * (2**32)) + freq
    print ('DstPort  F4 = {:<20d}\n'.format(f4_dstport))

    #read Protocol f2~f4
    freq = 0
    for j in range(2):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (2-j))
        freq = read(NFPLUS_MY_MODULE_0_F2_PROTOCOL()) 
        if(freq<0):
            freq=freq+(2**32) 
        f2_protocol = (f2_protocol * (2**32)) + freq
    print ('---  Protocol F2 = {:<15d}  ---  '.format(f2_protocol),end='')
    freq = 0
    for j in range(3):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (3-j))
        freq = read(NFPLUS_MY_MODULE_0_F3_PROTOCOL()) 
        if(freq<0):
            freq=freq+(2**32) 
        f3_protocol = (f3_protocol * (2**32)) + freq
    print ('Protocol F3 = {:<20d}  ---  '.format(f3_protocol),end='')
    freq = 0
    for j in range(4):
        write(NFPLUS_MY_MODULE_0_READ_FREQ_PTR(), (4-j))
        freq = read(NFPLUS_MY_MODULE_0_F4_PROTOCOL()) 
        if(freq<0):
            freq=freq+(2**32) 
        f4_protocol = (f4_protocol * (2**32)) + freq
    print ('Protocol F4 = {:<20d}\n'.format(f4_protocol))
    
    return f2_srcip,f2_dstip,f2_srcport,f2_dstport,f2_protocol,f3_srcip,f3_dstip,f3_srcport,f3_dstport,f3_protocol,f4_srcip,f4_dstip,f4_srcport,f4_dstport,f4_protocol
