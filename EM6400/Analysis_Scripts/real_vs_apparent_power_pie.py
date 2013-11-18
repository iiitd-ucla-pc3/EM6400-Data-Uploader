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
#Total Apparent Power
total_apparent_power=sum(data["VA3"])
#Total Real Power
total_real_power=sum(data["W3"])
#Pie chart protrusion
explode=(0.05,0.05)
#Labels for Pie Chart
labels='Real','Reactive'
#Fractions for Pie Charts
fracs=[(100*total_real_power)/total_apparent_power,100-(100*total_real_power)/total_apparent_power]
#Draw the pie chart
pie(fracs,explode=explode,labels=labels,shadow=True, autopct='%1.1f%%')
plt.title("Contribution of Real and Reactive Power to Apparent Power for Second Floor")
plt.show()


#plt.savefig("/home/nipun/study/reports/real_vs_apparent.eps", bbox_inches=0)