#!/bin/sh

NUMBER_OF_PING_REQUESTS=4
ROUTER_ADDRESS="192.168.0.1"
SLEEP_TIME=300



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
	sleep $SLEEP_TIME
done