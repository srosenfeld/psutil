import time, psutil, os

while True:
    for p in psutil.pids():
        print(psutil.Process(p).name())
        if psutil.Process(p).name() == "pythonw.exe":
            print("FOUND PYTHON")
            print(psutil.Process(p).pid)
            print(psutil.Process(p).open_files())
            #psutil.Process(p).terminate()
    time.sleep(2)
