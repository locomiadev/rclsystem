import os
import time
from fs.system.HTK_video import SCRNCLR
import fs.system.HTK_variables as var
import fs.system.HTK_fschk as fscc

SCRNCLR()

# waller1init
try:
            initstart = time.time()
            print("[waller1init] HTK_video module enabled")
            time.sleep(0.03)
            print("[waller1init] HTK_variables module enabled")
            time.sleep(0.03)
            print(var.GREEN + "[waller1init] Enabled COLORS" + var.RESET)
            time.sleep(0.03)
            print(var.BLUE + "[waller1init] Checking HTK_variables..." + var.RESET)
            varchkstart = time.time()
            print(var.RED + "[waller1init] red")
            print(var.GREEN + "[waller1init] green")
            print(var.BLUE + "[waller1init] blue")
            print(var.RESET + "[waller1init] reset")
            print(var.BOLD + "[waller1init] bold")
            print(var.RESET)
            print("[waller1init] kernel is " + var.KERNEL)
            print("[waller1init] os name is " + var.OS_NAME)
            varchkend = time.time()
            time.sleep(0.03)
            print(f"{var.GREEN}[waller1init] Successfully checked HTK_variables for {varchkend - varchkstart} seconds{var.RESET}")
            time.sleep(0.03)
            print(var.BLUE + "[waller1init] checking the filesystem..." + var.RESET)
            time.sleep(0.1)
            fh = ["fs/private", "fs/user", "fs/system", "fs/apps", "fs/temp"]
            if fscc.fchk(fh):
                print(var.GREEN + "[waller1init] fschk: good environment" + var.RESET)
            else:
                print(var.RED + "[waller1init] fschk: environment broken" + var.RESET)
                print(var.RED + "[waller1init] aborting initializing" + var.RESET)
                print(var.RED + "[htk] failed to initialize" + var.RESET)
                print(var.RED + "[htk] kernel panic: failed init [return 1]" + var.RESET)
                exit()
            time.sleep(0.03)
            initend = time.time()
            print(f"{var.GREEN}[waller1init] initialized successfully [{initend - initstart}]{var.RESET}")
            print(var.GREEN + "[waller1init] now you will boot into waller1init nonbooted shell.\nif you want to log into your system write 'execsys'" + var.RESET)
            while True:
                nonbooted = input("waller1init >> ")
                if nonbooted == "version":
                    print(" waller1init: version 1.00")
                elif nonbooted == "execsys":
                    print(" waller1init: executing system...")
                    time.sleep(0.5)
                    os.system("python3 -m fs.system.rcluser")
                else:
                      print(var.RED + " waller1init: wrong cmd" + var.RESET)
            
except KeyboardInterrupt:
            print(var.RED + "\n[htk] return 2: Force-shutdowned." + var.RESET)

