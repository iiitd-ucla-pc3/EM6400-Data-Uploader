#Import all functions from visualize
from basic_functions import *
#Location of CSV file containing data
file_location="/home/nipun/Desktop/nipun/data/23_2/overall.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)
#Customizing the Plot to ensure x ticks don't overlap
[plt,fig]=create_plot_options('Apparent Power','Time','Power','W')
#Plot VA with red lines
plt.plot(time,data["VA"],"red")
#Getting axes object
ax=plt.axes()
#Adding Legend to upper right
plt.legend(('Apparent Power',),
           'upper right', shadow=True, fancybox=True)#Finding point to annotate
'''
x_point=datetime.datetime(2013,1,22,2,10,35,tzinfo=pytz.timezone(TIMEZONE))
print x_point.hour
print x_point.minute
#Finding index of point in time and VA series
x_index=time.index(x_point) 
y_point=data["VA"][x_index]
#Annotating point with appliance name
ax.annotate("Refrigerator",
            xy=(x_point, y_point), xycoords='data',
            xytext=(x_point+datetime.timedelta(minutes=3), +1000), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
            )
#S
'''
plt.show()
