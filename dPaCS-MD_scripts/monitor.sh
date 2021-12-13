#!/bin/bash

if [ -z "$2" ]
then
   echo :Usage ./$( basename $0 ) second cyc
   exit
fi

sec=$1
cyc=$2
 
lc=`jobinfo -c -l -q PN | grep cyc${cyc} | wc -l`

echo waiting for Cycle ${cyc} finish...

i=0
while [ ${lc} -ne 0  ] ; do
  i=$((i+1))
  sleep ${sec}
  lc=`jobinfo -c -l -q PN | grep cyc${cyc} | wc -l`
  echo Waited for $i times
done

echo Cycle ${cyc} finished.

exit 0
