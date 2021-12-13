#!/bin/bash

if [ -z "$1" ]
then
   echo :Usage ./$( basename $0 ) [try]
   exit 1
fi

cyc=1
lb=1
ub=10
try=$1

./cyc0.sh ${try}

sleep 30
echo waiting for job ends try$try cyc0.
./monitor.sh 30 0

echo making the next cycle directories.
./make_dir.sh $try $cyc $((cyc+1)) $lb $ub

echo selecting coordinates for the next cycle.
./select0.sh $try $cyc $lb $ub


#for i in `seq 1 100`; do
i=0; com=0;
while [ $com -lt 70 -a $i -lt 150 ]; do
    i=$((i+1))
    echo submitting md for try$try cyc$i
    ./cyc.sh $try $i $lb $ub
    ./strip.sh $try $i $lb $ub
    sleep 30

    echo waiting for job ends try$try cyc$i
    ./monitor.sh 30 $i

    echo making the next directory tree.
    ./make_dir.sh $try $((i+1)) $((i+1)) $lb $ub

    echo selecting initial coordinates for try$try cyc$((i+1))
    ./select.sh $try $i $lb $ub

    for j in 1; do
	read line
	a=($line)
	com=${a[2]}
	com=${com/.*}
    done < ../try$try/ana/cyc$i
done

exit 0
