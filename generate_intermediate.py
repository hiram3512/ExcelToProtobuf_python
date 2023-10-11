import log
import shutil
import os
import proto_file
import common
import config
from subprocess import Popen

def generate_python(proto_dir,proto_file,temp_dir):
    str = "generate python and pb:"+proto_file
    log.debug(str)
    protoc_exe = os.getcwd()+"/protoc.exe"
    Popen([protoc_exe, '-I', proto_dir, '--python_out', temp_dir, proto_file],
      shell=False).wait()

def generate_pb(proto_dir,proto_file):
    protoc_exe = os.getcwd()+"/protoc.exe"
    base_name = os.path.basename(proto_file)
    name_without_extension = os.path.splitext(base_name)[0]
    pb_file_name = name_without_extension+".pb"
    pb_file = config.auto_generate_data_dir+"/"+pb_file_name
    Popen([protoc_exe, '-I', proto_dir, '-o', pb_file, proto_file],
      shell=False).wait()

def start():
    log.debug("start generate_intermediate")
    temp_dir = os.getcwd()+"/"+common.temp_data_folder
    isExists = os.path.exists(temp_dir)
    if isExists:
        shutil.rmtree(temp_dir, ignore_errors=True)
    os.makedirs(temp_dir)

    files = proto_file.get_files()
    for file in files:
        proto_dir = os.path.dirname(file)
        generate_python(proto_dir,file,temp_dir)
        generate_pb(proto_dir,file)