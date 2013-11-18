#Import all functions from visualize
from basic_functions import *
#Location of CSV file containing data
file_location="/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/Jan_2013/22_1.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data]=create_Field_arrays(file_location,fields_to_use,contains_header)
#Customizing the Plot to ensure x ticks don't overlap
[plt,fig]=create_plot_options('Annotation of common appliances','Time','Power','W')
#Plot VA with red lines
plt.plot(time,data["W1"],"red")
plt.plot(time,data["VAR1"],"green")
#Getting axes object
ax=plt.axes()
#Adding Legend to upper right
plt.legend(('Active Power','Reactive Power'),
           'upper right', shadow=True, fancybox=True)#Finding point to annotate
x_point=datetime.datetime(2013,1,22,2,10,35,tzinfo=pytz.timezone(TIMEZONE))
[(x_point,y_point),xy]=create_annotation_points(time, data["W1"], x_point, 3, 2000)
ax=create_annotation(ax, (x_point, y_point), xy, "Refrigerator", 15)

geyser_x_point=datetime.datetime(2013,1,22,5,10,35,tzinfo=pytz.timezone(TIMEZONE))
[(x_point,y_point),xy]=create_annotation_points(time, data["W1"], geyser_x_point, 3, 3000)
ax=create_annotation(ax, (x_point, y_point), xy, "Geyser Used by Family", 15)

motor_x_point=datetime.datetime(2013,1,22,6,10,35,tzinfo=pytz.timezone(TIMEZONE))
[(x_point,y_point),xy]=create_annotation_points(time, data["W1"], motor_x_point, 3, 2500)
ax=create_annotation(ax, (x_point, y_point), xy, "Motor Used by Family", 15)

geyser_maid_x_point=datetime.datetime(2013,1,22,11,46,35,tzinfo=pytz.timezone(TIMEZONE))
[(x_point,y_point),xy]=create_annotation_points(time, data["W1"], geyser_maid_x_point, 3, 2000)
ax=create_annotation(ax, (x_point, y_point), xy, "Geyser Used by Maid", 15)

washing_x_point=datetime.datetime(2013,1,22,12,35,35,tzinfo=pytz.timezone(TIMEZONE))
[(x_point,y_point),xy]=create_annotation_points(time, data["W1"], washing_x_point, 3, 3000)
ax=create_annotation(ax, (x_point, y_point), xy, "Washing Machine", 15)

plt.show()
