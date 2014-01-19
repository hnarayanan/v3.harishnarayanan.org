#!/bin/sh

for i in $( ls ../moments/*.jpg ); do
    ln -s $i `basename $i`
done
