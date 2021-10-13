import os
from PyQt5.QtCore import Qt
import tag
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
import shutil
from PyQt5.QtGui import QImage, QPixmap
import cv2 as cv
import glob


class MainCode(QWidget, tag.Ui_MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        tag.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_27.clicked.connect(self.select_source_folder)
        self.pushButton_33.clicked.connect(self.select_save_folder)

        self.pushButton.clicked.connect(lambda: self.move_files('Good'))
        self.pushButton_2.clicked.connect(lambda: self.move_files('ITO'))
        self.pushButton_3.clicked.connect(lambda: self.move_files('Epitaxy'))
        self.pushButton_4.clicked.connect(lambda: self.move_files('EdgeDefect'))
        self.pushButton_5.clicked.connect(lambda: self.move_files('EdgeAbnormal'))
        self.pushButton_6.clicked.connect(lambda: self.move_files('EtroThinL1'))
        self.pushButton_7.clicked.connect(lambda: self.move_files('Mark'))
        self.pushButton_8.clicked.connect(lambda: self.move_files('ColorDif'))
        self.pushButton_9.clicked.connect(lambda: self.move_files('DarkL1'))
        self.pushButton_10.clicked.connect(lambda: self.move_files('MulGoldEtroL4'))
        self.pushButton_11.clicked.connect(lambda: self.move_files('MulGoldL1'))
        self.pushButton_12.clicked.connect(lambda: self.move_files('MulGoldL4'))
        self.pushButton_13.clicked.connect(lambda: self.move_files('Scratch'))
        self.pushButton_14.clicked.connect(lambda: self.move_files('TwoConnectL2'))
        self.pushButton_15.clicked.connect(lambda: self.move_files('TwoConnectL4'))
        self.pushButton_18.clicked.connect(lambda: self.move_files('PV'))
        self.pushButton_19.clicked.connect(lambda: self.move_files('Needle'))
        self.pushButton_20.clicked.connect(lambda: self.move_files('MESA'))
        self.pushButton_21.clicked.connect(lambda: self.move_files('Misalign'))
        self.pushButton_22.clicked.connect(lambda: self.move_files('MulGoldEtroL2'))
        self.pushButton_23.clicked.connect(lambda: self.move_files('EtroThinL2'))
        self.pushButton_24.clicked.connect(lambda: self.move_files('EtroThinL4'))
        self.pushButton_25.clicked.connect(lambda: self.move_files('DirtyL1'))
        self.pushButton_28.clicked.connect(lambda: self.move_files('EtroDirtyL1'))
        self.pushButton_29.clicked.connect(lambda: self.move_files('EtroMiss'))
        self.pushButton_30.clicked.connect(lambda: self.move_files('MulGoldEtroL1'))
        self.pushButton_31.clicked.connect(lambda: self.move_files('DirtyL2'))
        self.pushButton_32.clicked.connect(lambda: self.move_files('DirtyL4'))
        self.pushButton_16.clicked.connect(self.delete_file)

        # self.pushButton_17.clicked.connect(self.next_file)
        self.pushButton_26.clicked.connect(self.next_file)

        self.n = 0
        self.label_4.setText(str(self.n))

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.next_file()

        if event.key() == 16777223:
            self.delete_file()


    def select_source_folder(self):
        self.so_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "/")
        self.label_2.setText(self.so_directory)
        self.file_lists = glob.glob(self.so_directory + '/*')
        self.show_img(self.file_lists[self.n])

    def select_save_folder(self):
        self.sa_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "/")
        self.label_3.setText(self.sa_directory)

    def move_files(self, file):
        self.show_img(self.file_lists[self.n])
        shutil.move(self.file_lists[self.n], self.sa_directory + '/' + file)
        self.n = self.n + 1
        self.label_4.setText(str(self.n))
        self.show_img(self.file_lists[self.n])

    def delete_file(self):
        os.remove(self.file_lists[self.n])
        self.n = self.n + 1
        self.label_4.setText(str(self.n))
        self.show_img(self.file_lists[self.n])

    def next_file(self):
        self.n = self.n + 1
        self.label_4.setText(str(self.n))
        self.show_img(self.file_lists[self.n])

    def show_img(self, file_path):
        self.img = cv.imread(file_path, 3)
        self.img = cv.resize(self.img, (0, 0), fx=4, fy=4)

        self.QImg = QImage(self.img[:], self.img.shape[1], self.img.shape[0], self.img.shape[1] * 3,
                           QImage.Format_RGB888)

        self.label.setPixmap(QPixmap(self.QImg))
