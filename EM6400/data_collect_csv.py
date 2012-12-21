from ctypes import *
import datetime
import minimalmodbus
import os
import pytz
import struct
import time

data_base_path="/home/nipun/Desktop/data/"

threshold_time=900
def convert(s):
	return struct.unpack("<f",struct.pack("<I",s))[0]
    

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 19200   # Baud

start_time=int(time.time())
now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
start_day=now.day
start_month=now.month
print start_day
print start_month
if not os.path.exists(data_base_path+str(start_day)+"_"+str(start_month)):
		os.makedirs(data_base_path+str(start_day)+"_"+str(start_month))
f=open(data_base_path+str(start_day)+"_"+str(start_month)+"/0.csv","wa")
count=0

while True:
	now_time=int(time.time())
	now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
	now_day=now.day
	now_month=now.month
	
	
	if ((now_time-start_time) > threshold_time) or (now_day>start_day):
		if now_day>start_day:
			count=-1
		count=count+1
		start_time=now_time
		start_day=now_day
		start_month=now_month
		f.close()
		if not os.path.exists(data_base_path+str(start_day)+"_"+str(start_month)):
			os.makedirs(data_base_path+str(start_day)+"_"+str(start_month))
		f=open(data_base_path+str(start_day)+"_"+str(start_month)+"/"+str(count)+".csv","wa")

	else:
		try:
			readings_array = instrument.read_registers(3900,80)
			row=str(now_time)+","
			for i in range(0,len(readings_array)-1,2):
				a=(readings_array[i+1]<<16) +readings_array[i]
				row=row+str(convert(a))+","
			row=row[:-1]+"\n"
			f.write(row)
		
		except Exception as e:
			print e
			print "_________________________________________________"
			instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)		

	


	
