THRESHOLD_TIME=900 #Time in seconds after which a new CSV gets created
DATA_BASE_PATH="/home/nipun/Desktop/data/" #The path where the data gets stored
METER_PORT="/dev/ttyUSB0"  #The serial port where the meter is connected
METER_ID=2 #The slave id assigned to the meter
BAUD_RATE=19200 #The baud rate for serial communication
HEADER="Timestamp,VA,W,VAR,PF,VLL,VLN,A,F,VA1,W1,VAR1,PF1,V12,V1,A1,VA2,W2,VAR2,PF2,V23,V2,A2,VA3,W3,VAR3,PF3,V31,V3,A3,FwdVAh,FwdWh,FwdVARh,FwdVARh\n"
BASE_UPLOAD_PATH="/SmartMeter/Lab/"
EM6400_BASE_REGISTER=3900
EM6400_NUMBER_OF_REGISTERS=66
GMT_TIME_DIFFERENCE_MILLISECONDS=19800000
TIMEZONE='Asia/Kolkata'
URL_PATH="http://192.168.16.251:9001/upload"
