#!/bin/bash

#echo "Enter the number of nodes to use:"
#read nNodes

#echo "Enter the number of CPUs per node:"
#read nCPUs

#echo "Enter the number of runs for averaging:"
#read nRuns

#echo "Enter start of output filename:"
#read fname

#clear 

while read -r a b c d; do
	nNodes=$a
	nCPUs=$b
	nRuns=$c
	fname=$d

	DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
	x=$DIR
	savupath=${x%/bin}

	runfile=/bin/savu_launcher.sh
	datafile=/test_data/24737.nxs
	processfile=/test_data/process01.nxs
	outpath=$PWD #outputting to the current folder
	outname="${fname}N${nNodes}_C${nCPUs}_mpi_test"

	for i in $(eval echo {1..$nRuns})
  		do
   		 $savupath$runfile $savupath $datafile $processfile $outpath $outname $nNodes $nCPUs
	done

	python $savupath/scripts/log_evaluation/GraphicalThreadProfiler_multi.py "$outpath/"log_${outname}*""

done < ../input_params.txt
