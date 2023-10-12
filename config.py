# support: hiramtan@live.com
import log
import os

excel_dir = os.getcwd()+"\Example\Excel"
proto_dir = os.getcwd()+"\Example\Proto"
auto_generate_language_dir = os.getcwd()+"\Example\AutoGenerate_Language"
auto_generate_data_dir = os.getcwd()+"\Example\AutoGenerate_Data"

def start():
    log.debug("excel_dir:"+excel_dir)
    log.debug("proto_dir:"+proto_dir)
    log.debug("auto_generate_language_dir:"+auto_generate_language_dir)
    log.debug("auto_generate_data_dir:"+auto_generate_data_dir)
