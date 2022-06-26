from PyQt5 import QtCore, QtGui, QtWidgets
#from virtual_mouse import *
import sys
import down_rc
import gesture_rc
import leftc_rc
import ls_rc
import up_rc
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1054, 633)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(720, 60, 171, 221))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 291, 111))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 300, 211, 111))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(120, 300, 171, 111))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 391, 111))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 480, 341, 111))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 90, 171, 181))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(500, 440, 161, 201))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(720, 290, 171, 191))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 290, 181, 181))
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(360, -40, 661, 151))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(850, 540, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.start_camera)

    def start_camera(self):
        obj1 = hand_detect()
        obj1.main()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Virtual Mouse"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix6/up.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Curser Up Shift </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Right Click</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Left Click </span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Curser Right Shift </span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Curser Down Shift </span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix1/right_shif.png\"/></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix3/down.png\"/></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix23/right_click.png\"/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefixlc/left.png\"/></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">Virtual Mouse Gestures</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Start Gesture"))

import down_rc
import gesture_rc
import leftc_rc
import ls_rc
import up_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


