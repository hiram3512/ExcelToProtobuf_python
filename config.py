import log
import os

excel_dir = os.getcwd()+"\Example\Excel"

proto_dir = os.getcwd()+"\Example\Proto"

auto_generate_language_dir = os.getcwd()+"\AutoGenerate_Language"

auto_generate_data_dir = os.getcwd()+"\AutoGenerate_Data"

def start():
    log.write_log("excel_dir:"+excel_dir)
    log.write_log("proto_dir:"+proto_dir)
    log.write_log("auto_generate_language_dir:"+auto_generate_language_dir)
    log.write_log("auto_generate_data_dir:"+auto_generate_data_dir)
