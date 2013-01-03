from matplotlib import rc
from pylab import *
import csv
import matplotlib.pyplot as plt
import pytz
import sys
import time
from configuration import TIMEZONE
from maths_functions import *

field_array=      ["Time","VA"          ,"W"    ,"VAR"         ,"PF","VLL"  ,"VLN"  ,"A"      ,"F" ,"VA1"         ,"W1"   ,"VAR1"        ,"PF1","V12"  ,"V1"   ,"A1"     ,"VA2"         ,"W2"   ,"VAR2"        ,"PF2","V23"  ,"V2   ","A2"     ,"VA3"         ,"W3"   ,"VAR3"        ,"PF3","V31"  ,"V3"   ,"A3"     ,"FwdVAh","FwdWh","FwdVARh","FwdVARh","Present_demand","Max_MD","Max_DM_time","RevVAh","RevWh","RevVARh","RevVARh"]
field_array_units=["s"   ,"Volt-Amperes","Watts","Volt-Amperes",""  ,"Volts","Volts","Amperes","Hz","Volt-Amperes","Watts","Volt-Amperes",""   ,"Volts","Volts","Amperes","Volt-Amperes","Watts","Volt-Amperes",""   ,"Volts","Volts","Amperes","Volt-Amperes","Watts","Volt-Amperes",""   ,"Volts","Volts","Amperes","Joules","Joules","Joules","Joules","","","","Joules","Joules","Joules","Joules"]

field_array_phase_1_numbers=range(8,16)
field_array_phase_2_numbers=range(16,24)
field_array_phase_3_numbers=range(24,32)
def draw_plot_field_names(csv_file,field_names_to_plot,contains_header,save,file_save_path):
	field_numbers=[field_array.index(field_name) for field_name in field_names_to_plot]
	draw_plot(csv_file,field_numbers,contains_header,save,file_save_path)
	
def draw_plot(csv_file,field_numbers,contains_header,save,file_save_path):
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
			try:
				Y[i].append(float(row[field_numbers[i]]))
			except:
				print i,row
				try:
					X.remove(datetime.datetime.fromtimestamp(int(row[0]),pytz.timezone(TIMEZONE)))
				except:
					pass
	
	for i in range(0,len(field_numbers)):
		y_label=field_array[field_numbers[i]]
		figure = plt.gcf() # get current figure
		figure.set_size_inches(12, 8)
# when saving, specify the DPI
		grid(True)
		plt.title(y_label+ " vs Time",fontsize=35)
		plt.xlabel('Time',fontsize=35)
		plt.ylabel(y_label+" ("+field_array_units[field_numbers[i]]+")",fontsize=35)
		plt.tick_params(axis='both', which='major', labelsize=20)
		plt.axes().relim()
		plt.axes().autoscale_view(True,True,True)
		plt.plot(X,Y[i]	)
		av=average(Y[i])				
		#print "Mean of "+y_label+" is: ",av," Stdev is: ",stdev(Y[i], av),"Min :",min(Y[i]),"Max:",max(Y[i])
			
		figure.autofmt_xdate()	
		if save:
			plt.savefig(file_save_path+y_label+".eps", bbox_inches=0,dpi=300)
		else:
			plt.show()
		plt.close()
		
'''Example Calls'''
		
#Plotting data from a CSV containing header row for V1,A1,V2 parameters and not saving plots
draw_plot_field_names("/home/nipun/Desktop/data/25_12/overall.csv",field_array[1:],True,False,'/home/nipun/study/reports/e_energy/figures/india/amarjeet/29_12/')
#draw_plot("/home/nipun/Desktop/data/25_12/overall.csv",field_array_phase_3_numbers,True,False,'/home/nipun/study/reports/e_energy/figures/india/amarjeet/29_12/')

#Plotting data from a CSV containing header row for V1,A1,V2 parameters and saving plots
#draw_plot_field_names("csv_with_header.csv",["V1","A1","V2"],True,True)

#Plotting data from a CSV without header row for V1,A1,V2 parameters and not saving plots
#draw_plot_field_names("csv_without_header.csv",["V1","A1","V2"],False,False)

#Plotting data from a CSV without header row for 2,3,4th parameter and saving plots 
#draw_plot("csv_without_header.csv",[2,3,11],False,True)



