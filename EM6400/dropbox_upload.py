from configuration import THRESHOLD_TIME, DATA_BASE_PATH, BASE_UPLOAD_PATH
from dbupload import DropboxConnection
import db_password
import glob
import os
import time

email=db_password.email
password=db_password.password


folders=os.listdir(DATA_BASE_PATH)
try:
    # Create the connection
    conn = DropboxConnection(email, password)
    #List of files
    for folder in folders:
        list_of_files=glob.glob(str(DATA_BASE_PATH)+str(folder)+str("/*.csv"))
        print list_of_files
        for f in list_of_files:    
            print int(time.time())-int(os.stat(f).st_mtime),f
            if int(time.time())-int(os.stat(f).st_mtime)>THRESHOLD_TIME:
                
                # Upload the file
                print f +" will be uploaded"
                conn.upload_file(f,BASE_UPLOAD_PATH+str(folder),f)
                os.remove(f)
except:
    print("Upload failed")
else:
    pass

