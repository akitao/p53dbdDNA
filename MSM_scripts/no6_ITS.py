#!/misc/home/marzouk/anaconda3/bin/python3
import os,sys,glob
import numpy as np
import matplotlib.pyplot as plt
import pyemma
import pyemma.msm as msm
from msmtools import dtraj
import pyemma.plots as mplt
import matplotlib as mpl
if len(sys.argv)==4:
       clus= int(sys.argv[1])
       ni= int(sys.argv[2])    # first cluster trial number 
       nf= int(sys.argv[3])    # last cluster trial number 
else:
        print("please enter number of clus _  firstClusterTrail _lastClusterTrial in that order")
        quit()
f = 250
path="/work2/marzouk/pacsMDrestrain/MSMresult/3Dext/{}f/".format(f,clus)
for n in range (ni,nf+1):
        cluster=pyemma.load(path+'clustering/{}clus/nclus{}_{}f_clustering_no{}.h5'.format(clus,clus,f,n))
        dtrajs=cluster.dtrajs
        center=cluster.clustercenters
        its = pyemma.msm.its(dtrajs, lags= [1,2,3,4,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,100,110,115,120,125] , nits=20, n_jobs=10)
        #ltits=np.append(np.array([its.lagtimes]).T, its.timescales, axis=1)
        #np.savetxt(path+"ITS/its_nclus{}_{}f_no{}.txt".format(clus,f,n),ltits)
        mpl.rcParams["font.family"]="serif"
        fig, axes = plt.subplots(figsize=(12,8))
        axes = pyemma.plots.plot_implied_timescales(its, units='ps', dt=0.4,linewidth=2)
        axes.set_xlabel("Lag Time (ps)", fontsize=24, color='black')
        axes.set_ylabel('TimeScale (ps)', fontsize=24, color='black')
        plt.rc('xtick', labelsize= 18)
        plt.rc('ytick', labelsize= 18)
        axes.set_title("{} clusters  {} frames no {}".format(clus,f,n) , fontsize=24, color='black')
        for axis in ['top', 'bottom','left','right']:
                axes.spines[axis].set_linewidth(2)
        fig.savefig(path+"ITS/its_nclus{}_{}f_no{}.png".format(clus,f,n), dpi=1000)