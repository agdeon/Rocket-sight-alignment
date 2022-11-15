import subprocess
import psutil
import os
import time
import multiprocessing
from multiprocessing import Process
import PySimpleGUI as sg


def get_children_pids():
    children = multiprocessing.active_children()
    result = list()
    for child in children:
        result.append(str(child.pid))
    return ','.join(result)

def f(name):
    process = multiprocessing.current_process()
    pid = process.pid
    name = process.name

    print(f'[subprocess] name: {name} pid: {pid} parent: {os.getppid()}')
    layout = [[sg.Text('My one-shot window.')],
                     [sg.InputText()],
                     [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    window.close()
    text_input = values[0]
    sg.popup('You entered', text_input)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p = Process(target=f, args=('jane',))
    p.start()

    process = multiprocessing.current_process()
    pid = process.pid
    name = process.name
    print(f'[main process] name: {name} pid: {pid} children: {get_children_pids()}')


# proc = psutil.Process()
# if proc.name() == 'python.exe':  # developer mode
#     print(f'{proc.name()} > parent.py > id: {str(proc.pid)}')
#     proc = subprocess.Popen('python child.py', shell=True)
# elif proc.name() == 'parent.exe':
#     print('parent.exe > id: ' + str(proc.pid))
#     proc = subprocess.Popen(['start', 'child.exe'], shell=True)



