import time
import random
from reg_defines_reference_nic import *
from param import *

#C + Python
from ctypes import *
import os
dir = os.path.dirname(__file__)
sume = cdll.LoadLibrary(dir+'/libsume.so')

read = sume.regread
write = sume.regwrite



arr_pcsa = [[0] for i in range(32)]

                

write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xAAAA1400))
for k in range(32):
        arr_pcsa[k] = random.randint(0,134217727)
for k in range(32):                              
    write(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), arr_pcsa[k])
write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xBBBB1400))
for k in range(32):      
    check = read(NFPLUS_MY_MODULE_0_TABLE_VALUE_R())
    #print('param = {:d}'.format(arr_pcsa[k]))
    #print('check = {:d}'.format(check))
    if(check != arr_pcsa[k]):
        print ('Ahhh ! write wrong in entropy module')

#for i in range(K):
#    nftest_regwrite(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xAAAA1502+i*256))
#    for i in range(1000):
#        nftest_regwrite(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), value)
#        value = value+1
#    value = 0     
#    for i in range(1000):
#        nftest_regwrite(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), value)
#        value = value+1

print ('###########################')
print (' PCSA Hash write complete!')
print ('###########################\n')

