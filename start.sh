if [ -z "$(ls /run/screen/S-pi/)" ]; then
    screen -d -m Xvfb :100
fi

#if ! screen -list | grep -q "raspberrypi"; then
#    screen -d -m Xvfb :100
#fi
export DISPLAY=:100.0
python3 run.py
