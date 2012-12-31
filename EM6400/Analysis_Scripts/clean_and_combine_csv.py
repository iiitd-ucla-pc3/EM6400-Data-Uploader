from configuration import HEADER
from sqlite3 import IntegrityError
import csv
import glob
import os
import re
import sqlite3
import time

re_pattern=re.compile('.*/(\d+\.csv)')


def create_table_fields():
    temp=""
    for i in range(0,41):
        temp=temp+"field"+str(i)+" text, "
    temp=temp+"primary key (field0)"
    return temp

def create_insert_string():
    temp="insert into test values ("
    for i in range(0,41):
        temp=temp+"?, "  
    temp=temp[:-2]+")"
    return temp
          

def create_temp_table():
    conn = sqlite3.connect('single.db')
    cur = conn.cursor()
    table_structure_string="create table if not exists test("+create_table_fields()+")"
    cur.execute(table_structure_string)
    conn.commit()
    return [conn,cur]



def remove_duplicates(filename,contains_header):
    seen=set()
    count=0
    f_read=csv.reader(open(filename, 'rb'))
    file_number_string=re_pattern.match(filename).group(1)
    outfile=re.sub(file_number_string,"backup_"+file_number_string,filename)
    print outfile
    f_write=csv.writer(open(outfile,'wa'))
    if contains_header:
        f_read.next()
    for row in f_read:
        if row[0] not in seen:
            seen.add(row[0])
            f_write.writerow(row)
            count=count+1
    
    os.remove(filename)
    os.rename(outfile,filename)
    
    return count
    
        
    
    
    


def remove_duplicates_from_csv(base_path,filename,contains_header):
    insert_string=create_insert_string()
    [conn,cur]=create_temp_table()
    #Empty database for faster management
    cur.execute("delete from test")
    conn.commit()
    os.rename(base_path+filename,base_path+filename+"~")
    file_pointer = csv.reader(open(base_path+filename+"~", 'rb'))
    file_pointer_writer=csv.writer(open(base_path+filename,'wa'))
    if contains_header:
        header=file_pointer.next()
    for row in file_pointer:
        try:
        
            cur.execute(insert_string,row)
            conn.commit()
            
        except IntegrityError:
            pass
    conn.commit()
    cur.execute('select * from test')
    count=0
    for row in cur:
        count=count+1
        file_pointer_writer.writerow(row)
   
    return count

print create_insert_string()
path='/home/nipun/Desktop/data/25_12/'
list_of_files=glob.glob(path+str("/*.csv"))
number_of_files=len(list_of_files)
count=0
for file_name in list_of_files:  
    count=count+remove_duplicates(file_name,True)
print count
outfile=open(path+"overall.csv","wa")
outfile.write(HEADER)
for i in range(0,number_of_files):
    outfile.write(open(path+str(i)+".csv").read())
    
outfile.close()

    
    



    