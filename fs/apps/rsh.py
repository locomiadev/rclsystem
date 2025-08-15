RCLSYSAPPN = "RCL Shell"
RCLSYSAPPT = "Dangerous to remove"
import fs.system.rcluser as usr
import fs.system.HTK_variables as var
import time
import sys
import os
import fs.private.rsh.variables as rvar
# This is RCL System basic shell (RSh)

username = usr.getUser()    # Username getting.

def vpathrun(cmd, args):
    for path in rvar.vpath:
        full_path = os.path.join("fs", path.lstrip("/"), cmd + ".py")
        if os.path.isfile(full_path):
            os.system(f"python3 {full_path} {' '.join(args)}")
            return True
    return False

while True:
    tesled = input(username + " > ")
    parts = tesled.split()
    cmd = parts[0]
    args = parts[1:]
    if tesled == "version":
        print(" RCL System: version " + var.sysver)
    elif tesled == "shutdown":
        print(" Shutting down...")
        time.sleep(0.8)
        exit()
    elif tesled == "help":
        rvar.help()
    elif tesled == "vpath":
        print(f"{rvar.vpath}")
    else:
        if vpathrun(cmd, args):
            continue
        else:
            print(var.RED + " rsh: unknown command" + var.RESET)
