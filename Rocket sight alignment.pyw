import sys
import multiprocessing
from multiprocessing import Process
import psutil
import win32gui
import win32con
from pynput import keyboard
from enum import IntEnum
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets
from rsaUI import MainWindow
from ProjectStructures import NumKeys, RocketTypeArg, Language, Localization

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

    def kill_subproc():
        Coordinator.get_script_fullname('scale')
        for proc in psutil.process_iter():
            print(proc.name())
            if proc.name() == Coordinator.get_script_fullname('scale'):
                proc.kill()

        # process = psutil.Process(proc_pid)
        # for proc in process.children(recursive=True):
        #      proc.kill()
        # process.kill()

    # rocket_type values: -hv, -i or empty for simple rocket sight
    def run_sub_proc(rocket_type_arg):
        proc = Process(target=f, args=('bob',))

        # scr_f_name = Coordinator.get_script_fullname('scale')
        # if Coordinator.developer_mode:
        #     proc = subprocess.Popen(['python', scr_f_name, rocket_type_arg.value], shell=True)
        # else:
        #     proc = subprocess.Popen(['start', scr_f_name, rocket_type_arg.value], shell=True)
        # Coordinator.active_proc_id = proc.pid

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
            Coordinator.kill_subproc()
            Coordinator.active_proc_id = None
            Coordinator.sight_hvr_displayed = False
            Coordinator.sight_ir_displayed = False
            Coordinator.sight_er_displayed = False

    def minimize_rust_window():
        whnd = win32gui.FindWindowEx(None, None, None, 'Rust')
        if not whnd or win32gui.GetWindowPlacement(whnd)[2][0] == -1:
            return
        win32gui.ShowWindow(whnd, win32con.SW_MINIMIZE)


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