# support: hiramtan@live.com
import log
import os
import proto_file
import config
from subprocess import Popen

def generate(proto_dir,proto_file,language_dir):
    str = "generate cpp language:"+proto_file
    log.debug(str)
    protoc_exe = os.getcwd()+"/protoc.exe"
    Popen([protoc_exe, '-I', proto_dir, '--cpp_out', language_dir, proto_file],
      shell=False).wait()
def start():
    log.debug("start cpp language")
    language_dir = config.auto_generate_language_dir+"/cpp"
    os.makedirs(language_dir)
    files = proto_file.get_files()
    for file in files:
        proto_dir = os.path.dirname(file)
        generate(proto_dir,file,language_dir)