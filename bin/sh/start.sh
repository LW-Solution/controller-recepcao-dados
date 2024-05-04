#!/bin/sh
cd src
python main.py &
python pubSJC.py &
python pubTBT.py &
python pubJAC.py &
wait