from dbupload import DropboxConnection
from getpass import getpass
import random,time,glob,os

#email = raw_input("Enter Dropbox email address:")
#password = getpass("Enter Dropbox password:")

email="smartroom.iiit@gmail.com"	
password="password"
# Create a little test file

threshold=900
base_path='/root/em6400/data/'
#Path in Dropbox in which to upload the data
base_upload_path='/SmartMeter/Lab/'
folders=os.listdir(base_path)


try:
    # Create the connection
    conn = DropboxConnection(email, password)
  
     
    #List of files
    for folder in folders:
		list_of_files=glob.glob(str(base_path)+str(folder)+str("/*.csv"))
		print list_of_files
		for f in list_of_files:	    
			if int(time.time())-int(os.stat(f).st_mtime)>threshold:
				# Upload the file
				print f +"will be uploaded"
				conn.upload_file(f,base_upload_path+str(folder),f)
				os.remove(f)
except:
    print("Upload failed")
else:
    pass
