#! /bin/bash

ssh -f -p 26011 nofelY94@c220g2-010823.wisc.cloudlab.us "cd trafficGenerator; sudo nohup ./start_background.sh 0 2 </dev/null >/dev/null 2>&1 &"
ssh -f -p 26012 nofelY94@c220g2-010823.wisc.cloudlab.us "cd trafficGenerator; sudo nohup ./start_background.sh 1 2 </dev/null >/dev/null 2>&1 &"
