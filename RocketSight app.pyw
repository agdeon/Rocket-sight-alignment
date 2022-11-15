import sys
import psutil
import win32gui
import win32con
from pynput import keyboard
from PyQt5 import QtCore, QtGui, QtWidgets
from appUI import RSAppWindow
from projectStructures import NumKeys, RocketTypeArg
from rsdisplay import RocketSight

# Main process coordinator
class Coordinator():

    def __init__(self):
        self.active_proc = None
        self.sight_hidden = True
        self.sight_hvr_displayed = False
        self.sight_ir_displayed = False
        self.sight_er_displayed = False

        self.developer_mode = False
        self.rust_window_minimized = False
        self.rust_window_id = None


    def create_numpad_listener(self):
        numpad_listener = keyboard.Listener(on_press=self.numpad_on_press)
        numpad_listener.start()

    def numpad_on_press(self, key):
        if str(key) == NumKeys.NUM0:
            self.hide_sight()
        elif str(key) == NumKeys.NUM1:
            self.show_hvr_sight()
        elif str(key) == NumKeys.NUM2:
            self.show_ir_sight()
        elif str(key) == NumKeys.NUM3:
            self.show_er_sight()
        elif str(key) == NumKeys.NUM4:
            pass
        elif str(key) == NumKeys.NUM5:
            self.minimize_rust_window()

    def create_rocketsight_manager_process(self):
        pass

    def display_main_window(self):
        app = QtWidgets.QApplication([])
        application = RSAppWindow()
        application.show()
        exit_code = app.exec()
        self.hide_sight()
        sys.exit(exit_code)

    def detect_developer_mode(self):
        script_path_splitted = sys.argv[0].split('\\')
        script_name = script_path_splitted[len(script_path_splitted) - 1]
        if script_name.split('.')[1] == 'pyw':
            self.developer_mode = True
        else:
            self.developer_mode = False

    def get_script_fullname(self, name):
        self.detect_developer_mode()
        if self.developer_mode:
            return name + '.pyw'
        else:
            return name + '.exe'

    def kill_subproc(self):
        self.get_script_fullname('scale')
        for proc in psutil.process_iter():
            print(proc.name())
            if proc.name() == self.get_script_fullname('scale'):
                proc.kill()

    def show_hvr_sight(self):
        if self.sight_hvr_displayed:
            return
        self.hide_sight()
        self.sight_hvr_displayed = True
        self.create_scale()

    def show_ir_sight(self):
        if self.sight_ir_displayed:
            return
        self.hide_sight()
        self.sight_ir_displayed = True
        self.run_sub_script(RocketTypeArg.INC)

    def show_er_sight(self):
        if self.sight_er_displayed:
            return
        self.sight_er_displayed = True
        self.create_rs_subprocess(RocketTypeArg.EXP)

    def hide_sight(self):
        if self.active_proc:
            self.active_proc.terminate()
            self.sight_er_displayed = False
            self.active_proc = None

    def minimize_rust_window(self):
        whnd = win32gui.FindWindowEx(None, None, None, 'Rust')
        if win32gui.GetWindowText(whnd) == 'Rust':
            win32gui.ShowWindow(whnd, win32con.SW_MINIMIZE)

    def create_rs_subprocess(self, rocket_type):
        if self.active_proc:
            self.active_proc.terminate()
            self.active_proc = None
        self.active_proc = RocketSight.run_subprocess(rocket_type)

def main():
    coordinator = Coordinator()
    coordinator.create_numpad_listener()
    coordinator.display_main_window()

if __name__ == '__main__':
    main()