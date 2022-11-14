from fileinput import filename
import os
import time

file_name = "log.txt"

def write_log(str):
    path = os.getcwd()+"\\"+file_name
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    out_str = time_str+"   "+str
    with open(path,'a',encoding='utf-8') as f:
        f.writelines(out_str)
        f.write('\n')

def init():
    path = os.getcwd()+"\\"+file_name
    if(os.path.isfile(path)):
        os.remove(path)