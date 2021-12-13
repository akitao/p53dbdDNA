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
LOC=${COMMAND}/../${try}/cyc0/
PRE=${COMMAND}/../pre
TMPLIST=~/tmp/tmplist$1
LIST=${COMMAND}/../${try}/ana/${cyc}

export AMBERHOME="/local/apl/lx/amber16-bf10/"
export PATH="${AMBERHOME}/bin:${PATH}"


cat <<EOF > select.in
parm ${PRE}/1TSRB_ZAFF2.prmtop
trajin ${LOC}/md.mdcrd 1 last 25
distance com :28,29,72,73,74,75,148,149,155,156,157,181,185,188,189,191,193 :210,211,212,213,224,225,226,231,232,233,234,235  out ${LOC}/select.dat
run
EOF

cpptraj.MPI -i select.in

cat ${LOC}/select.dat | awk '{printf "'${COMMAND}/../' ''%s %s %s\n",$1,$2,$3}'>>$TMPLIST
#done

echo Sorting selection data
cat $TMPLIST | sort -nr -k 3 | head -$4 >$LIST
echo Generating inpcrd files

i=0
while read line; do
    traj=`echo $line | cut -d ' ' -f 1`
    numb=`echo $line | cut -d ' ' -f 2`
    i=$((i+1))
    echo $traj $numb $i

cat << eof1 > make_rst.in
parm ${PRE}/1TSRB_ZAFF2.prmtop
trajin ${LOC}/md.mdcrd 1 last 25
trajout ${COMMAND}/../${try}/${cyc}/candi$i/cyc$2_cd$i.rst7 onlyframes $numb
run
eof1

cd ${COMMAND}/../${try}/${cyc}/candi$i/
cpptraj.MPI -i ${COMMAND}/make_rst.in
cd -
done < $LIST

rm $TMPLIST
