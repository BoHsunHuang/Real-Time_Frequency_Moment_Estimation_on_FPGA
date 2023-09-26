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




for i in range(7):
    for j in range(2):
        arr_ams=[]
        for k in range(2):
            arr_ams.append(random.randint(0,0xFFFFFFFF))
            #arr_ams.append(0x0)
            #arr_ams.append(1-k)

        write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xAAAA1500+i*0x0100+j)) 
        for k in range(2):                              
            write(NFPLUS_MY_MODULE_0_TABLE_VALUE_W(), arr_ams[k])
        write(NFPLUS_MY_MODULE_0_TABLE_ID(), (0xBBBB1500+i*0x0100+j))
        for k in range(2):      
            check = read(NFPLUS_MY_MODULE_0_TABLE_VALUE_R())
            if(check<0):
                check = check+2**32
            if(check != arr_ams[k]):

                print ('Oops ! write wrong in ams module')
                print('param = {:d}'.format(arr_ams[k]))
                print('check = {:d}'.format(check))


print ('##########################')
print (' AMS Hash write complete!')
print ('##########################\n')

