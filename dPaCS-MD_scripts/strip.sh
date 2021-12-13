#!/bin/bash                                                                     
if [ $# -ne 4 ]; then
  echo "Usage: select.sh [try #] [cyc #] [lb] [ub] " 1>&2
  exit 1
fi

try=try$1
cyc=cyc$2
cycp=cyc$(($2-1))
lb=$3
ub=$4

COMMAND=$(cd $(dirname $0) && pwd)
PRE=${COMMAND}/../pre

cat <<EOF > strip.in
parm ${PRE}/1TSRB_ZAFF2.prmtop
trajin md.mdcrd
strip :WAT outprefix wow
trajout wow.mdcrd
run
EOF

export AMBERHOME="/local/apl/lx/amber16-bf10/"
export PATH="${AMBERHOME}/bin:${PATH}"

for i in `seq ${lb} ${ub} ` ; do
    cd ${COMMAND}/../${try}/${cycp}/candi${i}
    cpptraj.MPI -i ${COMMAND}/strip.in
    rm md.mdcrd
done

