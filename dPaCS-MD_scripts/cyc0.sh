#!/bin/bash

if [ -z "$1" ]
then
   echo :Usage ./$( basename $0 ) id
   exit 1
fi

id=$1

export AMBERHOME="/local/apl/lx/amber16-bf10/"
export PATH="${AMBERHOME}/bin:${PATH}"

command=$(cd $(dirname $0) && pwd)
pre=${command}/../pre

mkdir ../try${id}
mkdir ../try${id}/cyc0/
cd ../try${id}/cyc0

cat <<EOF > try${id}.in
Production
&cntrl
  imin=0,ntx=1,irest=0,
  nstlim=50000,dt=0.002,
  ntpr=100,ntwx=20,
  cut=12.0,
  ntf=2,ntc=2,
  temp0=300.0,ntt=3,taup=1.0,gamma_ln=2.0,ig=-1,
  ntp=1,ntb=2,pres0=1000.0,iwrap=1,ntr=1,
restraint_wt=1.0
restraintmask=':200,201,202,203,220,219,217,218,221,222,223,224,241,240,239,238&!@H='/
END
EOF

cat <<EOF > try${id}.cyc0.job
#!/bin/csh -f 
#PBS -l select=1:ncpus=6:mpiprocs=1:ompthreads=1:jobtype=gpu:ngpus=1
#PBS -l walltime=00:40:00
cd ${PWD}

setenv AMBERHOME "/local/apl/lx/amber16-bf10/"
setenv PATH "${AMBERHOME}/bin:${PATH}"
setenv LD_LIBRARY_PATH "/usr/local/cuda-8.0/lib64:${LD_LIBRARY_PATH}"


pmemd.cuda -O \
    -i   try${id}.in \
    -o   md.out \
    -p   ${pre}/1TSRB_ZAFF2.prmtop \
    -c   ${pre}/04_Prod7.ncrst \
    -x   md.mdcrd \
    -r   md.rst \
    -ref ${pre}/04_Prod7.ncrst  < /dev/null
EOF

jsub -q PN try${id}.cyc0.job

cd -

exit 0
