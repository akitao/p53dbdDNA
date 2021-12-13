#!/misc/home/marzouk/anaconda3/bin/python3
import os
import sys
import time
from glob import glob
import pickle as pickle
import numpy as np
import fnmatch
import mdtraj as md
import itertools
import glob
#plots
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
#PyEMMA
import pyemma
import pyemma.coordinates as coor
import pyemma.msm as msm
from msmtools import dtraj
import pyemma.plots as mplt
from pyemma.util.contexts import settings

f=$1
n=$2    #the number of try to do cluster by kmeans because it is changing from one time to another

data = np.load('/save/users/bps/1TSRB2/pacsMDrestrain/MSM_3D/inputdata/vector_alldata_{}f_ext.npy'.format(f), allow_pickle=True )
data=data.tolist()


for clus in [500,1000,1500]:
    cluster = pyemma.coordinates.cluster_kmeans(data,k=clus,max_iter=500,n_jobs=10,stride=2,init_strategy='kmeans++')
    dtraj=cluster.dtrajs
    cluster.save('/save/users/bps/1TSRB2/pacsMDrestrain/MSM_results/3Dext/{}f/clustering/{}clus/nclus{}_{}f_clustering_no{}.h5'.format(f,clus,clus,f,n))
    np.save("/save/users/bps/1TSRB2/pacsMDrestrain/MSM_results/3Dext/{}f/clustering/{}clus/nclus{}_{}f_centers_no{}.npy".format(f,clus,clus,f,n),cluster.clustercenters)
    np.save("/save/users/bps/1TSRB2/pacsMDrestrain/MSM_results/3Dext/{}f/clustering/{}clus/nclus{}_{}f_dtrajs_no{}.npy".format(f,clus,clus,f,n),np.array(dtraj))
    pickle.dump(np.array(dtraj),open("/save/users/bps/1TSRB2/pacsMDrestrain/MSM_results/3Dext/{}f/clustering/{}clus/nclus{}_{}f_dtrajs_no{}.pkl".format(f,clus,clus,f,n),"wb"), protocol=2)



