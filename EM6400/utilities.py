from configuration import DATA_BASE_PATH
import glob
import os
import struct
import re

re_pattern=re.compile('.*/(\d+)\.csv')

'''
Tests to check validity of regular expressions
match=re_pattern.match('/home/nipun/21/2.csv')
print match       
print match.group(1)'''

def convert(s):
    '''Function to convert data into float'''
    return struct.unpack("<f",struct.pack("<I",s))[0]

def find_count(day,month):
    '''Function to correct number of next data file to be generated and create corresponding folders according to date'''
    path=DATA_BASE_PATH+str(day)+"_"+str(month)
    if not os.path.exists(path):
        os.makedirs(path)
        return 0
    else:
        list_of_files=glob.glob(path+str("/*.csv"))
        if len(list_of_files)==0:
            return 0
        else:
            file_numbers_list=[int(re_pattern.match(file_name).group(1)) for file_name in list_of_files]
            return max(file_numbers_list)+1
