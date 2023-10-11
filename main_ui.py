# support: hiramtan@live.com

import main
import log
import config
import excel_to_data
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog,QListWidgetItem
from dialog_ui import Ui_Dialog
class MainUI(QWidget,Ui_Dialog):
    def __init__(self,parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_ExcelFolder.clicked.connect(self.dir_excel_button_clicked)
        self.pushButton_ProtoFolder.clicked.connect(self.dir_proto_button_clicked)
        self.pushButton_LanguageFolder.clicked.connect(self.export_language_button_clicked)
        self.pushButton_DataFolder.clicked.connect(self.export_data_button_clicked)
        self.pushButton_SelectAll.clicked.connect(self.select_all_button_clicked)
        self.pushButton_UnselectAll.clicked.connect(self.unselect_all_button_clicked)
        self.pushButton_Export.clicked.connect(self.export_button_clicked)

        self.lineEdit_ExcelFolder.setText(config.excel_dir)
        self.lineEdit_ProtoFolder.setText(config.proto_dir)
        self.lineEdit_LanguageFolder.setText(config.auto_generate_language_dir)
        self.lineEdit_DataFolder.setText(config.auto_generate_data_dir)
        
        self.all_excel_files = excel_to_data.get_files()
        self.selected_excel_files = self.all_excel_files
        self.update_scroll_area_widget()

    # 目录选择
    def dir_excel_button_clicked(self):
        folder_selected = QFileDialog.getExistingDirectory()
        config.excel_dir = folder_selected
        self.lineEdit_ExcelFolder.setText(config.excel_dir)
        self.all_excel_files = excel_to_data.get_files()
        self.selected_excel_files = self.all_excel_files
        self.update_scroll_area_widget()

    def dir_proto_button_clicked(self):
        folder_selected = QFileDialog.getExistingDirectory()
        config.proto_dir = folder_selected
        self.lineEdit_ProtoFolder.setText(config.proto_dir)

    def export_language_button_clicked(self):
        folder_selected = QFileDialog.getExistingDirectory()
        config.auto_generate_language_dir = folder_selected
        self.lineEdit_LanguageFolder.setText(config.auto_generate_language_dir)

    def export_data_button_clicked(self):
        folder_selected = QFileDialog.getExistingDirectory()
        config.auto_generate_data_dir = folder_selected
        self.lineEdit_DataFolder.setText(config.auto_generate_data_dir)

    # excel文件选择
    def select_all_button_clicked(self):
        self.selected_excel_files = self.all_excel_files
        for checkbox in self.all_checkbox:
            checkbox.setChecked(True)
    
    def unselect_all_button_clicked(self):
        self.selected_excel_files = []
        for checkbox in self.all_checkbox:
            checkbox.setChecked(False)

    def export_button_clicked(self):
        main.start_with_excel_files(self.selected_excel_files)
        self.label_log.setText("finish")

    def excel_file_checkbox(self):
        self.selected_excel_files = []
        for checkbox in self.all_checkbox:
            if checkbox.isChecked() :
                name = checkbox.text()
                self.selected_excel_files.append(name)

    def update_scroll_area_widget(self):
        self.all_checkbox = []  
        self.listWidget.clear()
        for row in range(len(self.all_excel_files)):
            name = self.all_excel_files[row]            
            checkbox = QtWidgets.QCheckBox(name)
            checkbox.setChecked(True)
            self.all_checkbox.append(checkbox)
            item = QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,checkbox)
            
if __name__ == "__main__":  
    log.debug("start")
    config.start()
    app = QApplication(sys.argv) 
    main_ui = MainUI()
    main_ui.show()
    sys.exit(app.exec())