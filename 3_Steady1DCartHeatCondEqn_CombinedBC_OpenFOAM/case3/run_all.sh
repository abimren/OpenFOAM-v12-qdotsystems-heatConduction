#!/bin/bash

foamCleanCase

rm -r 0
cp -r 0_orig 0

blockMesh | tee log.blockMesh

laplacianFoam | tee log.laplacianFoam

foamPostProcess -func sample -latestTime

cd plots
python plot_OF_vs_analytical.py

