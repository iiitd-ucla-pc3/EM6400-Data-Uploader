import shutil
destination=open("/home/nipun/Desktop/22_12.csv","a")
destination.write("Time,VA,W,VAR,PF,VLL,VLN,A,F,VA1,W1,VAR1,PF1,V12,V1,A1,VA2,W2,VAR2,PF2,V23,V2,A2,VA3,W3,VAR3,PF3,V31,V3,A3,FwdVAh,FwdWh,FwdVARh,FwdVARh,Present_demand,Max_MD,Max_DM_time,RevVAh,RevWh,RevVARh,RevVARh" )
for i in range(1,44):
    shutil.copyfileobj(open("/home/nipun/Dropbox/SmartMeter/Home/Amarjeet/22_12/"+str(i)+".csv",'rb'), destination)
    print i
destination.close()
