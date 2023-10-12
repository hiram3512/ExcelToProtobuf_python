# support: hiramtan@live.com
import sys
import log
import config
from PyQt6.QtWidgets import QApplication
from dialog_ui_proxyer import MainUI

if __name__ == "__main__":  
    log.debug("start")
    config.start()
    app = QApplication(sys.argv) 
    main_ui = MainUI()
    main_ui.show()
    sys.exit(app.exec())