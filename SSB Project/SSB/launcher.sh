#!/bin/sh
# launcher.sh
# navigate to home, ssb, execute ssb, home

cd /
cd home/pi/python_games/SSB
sudo python ssb.py & sudo python keyboard.py
cd / 
