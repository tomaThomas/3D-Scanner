#!/bin/bash
cd /home/pi/3D-Scanner
python3 run.py 2> web-interface/error.txt > web-interface/log.txt &
exit $?
