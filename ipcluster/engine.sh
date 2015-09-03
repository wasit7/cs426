#!/bin/bash
screen -ls | grep ipe | cut -d. -f1 | awk '{print $1}' | xargs kill
screen -S ipe -d -m ipcluster engines


#UDIR=/home/*
#for d in $UDIR
#do
#  echo "--> $d"
#done
