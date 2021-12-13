#---------------------------------
#dPaCS-MD using AMBER package  
#Date created : 11/12/2021
#This file to explain the using of all scripts required to run dPaCS-MD
# For MD simulation we used AMBER16 package 
# for distance calculations for structure ranking after every cycle, we used  cpptraj module of the Amber Tools 16 package
#---------------------------------------------------------------------
We have total 9 files cyc0.sh, cyc.sh, main.sh, make_dir.sh, monitor.sh, 
rst.sh, select.sh, select0.sh, strip.sh 
We will explain here the main role of each one of them in the dPaCS-MD 
1- main.sh 
The main file required to control the running of the dPaCS-MD process and 
you can specify important parameters like;
- the number of replica : 10 in our case 
- the threshold of Inter-COM distance ,d, in our case d=70 A 
#---------------------------------------------------------------------
Then to run the preliminary cycle in dPaCS-MD  we use two files no. 2 & 3 
2-cyc0.sh
The inputs required for this preliminary cycle is the output of the extended box
 a- Certain starting conformation's restart file    #  in directory called five_starting_conformotions
 b- AMBER topology file of the extend box system  # in directory nput_files_extendedbox
 In this cycle we run short MD simulation 0.1 ns 

3-select0.sh
Using the distance function of AMBER Tools we can calculate d for the output snapshots of cyc0 
based on the selection criteria 
Then rank snapshots and choose the highest 10 for the next cycle. 

#---------------------------------------------------------------------
4-cyc.sh
In this cycle we run short MD simulation 0.1 ns  for the 10 replica chosen from the previous cycle 


5-select.sh
calculate d for all replica (10) then Rank them then take the highest 10 for the next cycle 

#----------------------------------------------------------------------------
During the running of dPaCS-MD we need to do some of similar steps when go from one cycle to another such as 
6- make_dir.sh
Make the required directory based on the number of replica   
 
7-monitor.sh 
Show notifications sentences on the monitor to let us know where the process are regularly 

8-strip.sh
To remove the water from the output trajectories each cycles, for avoid storage problems 
#----------------------------------------------------------------------------

9-rst.sh
Just in case, if for any reason the dPaCS-MD process disconnected at certain cycle number
then you can restart the dPaCS-MD for this specific cycle using this file code. 
This code contains the same regulations like the main.sh file 
number of replica : 10 in our case 
d = 70 Angstrom 



