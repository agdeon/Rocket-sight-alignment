import psutil

proc = psutil.Process()

try:
    pid = proc.pid
except:
    pid = ''
try:
    parent_pid = proc.parent().pid
except:
    parent_pid = ''

f = open("child.txt", "a")
f.write(f'[child] My id is: {pid} My parent is: {parent_pid}\n')
f.close()