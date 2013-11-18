#Import all functions from visualize
from basic_functions import *
#Location of CSV file containing data
file_location="/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/Jan_2013/22_1.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)
#Customizing the Plot to ensure x ticks don't overlap
[plt,fig]=create_plot_options('Apparent and Real Power','Time','Power','W')
#Plot VA with red lines
plt.plot(time,data["VA3"],"red")
#Plot W with yellow lines
plt.plot(time,data["W3"],"yellow")
#Fill with Yellow Area under Real Power
fill_between(time,data["W3"],0,color='yellow')
#Fill with Red the Area between Apparent and Real Power
fill_between(time, data["W3"],data["VA3"] ,color="red")
#Getting axes object
ax=plt.axes()
#Adding Legend to upper right
plt.legend(('Apparent Power','Real Power'),
           'upper right', shadow=True, fancybox=True)

#Save the plot
plt.show()
#plt.savefig("/home/nipun/study/reports/real_vs_apparent.eps", bbox_inches=0)