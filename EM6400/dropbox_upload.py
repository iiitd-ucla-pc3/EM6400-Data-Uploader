from configuration import THRESHOLD_TIME, DATA_BASE_PATH, BASE_UPLOAD_PATH,URL_PATH
import glob
import os
import time
import requests

file_upload_log=open(DATA_BASE_PATH+"file_upload_log.txt","w")

while True:

    folders=os.listdir(DATA_BASE_PATH)
    try:
        
        for folder in folders:
            list_of_files=glob.glob(str(DATA_BASE_PATH)+str(folder)+str("/*.csv"))
            for f in list_of_files:    
                if int(time.time())-int(os.stat(f).st_mtime)>THRESHOLD_TIME:
                
                    file_upload_log=open(DATA_BASE_PATH+"file_upload_log.txt","w")
                    file_upload_log.write(str(f) +" will be uploaded")
                    file_upload_log.close()
                    r=open(f,"r")
                    files = {'myfile': r} 
                    g = requests.post(url=URL_PATH,files=files)
                    if g.status_code==200:
                        os.remove(f)
    except:
        file_upload_log=open(DATA_BASE_PATH+"file_upload_log.txt","w")
        file_upload_log.write("Upload failed"+str(int(time.time())))
        file_upload_log.close()
    else:
        pass
    time.sleep(THRESHOLD_TIME)

