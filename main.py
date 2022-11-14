# support: hiramtan@live.com

import log
import config
import excel_to_data
import language_generate_python
import language_generate_cpp
import language_generate_csharp
import language_generate_java

# this called from ui export button
def start_with_excel_files(files):
    log.write_log("main start_with_excel_files")
    excel_to_data.start_with_files(files)
    log.write_log("main generate_language")
    language_generate_python.start()
    language_generate_cpp.start()
    language_generate_csharp.start()
    language_generate_java.start()

    #generate other language here
    log.write_log("main finish")

# this will called from CI
def start():
    log.init()
    log.write_log("main start")
    config.start()
    files = excel_to_data.get_files()
    start_with_excel_files(files)
