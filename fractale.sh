#!/bin/sh

current_directory=`pwd`
destination=$current_directory/$2
mkdir $destination
mv $1 $destination
