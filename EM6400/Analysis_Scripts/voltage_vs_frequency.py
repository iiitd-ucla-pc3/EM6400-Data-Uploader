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
[plt,fig]=create_plot_options('Apparent Power','Time','Power','W')


#Plot VA with red lines
def mat_div(a, b): 
    return [(a[i]*a[i])/b[i] for i in range(0,len(a))] 


from numpy import arange,array,ones,linalg
from pylab import plot,show

x=np.array(raw_timestamp[1:100])
# linearly generated sequence
import random
y = np.array(x+random.randint(0,50))
p30=np.poly1d(np.polyfit(x, y, 2))
print p30(x),x
plt.plot(x,p30(x),'r')
plt.scatter(x,y)
show()


#Getting axes object
plt.show()#Adding Legend to upper right
