from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog
from PyQt5.QtCore import Qt
from ex.autopptx_ui import *
from ex import autopptx
from tkinter import filedialog
import sys
import tkinter
import os


root = tkinter.Tk()
root.withdraw()

# 创建GUI


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.name = ""
        self.ui.spinBox.setMinimum(1)
        self.show()
        # 修订代码
        self.ui.radioButton.toggled.connect(
            lambda: self.edit_show(self.ui.radioButton))
        self.ui.radioButton_2.toggled.connect(
            lambda: self.edit_show(self.ui.radioButton_2))
        self.ui.radioButton_3.toggled.connect(
            lambda: self.edit_show(self.ui.radioButton_3))
        self.ui.lineEdit.editingFinished.connect(
            lambda: self.edit_show(self.ui.lineEdit))
        self.ui.spinBox.valueChanged.connect(
            lambda: self.edit_show(self.ui.spinBox))
        self.ui.pushButton_2.clicked.connect(lambda: self.choose_file())
        self.ui.pushButton.clicked.connect(
            lambda: self.edit_show(self.ui.spinBox))
        self.ui.pushButton.clicked.connect(lambda: self.creatpptx())

    # 获取控件的内容

    def edit_show(self, widget):
        if widget == self.ui.lineEdit:
            self.name = widget.text()
        elif widget == self.ui.spinBox:
            self.index = self.ui.spinBox.value()
        elif widget == self.ui.radioButton:
            self.value = 1
        elif widget == self.ui.radioButton_2:
            self.value = 2
        elif widget == self.ui.radioButton_3:
            self.value = 3

    # 选择文件
    def choose_file(self):
        if self.ui.radioButton_4.isChecked():
            self.file_paths = filedialog.askopenfilenames(
                title='选择音乐', filetypes=[('音频', '.mp3')])
            self.show_name('.mp3')
        elif self.ui.radioButton_5.isChecked():
            self.file_paths = filedialog.askopenfilenames(
                title='选择视频', filetypes=[('视频', '.mp4')])
            self.show_name('.mp4')

    def creatpptx(self):
        if self.ui.radioButton_4.isChecked():
            self.files = [self.file_paths[i:i+self.value]
                          for i in range(0, len(self.file_paths), self.value)]
            progress = QProgressDialog(self)
            progress.setWindowTitle("请稍等")
            progress.setLabelText("正在操作...")
            progress.setCancelButtonText("取消")
            # progress.setMinimumDuration(5)
            progress.setWindowModality(Qt.WindowModal)
            progress.setRange(0, len(self.files))
            for index, filepath in enumerate(self.files):
                name = self.name+str(self.index)
                autopptx.audio(filepath=filepath, name=name)
                self.index += 1
                progress.setValue(index+1)
        elif self.ui.radioButton_5.isChecked():
            filepath = self.file_paths[0]
            name = self.name + str(self.index)
            autopptx.movie(filepath=filepath, name=name)

    def show_name(self, extend):
        for file in self.file_paths:
            self.ui.textBrowser.append(
                os.path.basename(file).replace(extend, ''))
            self.cursot = self.ui.textBrowser.textCursor()
            self.ui.textBrowser.moveCursor(self.cursot.End)
            QApplication.processEvents()


# 创建程序对象
app = QApplication(sys.argv)
window = Window()
# msg_box = QMessageBox.about(None,  , )
# 消息循环
sys.exit(app.exec_())
