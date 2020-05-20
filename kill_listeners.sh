#! /bin/bash

ssh -p 26011 nofelY94@c220g2-010823.wisc.cloudlab.us "sudo killall socat; sudo killall start_background; sudo killall python"
ssh -p 26012 nofelY94@c220g2-010823.wisc.cloudlab.us "sudo killall socat; sudo killall start_background; sudo killall python"
