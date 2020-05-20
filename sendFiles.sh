#! /bin/bash

echo "Sending start_background"

scp -P 26011 start_background.sh nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/
scp -P 26012 start_background.sh nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/

echo "Sending traffic_X.txt"

scp -P 26011 traffic_0.txt nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/
scp -P 26012 traffic_1.txt nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/


echo "Sending time_walking"

scp -P 26011 time_walking.py nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/
scp -P 26012 time_walking.py nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/

echo "Sending time_walking"

scp -P 26011 TimeEvent.py nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/
scp -P 26012 TimeEvent.py nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/

echo "Sending servers.json"

scp -P 26011 servers.json nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/
scp -P 26012 servers.json nofelY94@c220g2-010823.wisc.cloudlab.us:./trafficGenerator/