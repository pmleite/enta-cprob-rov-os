#!/bin/bash
clear 

echo updating...
git pull

echo running rovOS
lxterminal --title="ROV_OS" -e python3 /home/pi/enta-cprob-rov-os/rovOS.py
echo done

echo runnig videoStreaming
lxterminal --title="ROV_VIDEO_STREAM" -e pyhton3 /home/pi/enta-cprob-rov-os/videoStream.py 




