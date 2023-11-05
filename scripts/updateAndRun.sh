#!/bin/bash
clear 

echo updating...
git pull

echo running rovOS
lxterminal -e pyhton3 rovOS.py

echo runnig videoStreaming
lxterminal -e pyhton3 videoStream.py 


