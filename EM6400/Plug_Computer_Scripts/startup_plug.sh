#!/bin/sh


<<'Instructions'
Run the following commands for creating startup scripts
1.vi /etc/init.d/startup_plug.sh
Copy the contents of this file
2.chmod +x /etc/init.d/startup_plugs.sh
3.update-rc.d startup_plug defaults
Instructions

ifconfig eth0 down
/root/setup/init_wlan
iwconfig mlan0 essid "NETGEAR"
dhclient mlan0

sleep 30
python ../data_collect_csv_realtime_plot.py & > /root/log_data_collect.txt
sleep 5
python ../dropbox_upload.py & > /root/log_dropbox_upload.txt

