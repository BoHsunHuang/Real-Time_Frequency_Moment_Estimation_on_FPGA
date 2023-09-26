#import numpy
import time
from reg_defines_reference_nic import *
from param import *

#C + Python
from ctypes import *
import os
dir = os.path.dirname(__file__)
sume = cdll.LoadLibrary(dir+'/libsume.so')

read = sume.regread
write = sume.regwrite

K = K_VALUE()
B_W = BRAM_WIDTH()

for i in range(K):
    table_array = []
    check_array = []
    name = dir+"/table/table"+str(i)+".txt"
    fo = open(str(name), "r")
    for line in fo:
        for value in line.split():
            table_array.append(int(value))
    while(len(table_array)!=B_W):
        table_array.append(int(0))
    #write value in
    write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xAAAA0002+i*0x0100))
    for table_value in table_array:
        write(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), table_value)
    #read value    
    write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xBBBB0002+i*0x0100))
    for j in range(B_W):
        read_value = read(NFPLUS_MY_MODULE_0_TABLE_VALUE_R())
        if read_value < 0:
            read_value = read_value+2**32         
        check_array.append(read_value)
    err = 0
    for j in range(B_W):
        if(table_array[j]!=check_array[j]):
            print('in = {:d} out = {:d}'.format(table_array[j],check_array[j]))
            err = 1
            break

    if(err==1):
        print('write table{:d} fail'.format(i))

print ('###############################')
print (' Entropy Table write complete!')
print ('###############################\n')


