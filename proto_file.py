# support: hiramtan@live.com
import os
import config
import log

directory = config.proto_dir
extension = ".proto"

def get_files():
    log.debug("start get proto file")
    result = []
    g = os.walk(directory)
    for root, subFolder, files in g:
        for file in files:
            if file.endswith(extension):
                path = os.path.join(root, file)               
                result.append(path)
                str = "proto:"+path
                log.debug(str)
    return result
