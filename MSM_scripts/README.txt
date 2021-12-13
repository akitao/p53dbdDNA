#---------------------------------
#dPaCS-MD using AMBER package  
#Date created : 13/12/2021
#This file to use PyEMMA package to build 3D-MSM using;
- PyEMMA Package 2.5.7
- Python 3.7.4
- Cpptraj of Amber Tools 16 package : to calculate the 3D vector coordinates between interface residues of p53-DBD and DNA 
#---------------------------------------------------------------------

1- no1_dat_to_npy3d.py 
To convert the 3D input data files of trajectories to numpy python files 

Then we can collect all the data by using the following script files 

2-no2_load_data_dPaCS-MD_trial.py
To collect the 3D data from all cycles of one  dPaCS-MD_trial

3-no3_load_data_startingConf.py
To collect the 3D data from all trials (15 in our case) of of each one of the starting conformation 

4-no4_load_alldata_allstratingconf.py 
To collect all the data from all the starting conformations ( 5 in our case)

Then to build MSM we have to do clustering for the input data with K-means using this script 
5-no5_clustering.py

To check the MS model and the prober time scale we have to plot the relation between lag time and implied time scale using this script 
6- no6_ITS.py

Finally we can build MSM and plot the FEL using one of these scripts
no7_FEL_XY.py
no8_FEL_YZ.py
no9_FEL_XZ.py
