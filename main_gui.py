# support: hiramtan@live.com

import main
import log
import config
import excel_to_data
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QFileDialog, QGridLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):       
        self.all_excel_files = excel_to_data.get_files()
        self.selected_excel_files = self.all_excel_files

        grid = QGridLayout()
        grid.setSpacing(10)

        self.dir_excel = QLabel(config.excel_dir)
        dir_excel_button = QPushButton("Select", self)
        dir_excel_button.clicked.connect(self.dir_excel_button_clicked)
        grid.addWidget(QLabel("Excel Folder:"), 1, 0)
        grid.addWidget(self.dir_excel, 1, 1)
        grid.addWidget(dir_excel_button, 1, 2)

        self.dir_proto=QLabel(config.proto_dir)
        dir_proto_button = QPushButton("Select", self)
        dir_proto_button.clicked.connect(self.dir_proto_button_clicked)
        grid.addWidget(QLabel("Proto Folder:"), 2, 0)
        grid.addWidget(self.dir_proto, 2, 1)
        grid.addWidget(dir_proto_button, 2, 2)

        self.export_language=QLabel(config.auto_generate_language_dir)
        export_language_button = QPushButton("Select", self)
        export_language_button.clicked.connect(self.export_language_button_clicked)
        grid.addWidget(QLabel("Export Language Folder:"), 3, 0)
        grid.addWidget(self.export_language, 3, 1)
        grid.addWidget(export_language_button, 3, 2)

        self.export_data=QLabel(config.auto_generate_data_dir)
        export_data_button = QPushButton("Select", self)
        export_data_button.clicked.connect(self.export_data_button_clicked)
        grid.addWidget(QLabel("Export Data Folder:"), 4, 0)
        grid.addWidget(self.export_data, 4, 1)
        grid.addWidget(export_data_button, 4, 2)

        #########################
        button_select_all = QPushButton("Select All", self)
        button_select_all.clicked.connect(self.select_all_button_clicked)
        button_unselect_all = QPushButton("Unselect All", self)
        button_unselect_all.clicked.connect(self.unselect_all_button_clicked)
        button_export = QPushButton("Export", self)
        button_export.clicked.connect(self.export_button_clicked)
        grid.addWidget(button_select_all, 5, 0)
        grid.addWidget(button_unselect_all, 5, 1)
        grid.addWidget(button_export, 5, 2)

        #########################
        self.scroll = QtWidgets.QScrollArea()
        self.update_scroll_area_widget()
        grid.addWidget(self.scroll,6,0,1,3)
        self.setLayout(grid)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Convert tool')
        self.show()
    
    # 目录选择
    def dir_excel_button_clicked(self, n):
        folder_selected = QFileDialog.getExistingDirectory()
        config.excel_dir = folder_selected
        self.dir_excel.setText(config.excel_dir)
        self.all_excel_files = excel_to_data.get_files()
        self.selected_excel_files = self.all_excel_files
        self.update_scroll_area_widget()
        for checkbox in self.all_checkbox:
            checkbox.setChecked(True)

    def dir_proto_button_clicked(self, n):
        folder_selected = QFileDialog.getExistingDirectory()
        config.dir_proto = folder_selected
        self.dir_proto.setText(config.dir_proto)

    def export_language_button_clicked(self, n):
        folder_selected = QFileDialog.getExistingDirectory()
        config.auto_generate_language_dir = folder_selected
        self.export_language.setText(config.auto_generate_language_dir)

    def export_data_button_clicked(self, n):
        folder_selected = QFileDialog.getExistingDirectory()
        config.auto_generate_data_dir = folder_selected
        self.export_data.setText(config.auto_generate_data_dir)

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

    def excel_file_checkbox(self):
        self.selected_excel_files = []
        for checkbox in self.all_checkbox:
            if checkbox.isChecked() :
                name = checkbox.text()
                self.selected_excel_files.append(name)

    def update_scroll_area_widget(self):
        self.all_checkbox = []
        groupBox = QtWidgets.QGroupBox()
        self.scroll.setWidget(groupBox)
        self.scroll.widget
        self.scroll.setWidgetResizable(True)
        groupLayout = QtWidgets.QGridLayout(groupBox)
        for row in range(len(self.all_excel_files)):
            name = self.all_excel_files[row]
            checkbox = QtWidgets.QCheckBox(name)
            checkbox.setChecked(True)
            self.all_checkbox.append(checkbox)
            checkbox.toggled.connect(self.excel_file_checkbox)
            groupLayout.addWidget(checkbox, row, 0)

def start_windows():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

def start():
    log.init()
    log.write_log("main start")
    config.start()
    start_windows()

start()