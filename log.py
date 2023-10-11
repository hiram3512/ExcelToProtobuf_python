from fileinput import filename
import os
import time

def debug(str):
    file_name = time.strftime("%Y-%m-%d", time.localtime())+".txt"
    dir = os.getcwd()+"\\Logs"
    isExists = os.path.exists(dir)
    if not isExists:
        os.makedirs(dir)
    path = dir+"\\"+file_name
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    out_str = time_str+"   "+str
    with open(path,'a',encoding='utf-8') as f:
        f.writelines(out_str)
        f.write('\n')