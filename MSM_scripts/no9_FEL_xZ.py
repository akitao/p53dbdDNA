#!/misc/home/marzouk/anaconda3/bin/python3
import os,sys,glob
import numpy as np
import fnmatch
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib as mpl
#PyEMMA
import pyemma
import pyemma.msm as msm
from msmtools import dtraj
import pyemma.plots as mplt
from scipy.interpolate import griddata
if len(sys.argv)==3:
       clus= int(sys.argv[1])
       n= int(sys.argv[2])
else: 
        print("please enter number of  clus _ trail number  in that order")
        quit()
f=250  #if u want to change 500 change dt too to 0.2

#General requirements
kB=1.9872066124357268*1e-3    # kcal/mol
T=300.0                       # K
beta=1.0/(kB*T)               # mol/kcal
path="/work2/marzouk/pacsMDrestrain/MSMresult/3Dext/{}f/".format(f,clus)

#load clustering
cluster=pyemma.load(path+'clustering/{}clus/nclus{}_{}f_clustering_no{}.h5'.format(clus,clus,f,n))
dtrajs=cluster.dtrajs
center=cluster.clustercenters
#msm


d=center[:, 2:3]
b=center[:, 0:1]
mm=[]
for i in range(len(b)):
    mm.append(i)


lt=50
msm = pyemma.msm.estimate_markov_model(dtrajs, lag=lt, dt_traj='0.4 ps')
lcc = msm.active_set
centers_lcc =cluster.clustercenters[lcc, :]
transprob=msm.stationary_distribution
A =-1.0/beta*np.log(transprob)
A -= A.max()
#mesh grid
nx, ny, nz = 500, 500, 500
x = np.linspace(np.min(centers_lcc[:,0]), np.max(centers_lcc[:,0]), nx)
y = np.linspace(np.min(centers_lcc[:,1]), np.max(centers_lcc[:,1]), ny)
z = np.linspace(np.min(centers_lcc[:,2]), np.max(centers_lcc[:,2]), nz)
X, Z = np.meshgrid(x, z)
AXZ = griddata(centers_lcc[:,[0,2]], np.array(A), (X, Z), method='linear')
# plot the FEL
mpl.rcParams["font.family"]="serif"
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
CS = ax.contourf(X, Z, AXZ, levels=800, origin="upper", cmap=plt.cm.RdYlGn, alpha=1.0)
cbar = plt.colorbar(CS, ticks=[0.0, -1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0,-8.0,-9.0,-10.0])
cbar.ax.set_ylabel('Free Energy (kcal/mol)', fontsize=24)
cbar.ax.set_yticklabels(["0.0", "-1.0", "-2.0", "-3.0", "-4.0", "-5.0", "-6.0", "-7.0","-8.0","-9.0","-10.0"], fontsize=20)
plt.xlabel("X ($\AA$)" , fontsize=24)
plt.ylabel("Z ($\AA$)", fontsize=24)
plt.rc('xtick', labelsize= 16)
plt.rc('ytick', labelsize= 16)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.tick_params(axis='both', labelsize=16, direction="in", length=9, right=True, left=True, top=True, bottom=True, which="minor")
fig.savefig(path+"MSM/FEL_XZ_nclus{}_{}f_no{}_lag{}_Nopathways_DecNo1.png".format(clus,f,n,lt))




