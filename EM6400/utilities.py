from configuration import DATA_BASE_PATH
import glob
import os
import struct

def convert(s):
    '''Function to convert data into float'''
    return struct.unpack("<f",struct.pack("<I",s))[0]

def find_count(day,month):
    '''Function to find the number of existing data files so that overwriting does not happen'''
    path=DATA_BASE_PATH+str(day)+"_"+str(month)
    if not os.path.exists(path):
        os.makedirs(path)
        return 0
    else:
        list_of_files=glob.glob(path+str("/*.csv"))
        return len(list_of_files)