import sys
import subprocess
import psutil
import win32gui
import win32con
from pynput import keyboard
from enum import IntEnum
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets


class Language(IntEnum):
    ENG = 0
    RU = 1


class NumKeys(str, Enum):
    NUM0 = '<96>'
    NUM1 = '<97>'
    NUM2 = '<98>'
    NUM3 = '<99>'
    NUM4 = '<100>'
    NUM5 = '<101>'


class RocketTypeArg(str, Enum):
    HV = '-hvr'  # High velocity rocket
    INC = '-ir'  # Incedinary rocket
    EXP = '-er'  # Explosive rocket


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
        self.comboBox_lang.setItemText(0, _translate("MainWindow", "Eng"))
        self.comboBox_lang.setItemText(1, _translate("MainWindow", "Ru"))
        self.label_warning.setText(_translate("MainWindow", "{only_for_fixed_resolution}"))
        self.groupBox_hotkeys_info.setTitle(_translate("MainWindow", "{hotkeys_info}"))
        self.label_sh_sr.setText(_translate("MainWindow", "NUMPAD 3 - {show_simple_rocketsight}"))
        self.label_hide.setText(_translate("MainWindow", "NUMPAD 0 - {hide_sight}"))
        self.label_sh_inr.setText(_translate("MainWindow", "NUMPAD 2 - {show_incedinary_rocketsight}"))
        self.label_sh_hvr.setText(_translate("MainWindow", "NUMPAD 1 - {show_high_velocity_rocketsight}"))
        self.label_ch_color.setText(_translate("MainWindow", "NUMPAD 4 - {change_color}"))
        self.label_minimize.setText(_translate("MainWindow", "NUMPAD 5 - {minimize_rust_window}"))
        self.label_contact_info.setText(_translate("MainWindow", "{cotact_info}"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_lang.activated[str].connect(self.onLangChanged)
        self.refreshLocalization()

    def refreshLocalization(self):
        self.ui.groupBox_hotkeys_info.setTitle(Localization.getText("hotkeys_info"))
        self.ui.label_hide.setText("NUMPAD 0 - " + Localization.getText("hide_sight"))
        self.ui.label_sh_hvr.setText("NUMPAD 1 - " + Localization.getText("show_high_velocity_rocketsight"))
        self.ui.label_sh_inr.setText("NUMPAD 2 - " + Localization.getText("show_incedinary_rocketsight"))
        self.ui.label_sh_sr.setText("NUMPAD 3 - " + Localization.getText("show_simple_rocketsight"))
        self.ui.label_ch_color.setText("NUMPAD 4 - " + Localization.getText("change_color"))
        self.ui.label_minimize.setText("NUMPAD 5 - " + Localization.getText("minimize_rust_window"))
        self.ui.label_warning.setText(Localization.getText("only_for_fixed_resolution"))
        self.ui.label_contact_info.setText(Localization.getText("cotact_info"))

    def onLangChanged(self, text):
        if text == 'Eng':
            Localization.LANG = Language.ENG
        else:
            Localization.LANG = Language.RU
        self.refreshLocalization()


class Coordinator():
    active_proc_id = None
    sight_hidden = True
    sight_hvr_displayed = False
    sight_ir_displayed = False
    sight_er_displayed = False

    developer_mode = False
    rust_window_minimized = False
    rust_window_id = None

    def numpad_on_press(key):
        if str(key) == NumKeys.NUM0:
            Coordinator.hide_all()
        elif str(key) == NumKeys.NUM1:
            Coordinator.show_hvr_sight()
        elif str(key) == NumKeys.NUM2:
            Coordinator.show_ir_sight()
        elif str(key) == NumKeys.NUM3:
            Coordinator.show_er_sight()
        elif str(key) == NumKeys.NUM4:
            pass
        elif str(key) == NumKeys.NUM5:
            Coordinator.minimize_rust_window()

    def detect_developer_mode():
        script_path_splitted = sys.argv[0].split('\\')
        script_name = script_path_splitted[len(script_path_splitted) - 1]
        if script_name.split('.')[1] == 'pyw':
            Coordinator.developer_mode = True
        else:
            Coordinator.developer_mode = False

    def get_script_fullname(name):
        Coordinator.detect_developer_mode()
        if Coordinator.developer_mode:
            return name + '.pyw'
        else:
            return name + '.exe'

    def kill(proc_pid):
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()

    # rocket_type values: -hv, -i or empty for simple rocket sight
    def run_sub_script(rocket_type_arg):
        scr_f_name = Coordinator.get_script_fullname('hvrsight')
        proc = subprocess.Popen(['python', scr_f_name, rocket_type_arg.value], shell=True)
        Coordinator.active_proc_id = proc.pid

    def show_hvr_sight():
        if Coordinator.sight_hvr_displayed:
            return
        Coordinator.hide_all()
        Coordinator.sight_hvr_displayed = True
        Coordinator.run_sub_script(RocketTypeArg.HV)

    def show_ir_sight():
        if Coordinator.sight_ir_displayed:
            return
        Coordinator.hide_all()
        Coordinator.sight_ir_displayed = True
        Coordinator.run_sub_script(RocketTypeArg.INC)

    def show_er_sight():
        if Coordinator.sight_er_displayed:
            return
        Coordinator.hide_all()
        Coordinator.sight_er_displayed = True
        Coordinator.run_sub_script(RocketTypeArg.EXP)

    def hide_all():
        if Coordinator.active_proc_id:
            Coordinator.kill(Coordinator.active_proc_id)
            Coordinator.active_proc_id = None
            Coordinator.sight_hvr_displayed = False
            Coordinator.sight_ir_displayed = False
            Coordinator.sight_er_displayed = False

    def minimize_rust_window():
        whnd = win32gui.FindWindowEx(None, None, None, 'Rust')
        if not whnd or win32gui.GetWindowPlacement(whnd)[2][0] == -1:
            return
        win32gui.ShowWindow(whnd, win32con.SW_MINIMIZE)

class Localization:
    LANG = Language.ENG
    textmsg = {
        "hide_sight": [
            "Hide sight alignment",
            "Скрыть прицел для ракетницы"
        ],
        "show_high_velocity_rocketsight": [
            "Show hight velocity rocket sight",
            "Показать прицел для ракет большой дальности"
        ],
        "show_incedinary_rocketsight": [
            "Show incedinary rocket sight",
            "Показать прицел для зажигательных ракет"
        ],
        "stop_any_action": [
            "Stop any action",
            "Остановить все текущие действия"
        ],
        "hotkeys_info": [
            "Hotkeys",
            "Горячие клавиши"
        ],
        "show_simple_rocketsight": [
            "Sight alignment for regular rocket",
            "Прицел для обычных ракет"
        ],
        "change_color": [
            "Change sight color",
            "Изменить цвет прицела"
        ],
        "minimize_rust_window": [
            "Minimize Rust window",
            "Свернуть окно игры"
        ],
        "only_for_fixed_resolution": [
            "[!] Coordinator works correctly only with 1920x1080 resolution and with borderless window mode",
            "[!] Программа работает корректно только с разрешением экрана 1920x1080 и при оконном режиме Borderless(без рамки)"
        ],
        "cotact_info": [
            "My concacts: andreyperepelytsaaa@gmail.com \nGithub: https://github.com/agdeon",
            "Связь со мной: andreyperepelytsaaa@gmail.com\nGithub: https://github.com/agdeon"
        ]
    }

    def getText(msg_code):
        return Localization.textmsg[msg_code][Localization.LANG]


def main():
    numpad_listener = keyboard.Listener(on_press=Coordinator.numpad_on_press)
    numpad_listener.start()

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    exit_code = app.exec()
    Coordinator.hide_all()
    sys.exit(exit_code)

if __name__ == '__main__':
    main()