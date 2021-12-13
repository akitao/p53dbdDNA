#!/bin/bash

if [ -z "$5" ]
then
   echo Usage: ./$( basename $0 ) try cyc1 cyc2 lb ub
   exit
fi

try=$1
cyc1=$2
cyc2=$3
lb=$4
ub=$5

cd ../try$1

mkdir ana

for i in ` seq ${cyc1} ${cyc2} ` ; do
    mkdir cyc${i}
    cd cyc${i}
    for j in ` seq ${lb} ${ub} ` ; do
	mkdir candi${j}
    done
    cd -
done

cd -
