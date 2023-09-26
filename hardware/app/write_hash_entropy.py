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

K=K_VALUE()

arr_entropy=[[0] for i in range(4)]

for i in range(K):
    for j in range(2):
        for k in range(4):
            arr_entropy[k] = random.randint(0,0xFFFFFFFF)
        write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xAAAA0000+i*0x0100+j)) 
        for k in range(4):                              
            write(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), arr_entropy[k])
        write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xBBBB0000+i*0x0100+j))
        for k in range(4):      
            check = read(NFPLUS_MY_MODULE_0_TABLE_VALUE_R())
            if(check<0):
                check = check+2**32
            if(check != arr_entropy[k]):
                print ('Ahhh ! write wrong in entropy module')
                print('param = {:d}'.format(arr_entropy[k]))
                print('check = {:d}'.format(check))

#arr_entropy[0] = 0
#arr_entropy[1] = 2
#arr_entropy[2] = 0
#arr_entropy[3] = 2
#
#for i in range(K):
#    for j in range(2):
#        write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xAAAA0000+i*0x0100+j)) 
#        for k in range(4):                              
#            write(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), arr_entropy[k])
#        write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xBBBB0000+i*0x0100+j))
#        for k in range(4):      
#            check = read(NFPLUS_MY_MODULE_0_TABLE_VALUE_R())
#            if(check != arr_entropy[k]):
#                print ('Ahhh ! write wrong in entropy module')
#                print('param = {:d}'.format(arr_entropy[k]))
#                print('check = {:d}'.format(check))


print ('##############################')
print (' Entropy Hash write complete!')
print ('##############################\n')

