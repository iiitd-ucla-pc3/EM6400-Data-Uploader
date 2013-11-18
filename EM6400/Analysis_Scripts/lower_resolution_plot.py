#Import all functions from visualize
from basic_functions import *
from pytz import tzinfo
#Location of CSV file containing data
file_location="/home/nipun/Dropbox/SmartMeter/Home/Nipun/Feb_2013/17_2.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)

[plt,fig]=create_plot_options('Apparent Power','Time','Power','W')

ax=plt.axes()


#Size of window in seconds
WINDOW_SIZE=60*15
low_resolution_power=create_averaged_series(data["W2"], WINDOW_SIZE)

#Calculating modified timestamp
low_resolution_timestamp=create_averaged_series(raw_timestamp, WINDOW_SIZE)
low_resolution_time_series=[]
for i in range(0,len(low_resolution_timestamp)):
    low_resolution_time_series.append(datetime.datetime.fromtimestamp(int(low_resolution_timestamp[i]),pytz.timezone(TIMEZONE)))
    

figure(0)
#plt.plot(low_resolution_time_series,low_resolution_power,"green",linewidth="3")
#plt.plot(time,data["W3"],"red")
plt.bar(low_resolution_time_series,low_resolution_power,width=0.01,colors='red')
print len(low_resolution_time_series),len(low_resolution_power)

figure(1)
plt.bar(low_resolution_time_series,low_resolution_power,width=0.01,colors='green')


#plt.plot(time,data["W"],"red")
plt.show()