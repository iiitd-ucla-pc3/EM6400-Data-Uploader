#Import all functions from visualize
from basic_functions import *
from pytz import tzinfo
#Location of CSV file containing data
file_location="/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/Jan_2013/22_1.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)

#[plt,fig]=create_plot_options('Apparent Power','Time','Power','W')

ax=plt.axes()

file_location="/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/Jan_2013/15_1.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data_2,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)

file_location="/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/Jan_2013/13_1.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data_3,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)

#Size of window in seconds
WINDOW_SIZE=60*15
low_resolution_power=create_averaged_series(data["W2"], WINDOW_SIZE)
low_resolution_power_2=create_averaged_series(data_2["W2"], WINDOW_SIZE)
low_resolution_power_3=create_averaged_series(data_3["W2"], WINDOW_SIZE)




#Calculating modified timestamp
low_resolution_timestamp=create_averaged_series(raw_timestamp, WINDOW_SIZE)
low_resolution_time_series=[]
for i in range(0,len(low_resolution_timestamp)):
    low_resolution_time_series.append(datetime.datetime.fromtimestamp(int(low_resolution_timestamp[i]),pytz.timezone(TIMEZONE)))
    
plt.title('Power consumption across 3 days (2 weekdays, 1 weekend')
#plt.plot(low_resolution_time_series,low_resolution_power,"green",linewidth="3")
#plt.plot(time,data["W3"],"red")
ax1 = figure(0).add_subplot(311)
ax2 = figure(0).add_subplot(312)
ax3 = figure(0).add_subplot(313)
'''
ax1.bar(low_resolution_time_series,low_resolution_power,width=0.009)
ax2.bar(low_resolution_time_series,low_resolution_power_2,width=0.009)
ax3.bar(low_resolution_time_series,low_resolution_power_3,width=0.009)
'''

ax1.plot(low_resolution_time_series,low_resolution_power)
ax2.plot(low_resolution_time_series,low_resolution_power_2)
ax3.plot(low_resolution_time_series,low_resolution_power_3)

print len(low_resolution_time_series),len(low_resolution_power)

#plt.plot(time,data["W"],"red")

plt.show()