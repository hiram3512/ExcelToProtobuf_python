import log
import os
import proto_file
import config
from subprocess import Popen

def generate(proto_dir,proto_file,language_dir):
    str = "generate csharp language:"+proto_file
    log.write_log(str)
    protoc_exe = os.getcwd()+"/protoc.exe"
    Popen([protoc_exe, '-I', proto_dir, '--csharp_out', language_dir, proto_file],
      shell=False).wait()
def start():
    log.write_log("start csharp language")
    language_dir = config.auto_generate_language_dir+"/csharp"
    os.makedirs(language_dir)
    files = proto_file.get_files()
    for file in files:
        proto_dir = os.path.dirname(file)
        generate(proto_dir,file,language_dir)