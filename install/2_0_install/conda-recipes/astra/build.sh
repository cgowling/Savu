#!/bin/bash

nvcc=`command -v nvcc`
cuda=${nvcc%/bin/nvcc}

ana_path=`command -v savu`
prefix=${ana_path%/bin/savu}/lib/python2.7/site-packages/astra

cd build/linux

if [ "$cuda" ]; then
    ./configure --with-cuda=$cuda --with-python --prefix=$prefix
else
    echo "cuda has not been found."
    ./configure --with-python --prefix=$prefix
fi

make -j 4
make install

