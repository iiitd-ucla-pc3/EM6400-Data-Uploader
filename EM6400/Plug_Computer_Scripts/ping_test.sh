#!/bin/sh

NUMBER_OF_PING_REQUESTS=4
ROUTER_ADDRESS="192.168.0.1"
SLEEP_TIME=900



while true
do
	
	PACKETS_RECEIVED=`ping -c $NUMBER_OF_PING_REQUESTS $ROUTER_ADDRESS | grep "received" | awk '{print $4}'`
	if [ $PACKETS_RECEIVED -eq 0 ] 
	then 
		iwconfig mlan0 essid "NETGEAR"
		dhclient mlan0
		
	else 
		echo "ping Working"
	
	fi
	#Killing existing Dropbox Upload Scripts
	sh killproc.sh

	#Now invoking Python Dropbox upload script
	python /root/EM6400-Data-Uploader/EM6400/dropbox_upload.py & 
	
	sleep $SLEEP_TIME
done