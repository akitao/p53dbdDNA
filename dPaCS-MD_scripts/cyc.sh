#!/bin/bash

if [ -z "$4" ]
then
   echo :Usage ./$( basename $0 ) try cyc lb ub
   exit
fi

try=try$1
cyc=$2
lb=$3
ub=$4

COMMAND=$(cd $(dirname $0) && pwd)
LOC1=$COMMAND/../
PRE=$COMMAND/../pre

export AMBERHOME="/local/apl/lx/amber16-bf10/"
export PATH="${AMBERHOME}/bin:${PATH}"

cat <<EOF > cyc.in
Production
&cntrl
  imin=0,ntx=1,irest=0,
  nstlim=50000,dt=0.002,
  ntf=2,ntc=2,
  temp0=300.0,ntt=3,gamma_ln=2.0,ig=-1,
  ntpr=100,ntwx=20,
  cut=12.0,
  ntb=2,ntp=1,pres0=1000.0,iwrap=1,ntr=1,
restraint_wt=1.0
restraintmask=':200,201,202,203,220,219,217,218,221,222,223,224,241,240,239,238&!@H='/
END
EOF

cd $LOC1/${try}/cyc${cyc}/
for i in ` seq ${lb} ${ub} ` ; do
    cd candi${i}
    loc=$(cd $(dirname $0) && pwd)

    cat <<EOF > cyc${cyc}.cd${i}.job
#!/bin/csh -f
#PBS -l select=1:ncpus=6:mpiprocs=1:ompthreads=1:jobtype=gpu:ngpus=1
#PBS -l walltime=00:40:00
cd ${PWD}

setenv AMBERHOME "/local/apl/lx/amber16-bf10/"
setenv PATH "${AMBERHOME}/bin:${PATH}"
setenv LD_LIBRARY_PATH "/usr/local/cuda-8.0/lib64:${LD_LIBRARY_PATH}"

pmemd.cuda -O \
    -i   ${COMMAND}/cyc.in \
    -o   $loc/md.out \
    -inf $loc/md.inf \
    -p   $PRE/1TSRB_ZAFF2.prmtop \
    -c   $loc/cyc${cyc}_cd${i}.rst7 \
    -x   $loc/md.mdcrd \
    -r   $loc/md.rst \
    -ref ${PRE}/04_Prod7.ncrst  < /dev/null
EOF

    cd ..
done


cd ${COMMAND}
for i in ` seq ${lb} ${ub} ` ; do
    cd $LOC1/${try}/cyc${cyc}/candi${i}

    jsub -q PN cyc${cyc}.cd${i}.job
done

exit 0
