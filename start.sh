#!/bin/sh
ls -la
cd src
la -la
python main.py &
python pubSJC.py &
python pubTBT.py &
python pubJAC.py &
wait