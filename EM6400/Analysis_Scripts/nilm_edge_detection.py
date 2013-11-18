from basic_functions import *
from normalize import *
TOLERANCE_REAL=50
from sklearn.cluster import MeanShift, estimate_bandwidth
active_power="W1"
reactive_power="VAR1"

from scipy.spatial import distance
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from scipy.cluster.vq import kmeans,vq

'''Read Data'''
#Location of CSV file containing data
file_location="/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/23_2/23_12.csv"
#List of fields to use
fields_to_use=field_array[1:30]
#Whether the CSV contains a header row or not
contains_header=True
#Return time and data corresponding to field list mentioned above
[time,data,raw_timestamp]=create_Field_arrays(file_location,fields_to_use,contains_header)

print data['VA1']
print len(time),len(data[active_power])
minimum=min(len(data[active_power]),len(data[reactive_power]),len(time))
time=time[:minimum-1]
data[active_power]=data[active_power][:minimum-1]
data[reactive_power]=data[reactive_power][:minimum-1]

print len(time),len(data[active_power])
'''Unnormalized power'''
figure(0)
[plt,fig]=create_plot_options('Unnormzalized Power vs Time','Time','Power','W')
plt.plot(time,data[active_power])
plt.plot(time,data[reactive_power])
plt.legend(('Active Power','Reactive Power'),'upper right')



'''Draw plot for voltage showing the fluctuation'''
figure(1)
[plt,fig]=create_plot_options('Voltage vs Time','Time','Voltage','V')
plt.plot(time,data["VLN"][:minimum-1])
#plt.show()

'''Draw real and normalized power and add the capability to zoom the two together'''
figure(2)
'''ax2 = figure(2).add_subplot(211)
ax3 = figure(2).add_subplot(212, sharex=ax2)'''


  # share ax1's xaxis

data["N_W3"]=normalize(data[active_power],data["VLN"])
data["N_VAR3"]=normalize(data[reactive_power],data["VLN"])
[plt,fig]=create_plot_options('Normzalized Power vs Time','Time','Power','W')
plt.plot(time,data["N_W3"])
plt.plot(time,data["N_VAR3"])
plt.legend(('Active Power','Reactive Power'),'upper right')
'''ax2.plot(time,data["N_W3"])
ax3.plot(time,data["N_VAR3"])'''

#plt.show()

'''Removing transients'''
'''
i=1
while i<len(data["N_W3"]):
    if (math.fabs(data["N_W3"][i]-data["N_W3"][i-1])>100 and math.fabs((data["N_W3"][i+1]+data["N_W3"][i+2])/2-data["N_W3"][i])>100):
        
        del data["N_W3"][i-6:i+6]
        del data["N_VAR3"][i-6:i+6]
        del time[i-6:i+6]
        print i
        i=i-12
    
    i=i+1
        
    '''   
plt.plot(time,data["N_W3"],'y')

'''Find step changes'''
i=0
active_power_running_average=0
reactive_power_running_average=0
points_in_current_window=0
events=[]
events_times=[]
events_reactive=[]
averages=[]
averages_reactive=[]
count=0
while i<len(data["N_W3"]):
    #print i
    #averages.append(active_power_running_average)
    #averages_reactive.append(reactive_power_running_average)
    if math.fabs(data["N_W3"][i]-active_power_running_average)>TOLERANCE_REAL:
        count=count+1
        
        averages.append(active_power_running_average)
        averages_reactive.append(reactive_power_running_average)
        #print i,data["N_W3"][i]-active_power_running_average,active_power_running_average,data["N_W3"][i],(sum(data["N_W3"][i+3:i+14])/10)

        #Step change has been detected
        if i+3<minimum:
            events.append(data["N_W3"][i+3])
            events_reactive.append(data["N_VAR3"][i+3])
            active_power_running_average=data["N_W3"][i+3]
            reactive_power_running_average=data["N_VAR3"][i+3]
        #events.append((sum(data["N_W3"][i+3:i+14])/10)-active_power_running_average)
        #print count,i,data["N_W3"][i]-active_power_running_average,active_power_running_average,events[-1]
        events_times.append(time[i])
        #print events[time[i]],i
        #print events
        
        
        #active_power_running_average=(sum(data["N_W3"][i+3:i+14])/10)
        #reactive_power_running_average=(sum(data["N_VAR3"][i+3:i+14])/10)
        points_in_current_window=1
        i=i+3
    else:
        active_power_running_average=(active_power_running_average*points_in_current_window+data["N_W3"][i])/(points_in_current_window+1)
        reactive_power_running_average=(reactive_power_running_average*points_in_current_window+data["N_VAR3"][i])/(points_in_current_window+1)

        points_in_current_window=points_in_current_window+1
        i=i+1

plt.plot(events_times,events,'ro')
#ax3.plot(events_times,events_reactive,'ro')
figure(3)
#plt.plot(events_times,events)
#plt.plot(averages)
delta_averages=[]   
delta_averages_reactive=[]
for i in range(0,len(averages)-1):
    if math.fabs(averages[i+1]-averages[i])>TOLERANCE_REAL:
        delta_averages.append(averages[i+1]-averages[i])
        delta_averages_reactive.append(averages_reactive[i+1]-averages_reactive[i])

#delta_averages=[averages[i+1]-averages[i] for i in range(0,len(averages)-1) if math.fabs(averages[i+1]-averages[i])>TOLERANCE_REAL ]
#delta_averages_reactive=[averages_reactive[i+1]-averages_reactive[i] for i in range(0,len(averages)-1) if (averages_reactive[i+1]-averages_reactive[i])>10]
Z=[[delta_averages[i],delta_averages_reactive[i]] for i in range(0,len(delta_averages))]
#print Z
X=np.array(Z)


plt.plot(averages)
plt.plot(averages_reactive)
#print delta_averages
#plt.plot(events_times[:-1],delta_averages_reactive)
figure(4)

plt.title('Step changes')
plt.scatter(delta_averages, delta_averages_reactive)
plt.xlabel('Real Power (W)')
plt.ylabel('Reactive Power (VA)')
ax=plt.axes()
ax=create_annotation(ax, (2035, -40), (2050,-70), "Geyser on", 15)
ax=create_annotation(ax, (-2060, 40), (-2070,70), "Geyser off", 15)
ax=create_annotation(ax, (100, 100), (120,120), "Refrigerator on", 15)
ax=create_annotation(ax, (-100, -100), (-120,-120), "Refrigerator off", 15)
ax=create_annotation(ax, (617, 200), (630,250), "Motor on", 15)
ax=create_annotation(ax, (-550, -175), (-560,-190), "Motor off", 15)




#plt.plot(time,data["N_W3"],"red")

figure(5)
##############################################################################
# Compute similarities
D = distance.squareform(distance.pdist(X))
S = 1 - (D / np.max(D))
# Compute DBSCAN
db = DBSCAN(eps=.1, min_samples=5).fit(S)
core_samples = db.core_sample_indices_
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)


##############################################################################
# Plot result
import pylab as pl
from itertools import cycle

#pl.close('all')


# Black removed and is used for noise instead.
colors = cycle('bgrcmybgrcmybgrcmybgrcmy')
for k, col in zip(set(labels), colors):
    if k == -1:
        # Black used for noise.
        col = 'k'
        markersize = 6
    class_members = [index[0] for index in np.argwhere(labels == k)]
    cluster_core_samples = [index for index in core_samples
                            if labels[index] == k]
    for index in class_members:
        x = X[index]
        if index in core_samples and k != -1:
            markersize = 14
        else:
            markersize = 6
        pl.plot(x[0], x[1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=markersize)
plt.xlabel('Real Power (W)')
plt.ylabel('Reactive Power (VA)')
plt.title('DBSCAN clustering')
#pl.show()
#plt.plot(events)
#plt.plot(averages_reactive)
#print "EVENTS"
#print len(averages),averages,count
figure(6)
plt.plot(delta_averages)
plt.title('Real Power Step change')
plt.xlabel('Event number')
plt.ylabel('Step Change (W)')

figure(7)
'''K MEANS'''
# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(X,4)
# assign each sample to a cluster
idx,_ = vq(X,centroids)

# some plotting using numpy's logical indexing
plot(X[idx==0,0],X[idx==0,1],'ob',
     X[idx==1,0],X[idx==1,1],'or',
     X[idx==2,0],X[idx==2,1],'oy',
     X[idx==3,0],X[idx==3,1],'om')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
xlabel('Real Power (W)')
ylabel('Reactive Power (VA)')
title('K Means clustering with 4 clusters')
figure(8)

'''Building appliance table'''
devices_info={}
devices_info['Geyser']={}
devices_info['Geyser']['On']=[2150,-28]
devices_info['Geyser']['Off']=[-2150,28]
devices_info['Fri']={}
devices_info['Fri']['On']=[110,60]
devices_info['Fri']['Off']=[-110,-60]
devices_info['Motor']={}
devices_info['Motor']['On']=[610,100]
devices_info['Motor']['Off']=[-610,-100]
devices_info['TV']={}
devices_info['TV']['On']=[80,0]
devices_info['TV']['Off']=[-80,0]
devices_info['Unallocated']={}
devices_info['Unallocated']['On']=[100000,100000]
devices_info['Unallocated']['Off']=[-100000,-100000]



'''Current state of appliances'''
state={}
state['Geyser']='Off'
state['Fri']='Off'
state['Motor']='Off'
state['TV']='Off'

'''Color codes'''
colors={}
colors['Geyser']={}
colors['Geyser']['On']='r'
colors['Fri']={}
colors['Fri']['On']='y'
colors['Motor']={}
colors['Motor']['On']='b'
colors['TV']={}
colors['TV']['On']='g'

geyser_on=[]
geyser_off=[]

ref_on=[]
ref_off=[]

motor_on=[]
motor_off=[]



    
'''Using appliance table to make prediction'''
i=0
active_power_running_average=0
reactive_power_running_average=0
points_in_current_window=0
disaggregated_series=[0]*len(data["N_W3"])
plt.plot(time,data["N_W3"])
#fill_between(time,0,2000,colors='red')
events=[0]
events_times=[time[0]]
events_reactive=[0]

durations={}
for key in devices_info:
    durations[key]={}
    for key_state in devices_info[key]:
        durations[key][key_state]=[]
print durations
while i<len(data["N_W3"]):
    #print i,math.fabs(data["N_W3"][i+3])
    if math.fabs(data["N_W3"][i]-active_power_running_average)>TOLERANCE_REAL:
        events.append(sum(data["N_W3"][i+4:i+5])/1)
        events_reactive.append(sum(data["N_VAR3"][i+4:i+5])/1)
        #events.append((sum(data["N_W3"][i+3:i+14])/10)-active_power_running_average)
        #print count,i,data["N_W3"][i]-active_power_running_average,active_power_running_average,events[-1]
        events_times.append(time[i])
        #print events[-1],events_reactive[-1],events_times
        #print math.fabs(data["N_W3"][i]-active_power_running_average)
        '''Some event has occured, we need to do a lookup'''
        min_real,min_reactive=10000,10000
        min_key="Unallocated"
        min_state="On"
        for key in devices_info:
            
            for key_state in devices_info[key]:
                
                #print key,key_state
                
                #print i,math.fabs(data["N_W3"][i+3]-devices_info[key][key_state][0]),time[i]
                diff_real=math.fabs(events[-1]-events[-2]-devices_info[key][key_state][0])
                diff_reactive=math.fabs(events_reactive[-1]-events_reactive[-2]-devices_info[key][key_state][1])
                print diff_real,diff_reactive,key,key_state,events[-1]-events[-2]
                if (diff_real<50 and diff_reactive<50 and diff_real<min_real and diff_reactive<min_reactive):
                    print diff_real,diff_reactive
                    if state[key]!=key_state:
                        min_real=diff_real
                        min_reactive=diff_reactive
                        min_key=key
                        min_state=key_state
                        
        print min_real,min_reactive,min_key,min_state                
        state[min_key]=min_state
        print i,'New state of '+min_key+" is",min_state,time[i],data["N_W3"][i+5],events[-1]-devices_info[key][key_state][0]
        
        durations[min_key][min_state].append(time[i])
        '''
        if min_state=='On' and min_key=='Geyser':
            geyser_on.append(time[i])
            print 'GEYSER ON'
        elif min_state=='Off' and min_key=='Geyser':
            print 'GEYSER OFF'
            geyser_off.append(time[i])
        elif min_state=='On' and min_key=='Fri':
            print 'REF ON'
            ref_on.append(time[i])
        elif min_state=='Off' and min_key=='Fri':
            print 'NOTHING'
            ref_off.append(time[i])
        elif min_state=='On' and min_key=='Motor':
            motor_on.append(time[i])
        elif min_state=='Off' and min_key=='Motor':
            motor_off.append(time[i])
        '''
        active_power_running_average=sum(data["N_W3"][i+4:i+5])/1
        reactive_power_running_average=sum(data["N_VAR3"][i+4:i+5])/1
        #active_power_running_average=(sum(data["N_W3"][i+3:i+14])/10)
        #reactive_power_running_average=(sum(data["N_VAR3"][i+3:i+14])/10)
        points_in_current_window=1
        i=i+5       
        
    else:
        
        #print active_power_running_average,time[i],state
        active_power_running_average=(active_power_running_average*points_in_current_window+data["N_W3"][i])/(points_in_current_window+1)
        reactive_power_running_average=(reactive_power_running_average*points_in_current_window+data["N_VAR3"][i])/(points_in_current_window+1)

        points_in_current_window=points_in_current_window+1
        y=0
        '''
        for appliance in state:
            #print appliance,state,state[appliance],i
            if state[appliance]=='On':
                fill_between(events_times[-2:-1], y,devices_info[appliance]['On'][0],colors='green')
                y=y+devices_info[appliance]['On'][0]
                #print y
                
        '''
        i=i+1
    #print y
                
#plt.plot(events_times[1:],events[1:],'ro')   

print durations

for appliance in durations:
    for i in range(0,min(len(durations[appliance]['On']),len(durations[appliance]['Off']))):
    
        fill_between(time[time.index(durations[appliance]['On'][i]):time.index(durations[appliance]['Off'][i])],0,devices_info[appliance]['On'][0],color=colors[appliance]['On'])

'''         
for i in range(0,min(len(ref_on),len(ref_off))):
    fill_between(time[time.index(ref_on[i]):time.index(ref_off[i])],0,100,colors='y',alpha=2)
for i in range(0,min(len(motor_on),len(motor_off))):
    fill_between(time[time.index(motor_on[i]):time.index(motor_off[i])],0,650,colors='k',alpha=2)
'''
'''
    plt.plot(ref_on,[1000]*len(ref_on),'bo')
    plt.plot(ref_off,[1200]*len(ref_off),'ko')
    plt.plot(geyser_on,[2000]*len(geyser_on),'bo')
    plt.plot(geyser_off,[2100]*len(geyser_off),'ko')
    '''

print motor_on,motor_off
plt.legend(('Geyser','Refrigerator','Motor'),
           'upper right', shadow=True, fancybox=True)
p = Rectangle((0, 0), 1, 1, fc="y")
p1=Rectangle((0, 0), 1, 1, fc="g")
p2=Rectangle((0, 0), 1, 1, fc="k")

legend([p,p1,p2], ["Refrigerator","Geyser","Motor"])
plt.xlabel('Time')
plt.ylabel('Normalized Active Power(W)')
plt.show()

    
        

        
