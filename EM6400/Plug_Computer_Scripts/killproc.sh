#!/bin/sh

ps aux | grep dropbox | grep -v grep | tr -s " " | cut -d" " -f2 > sample.txt
while read line
do
kill -9 $line
done < sample.txt
