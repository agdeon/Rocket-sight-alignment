from PyQt5 import QtCore, QtGui, QtWidgets
from projectStructures import Localization

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Rocket sight alignment")
        MainWindow.resize(633, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_lang = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_lang.setGeometry(QtCore.QRect(560, 260, 61, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_lang.setFont(font)
        self.comboBox_lang.setObjectName("comboBox_lang")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.label_warning = QtWidgets.QLabel(self.centralwidget)
        self.label_warning.setGeometry(QtCore.QRect(10, 180, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_warning.setFont(font)
        self.label_warning.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_warning.setTextFormat(QtCore.Qt.AutoText)
        self.label_warning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_warning.setWordWrap(True)
        self.label_warning.setObjectName("label_warning")
        self.groupBox_hotkeys_info = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_hotkeys_info.setGeometry(QtCore.QRect(10, 10, 531, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_hotkeys_info.setFont(font)
        self.groupBox_hotkeys_info.setObjectName("groupBox_hotkeys_info")
        self.label_sh_sr = QtWidgets.QLabel(self.groupBox_hotkeys_info)
        self.label_sh_sr.setGeometry(QtCore.QRect(10, 90, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_sh_sr.setFont(font)
        self.label_sh_sr.setObjectName("label_sh_sr")
        self.label_hide = QtWidgets.QLabel(self.groupBox_hotkeys_info)
        self.label_hide.setGeometry(QtCore.QRect(10, 30, 691, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_hide.setFont(font)
        self.label_hide.setObjectName("label_hide")
        self.label_sh_inr = QtWidgets.QLabel(self.groupBox_hotkeys_info)
        self.label_sh_inr.setGeometry(QtCore.QRect(10, 70, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_sh_inr.setFont(font)
        self.label_sh_inr.setObjectName("label_sh_inr")
        self.label_sh_hvr = QtWidgets.QLabel(self.groupBox_hotkeys_info)
        self.label_sh_hvr.setGeometry(QtCore.QRect(10, 50, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_sh_hvr.setFont(font)
        self.label_sh_hvr.setObjectName("label_sh_hvr")
        self.label_ch_color = QtWidgets.QLabel(self.groupBox_hotkeys_info)
        self.label_ch_color.setGeometry(QtCore.QRect(10, 110, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch_color.setFont(font)
        self.label_ch_color.setObjectName("label_ch_color")
        self.label_minimize = QtWidgets.QLabel(self.groupBox_hotkeys_info)
        self.label_minimize.setGeometry(QtCore.QRect(10, 130, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_minimize.setFont(font)
        self.label_minimize.setObjectName("label_minimize")
        self.label_contact_info = QtWidgets.QLabel(self.centralwidget)
        self.label_contact_info.setGeometry(QtCore.QRect(10, 240, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_contact_info.setFont(font)
        self.label_contact_info.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_contact_info.setTextFormat(QtCore.Qt.AutoText)
        self.label_contact_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_contact_info.setWordWrap(True)
        self.label_contact_info.setObjectName("label_contact_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rocket sight alignment"))
        self.comboBox_lang.setItemText(0, _translate("MainWindow", "En"))
        self.comboBox_lang.setItemText(1, _translate("MainWindow", "Ru"))
        self.comboBox_lang.setCurrentIndex(Localization.current_lang)
        self.label_warning.setText(_translate("MainWindow", "{only_for_fixed_resolution}"))
        self.groupBox_hotkeys_info.setTitle(_translate("MainWindow", "{hotkeys_info}"))
        self.label_sh_sr.setText(_translate("MainWindow", "NUMPAD 3 - {show_simple_rocketsight}"))
        self.label_hide.setText(_translate("MainWindow", "NUMPAD 0 - {hide_sight}"))
        self.label_sh_inr.setText(_translate("MainWindow", "NUMPAD 2 - {show_incedinary_rocketsight}"))
        self.label_sh_hvr.setText(_translate("MainWindow", "NUMPAD 1 - {show_high_velocity_rocketsight}"))
        self.label_ch_color.setText(_translate("MainWindow", "NUMPAD 4 - {change_color}"))
        self.label_minimize.setText(_translate("MainWindow", "NUMPAD 5 - {minimize_rust_window}"))
        self.label_contact_info.setText(_translate("MainWindow", "{cotact_info}"))


class RSAppWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(RSAppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_lang.activated[int].connect(self.onLangChanged)
        self.refreshLocalization()

    def refreshLocalization(self):
        self.ui.groupBox_hotkeys_info.setTitle(Localization.get_text("hotkeys_info"))
        self.ui.label_hide.setText(f'NUMPAD 0 - {Localization.get_text("hide_sight")}')
        self.ui.label_sh_hvr.setText(f'NUMPAD 1 - {Localization.get_text("show_high_velocity_rocketsight")}')
        self.ui.label_sh_inr.setText(f'NUMPAD 2 - {Localization.get_text("show_incedinary_rocketsight")}')
        self.ui.label_sh_sr.setText(f'NUMPAD 3 - {Localization.get_text("show_simple_rocketsight")}')
        self.ui.label_ch_color.setText(f'NUMPAD 4 - {Localization.get_text("change_color")}')
        self.ui.label_minimize.setText(f'NUMPAD 5 - {Localization.get_text("minimize_rust_window")}')
        self.ui.label_warning.setText(Localization.get_text("only_for_fixed_resolution"))
        self.ui.label_contact_info.setText(Localization.get_text("cotact_info"))

    def onLangChanged(self, lang_index):
        Localization.current_lang = lang_index
        self.refreshLocalization()

