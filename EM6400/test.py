from utilities import find_count, delete_older_folders
import datetime

'''
print find_count(24,12)
print find_count(25,12)
print find_count(22,12)
print find_count(31,12)
'''

print delete_older_folders(datetime.datetime.now())