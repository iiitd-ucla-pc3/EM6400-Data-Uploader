from configuration import THRESHOLD_TIME, DATA_BASE_PATH, BASE_UPLOAD_PATH
from dbupload import DropboxConnection
import db_password
import glob
import os
import time

email=db_password.email
password=db_password.password
dropbox_upload_log=open(DATA_BASE_PATH+"db_log.txt","w")


folders=os.listdir(DATA_BASE_PATH)
try:
    # Create the connection
    conn = DropboxConnection(email, password)
    #List of files
    for folder in folders:
        list_of_files=glob.glob(str(DATA_BASE_PATH)+str(folder)+str("/*.csv"))
        for f in list_of_files:    
            
           
            if int(time.time())-int(os.stat(f).st_mtime)>THRESHOLD_TIME:
                
                dropbox_upload_log=open(DATA_BASE_PATH+"db_log.txt","w")
                dropbox_upload_log.write(str(f) +" will be uploaded")
                dropbox_upload_log.close()
                r=open(DATA_BASE_PATH+"db_log.txt","r")
                a=r.read()
                r.close()
                
                conn.upload_file(f,BASE_UPLOAD_PATH+str(folder),f)
                os.remove(f)
except:
    dropbox_upload_log=open(DATA_BASE_PATH+"db_log.txt","w")
    dropbox_upload_log.write("Upload failed"+str(int(time.time())))
    dropbox_upload_log.close()
else:
    pass

