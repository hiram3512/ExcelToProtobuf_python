# support: hiramtan@live.com
import os
import time
from pydispatch import dispatcher

def debug(msg):
    file_name = time.strftime("%Y-%m-%d", time.localtime()) + ".txt"
    dir = os.getcwd() + "\\Logs"
    isExists = os.path.exists(dir)
    if not isExists:
        os.makedirs(dir)
    path = dir + "\\" + file_name
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    out_str = time_str + "   " + msg
    dispatcher.send(message=out_str, signal='log')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(out_str + '\n')