import os
import config
import log
import common
import sys
import excel_parse
import shutil
import generate_intermediate
from google.protobuf.json_format import MessageToJson

extension = ".xlsx"

def get_files():
    log.write_log("get_files")
    result = []
    g = os.walk(config.excel_dir)
    for root, subFolder, files in g:
        for file in files:
            if file.endswith(extension):
                path = os.path.join(root, file)               
                result.append(path)
                str = "excel:"+path
                log.write_log(str)
    return result

def generate_intermediate_file():
    log.write_log("generate_intermediate_file")
    generate_intermediate.start()

def start_with_files(files):
    log.write_log("excel_to_data start_with_files")
    clean()
    generate_intermediate_file()
    for file in files:
        out_str = "start parse file:"+file
        log.write_log(out_str)
        base_name = os.path.basename(file)
        name_without_extension = os.path.splitext(base_name)[0]
        python_file_without_extension = name_without_extension+ "_pb2"
        python_file = os.getcwd()+"/"+common.temp_data_folder+"/"+name_without_extension+ "_pb2.py"
        if(os.path.isfile(python_file)):
            module_folder = common.temp_data_folder.replace("/",".")
            module_name = module_folder+"."+python_file_without_extension
            import_str = 'from '+module_name+ ' import *'
            exec(import_str)
            test_module = sys.modules[module_name]
            item_array = getattr(test_module, name_without_extension+"_Array")()
            item_array = excel_parse.get_item_array(file,item_array)            
            write_data_as_binary(name_without_extension,item_array)
            write_data_as_json(name_without_extension,item_array)
        else:
            error_str = "error: this excel can not find python language(check proto):"+file
            log.write_log(error_str)
    finish()

def write_data_as_binary(name,item_array):
    log.write_log("write_data_as_binary "+name)
    data = item_array.SerializeToString()
    path = config.auto_generate_data_dir+"/"+name+".bin"
    file = open(path, 'wb+')
    file.write(data)
    file.close()

def write_data_as_json(name,item_array):
    log.write_log("write_data_as_json "+name)
    str_with_default_value = MessageToJson(
        item_array,
        including_default_value_fields=True,
    )
    path = config.auto_generate_data_dir+"/"+name+".json"
    with open(path,'a',encoding='utf-8') as f:
        f.writelines(str_with_default_value)

def clean():
    log.write_log("excel_to_data clean")
    language_dir = config.auto_generate_language_dir
    isExists = os.path.exists(language_dir)
    if isExists:
        shutil.rmtree(language_dir, ignore_errors=True)
    os.makedirs(language_dir)

    data_dir = config.auto_generate_data_dir
    isExists = os.path.exists(data_dir)
    if isExists:
        shutil.rmtree(data_dir, ignore_errors=True)
    os.makedirs(data_dir)

    temp_dir = common.temp_data_folder
    isExists = os.path.exists(temp_dir)
    if isExists:
        shutil.rmtree(temp_dir, ignore_errors=True)
    os.makedirs(temp_dir)

def finish():
    log.write_log("excel_to_data finish")
    temp_dir = common.temp_data_folder
    isExists = os.path.exists(temp_dir)
    if isExists:
        shutil.rmtree(temp_dir, ignore_errors=True)
