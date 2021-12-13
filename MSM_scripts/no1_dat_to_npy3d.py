#!/misc/home/marzouk/anaconda3/bin/python3
import os,sys, shutil, glob
import numpy as np

if len(sys.argv)==4:
       res= int(sys.argv[1])
       t= int(sys.argv[2])
       cyc=int(sys.argv[3])
else:
        print("please enter number of restart  _ try _ last cycle  in that order")
        quit()


LOC = '/work2/marzouk/pacsMDrestrain/restart{}/try{}/try{}_vector_5A_500f_ext/'.format(res,t,t)
NewLoc = '/work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext/try{}_3dData_npy_250f'.format(res,t,t)

if not(os.path.exists("/work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext".format(res,t))):
    print ("MSM_3Dext directory does not exist. Try to create one!")
    os.system("mkdir /work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext".format(res,t))

if os.path.exists(NewLoc) == True:
        shutil.rmtree(NewLoc)
os.mkdir(NewLoc)
os.chdir(NewLoc)
for i in range(0, cyc+1):
        for j in range(1, 11):
            filename= str(LOC)+"cyc"+str(i)+"cd"+str(j)+".dat"
            if (not os.path.exists(filename)):
                continue
            f=np.loadtxt(filename)
            if (max(f[:,7]) <= 65):
                    fb=np.loadtxt(filename)[range(0,500,2), 1:4]
                    np.save('/work2/marzouk/pacsMDrestrain/restart{}/try{}/MSM_3Dext/try{}_3dData_npy_250f/cyc{}cd{}.npy'.format(res,t,t,i,j),fb)