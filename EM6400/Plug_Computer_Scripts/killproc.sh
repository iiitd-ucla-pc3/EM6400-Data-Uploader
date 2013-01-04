#!/bin/sh

ps aux | grep dropbox | grep -v grep | tr -s " " | cut -d" " -f2 > /root/sample.txt
while read line
do
kill -9 $line
done < /root/sample.txt
