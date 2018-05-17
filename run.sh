#!/bin/bash
cd /home/pi/3D-Scanner
stdbuf -oL -eL python3 run.py 2> web-interface/error.txt > web-interface/log.txt &
