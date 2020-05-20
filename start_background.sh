#! /bin/bash

if [[ $# -ne 2 ]]; then
    echo "Usage: sudo ./start_background.sh <current_server> <total_servers>"
    exit 1
fi

socat - TCP-LISTEN:5058,fork &> /dev/null &

sleep 5

cd ~/trafficGenerator
python time_walking.py $1 $2 &

wait
