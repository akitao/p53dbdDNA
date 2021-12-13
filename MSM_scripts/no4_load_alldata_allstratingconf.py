#!/misc/home/marzouk/anaconda3/bin/python3
import numpy as np
import glob
import os,sys

if len(sys.argv)==4:
       Fres=int(sys.argv[1])
       Lres=int(sys.argv[2])
       f= int(sys.argv[3])
else: 
        print("please enter number of Frestart _ Lrestart _ frames  in that order")
        quit()

data_list=[]
for i in range(Fres, Lres+1,1):
     data = np.load('/work2/marzouk/pacsMDrestrain/restart{}/MSM/3D/vector_rest{}_{}f_ext.npy'.format(i,i,f), allow_pickle=True )
     data_list.extend([data[x] for x in range(len(data))])
np.save('/work2/marzouk/pacsMDrestrain/MSMresult/3Dext/inputdata/vector_alldata_{}f_ext.npy'.format(f), data_list)

