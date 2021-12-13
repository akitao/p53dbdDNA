#!/misc/home/marzouk/anaconda3/bin/python3
import numpy as np
import glob
import os,sys

if len(sys.argv)==5:
       res= int(sys.argv[1])
       f= int(sys.argv[2])
       FT=int(sys.argv[3])
       LT=int(sys.argv[4])
else: 
        print("please enter number of restart _ frames _ FT _ LT  in that order")
        quit()

data_list=[]
for i in range(FT, LT+1,1):
     data = np.load('/work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext/vector_try{}_3D_{}f.npy'.format(res,i,i,f), allow_pickle=True )
     data_list.extend([data[x] for x in range(len(data))])
np.save('/work2/marzouk/pacsMDrestrain/restart{}/MSM/3D/vector_rest{}_{}f_ext1.npy'.format(res,res,f), data_list)

