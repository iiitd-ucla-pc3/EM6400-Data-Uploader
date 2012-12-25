from pylab import *
import csv
import matplotlib.pyplot as plt
import pytz
import sys
import time
from configuration import TIMEZONE

field_array=["Time","VA","W","VAR","PF","VLL","VLN","A","F","VA1","W1","VAR1","PF1","V12","V1","A1","VA2","W2","VAR2","PF2","V23","V2","A2","VA3","W3","VAR3","PF3","V31","V3","A3","FwdVAh","FwdWh","FwdVARh","FwdVARh","Present_demand","Max_MD","Max_DM_time","RevVAh","RevWh","RevVARh","RevVARh"]


def draw_plot_field_names(csv_file,field_names_to_plot,contains_header,save):
	field_numbers=[field_array.index(field_name) for field_name in field_names_to_plot]
	draw_plot(csv_file,field_numbers,contains_header,save)
	
def draw_plot(csv_file,field_numbers,contains_header,save):
	X=[]
	Y=[]
	print field_numbers
	for i in range(len(field_numbers)):
		Y.append([])
	file_pointer = csv.reader(open(csv_file, 'rb'))
	
	print file_pointer
	if contains_header:
		header=file_pointer.next()
	for row in file_pointer:
		X.append(datetime.datetime.fromtimestamp(int(row[0]),pytz.timezone(TIMEZONE)))
		for i in range(0,len(field_numbers)):
			Y[i].append(float(row[field_numbers[i]]))
	
	for i in range(0,len(field_numbers)):
		y_label=field_array[field_numbers[i]]
		plt.title(y_label+ " vs Time")
		plt.xlabel('Time')
		plt.ylabel(y_label)
		plt.plot(X,Y[i]	)
		if save:
			plt.savefig(y_label+ " vs Time", bbox_inches=0)
		else:
			plt.show()
		plt.close()
		
'''Example Calls'''
		
#Plotting data from a CSV containing header row for V1,A1,V2 parameters and not saving plots
draw_plot_field_names("csv_with_header.csv",["V1","A1","V2","VAR1"],True,False)

#Plotting data from a CSV containing header row for V1,A1,V2 parameters and saving plots
#draw_plot_field_names("csv_with_header.csv",["V1","A1","V2"],True,True)

#Plotting data from a CSV without header row for V1,A1,V2 parameters and not saving plots
#draw_plot_field_names("csv_without_header.csv",["V1","A1","V2"],False,False)

#Plotting data from a CSV without header row for 2,3,4th parameter and saving plots 
#draw_plot("csv_without_header.csv",[2,3,11],False,True)



