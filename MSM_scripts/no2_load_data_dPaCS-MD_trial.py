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
        print("please enter number of restart _ frames _ FT  _ LT in that order")
        quit()

for i in range(FT, LT+1,1):
    traj_list = glob.glob('/work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext/try{}_3dData_npy_{}f/cyc*cd*.npy'.format(res,i,i,f))   #.format(i,i))
    vector_reader=[]
    for name in traj_list:
        if (not os.path.exists(name)):
            print(name)
            continue
        else:
            inp = np.load(name)
            vector_reader.append(inp)
    np.save('/work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext/vector_try{}_3D_{}f.npy'.format(res,i,i,f), vector_reader)
