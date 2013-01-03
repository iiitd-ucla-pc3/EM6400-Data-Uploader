from configuration import METER_PORT, METER_ID, DATA_BASE_PATH, THRESHOLD_TIME, \
	TIMEZONE, EM6400_BASE_REGISTER, EM6400_NUMBER_OF_REGISTERS, BAUD_RATE, HEADER
from utilities import convert, find_count, delete_older_folders
import datetime
import minimalmodbus
import pytz
import time

instrument = minimalmodbus.Instrument(METER_PORT, METER_ID)
instrument.serial.baudrate = BAUD_RATE   # Baud

start_time=int(time.time())
now = datetime.datetime.now(pytz.timezone(TIMEZONE))
start_day=now.day
start_month=now.month
count=find_count(now.day, now.month)

f=open(DATA_BASE_PATH+str(start_day)+"_"+str(start_month)+"/"+str(count)+".csv","wa")
f.write(HEADER)
log_file=open(DATA_BASE_PATH+"log.txt","w")


while True:
	now_time=int(time.time())
	now = datetime.datetime.now(pytz.timezone(TIMEZONE))
	now_day=now.day
	now_month=now.month
	
	
	if ((now_time-start_time) > THRESHOLD_TIME) or (now_day!=start_day):
		if now_day!=start_day:
			count=find_count(now_day, now_month)-1
			delete_older_folders(now)
		count=count+1
		start_time=now_time
		start_day=now_day
		start_month=now_month
		f.close()
		f=open(DATA_BASE_PATH+str(start_day)+"_"+str(start_month)+"/"+str(count)+".csv","wa")
		f.write(HEADER)

	else:
		try:
			readings_array = instrument.read_registers(EM6400_BASE_REGISTER,EM6400_NUMBER_OF_REGISTERS)
			row=str(now_time)+","
			for i in range(0,len(readings_array)-1,2):
				a=(readings_array[i+1]<<16) +readings_array[i]
				row=row+str(convert(a))+","
			row=row[:-1]+"\n"
			f.write(row)
		
		except Exception as e:
			log_file.write(str(time.time())+" "+e.__str__())
			instrument = minimalmodbus.Instrument(METER_PORT, METER_ID)		

	


	
