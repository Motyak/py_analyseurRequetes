#!/bin/sh

# Create directories
mkdir -p bin lib

# Download ice lib
[ ! -f lib/ice-3.7.2.jar ] &&
wget https://search.maven.org/remotecontent?filepath=com/zeroc/ice/3.7.2/ice-3.7.2.jar -O lib/ice-3.7.2.jar

# Compile slice
slice2java generatedIce.ice &&

# Compile generatedIce source
javac generatedIce/*.java -cp lib/ice-3.7.2.jar -d bin &&

# Compile client (BackendApi)
javac BackendApi.java -cp lib/ice-3.7.2.jar:bin -d bin
