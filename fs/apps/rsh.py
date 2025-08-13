RCLSYSAPPN = "RCL Shell"
RCLSYSAPPT = "Dangerous to remove"
import fs.system.rcluser as usr
import fs.system.HTK_variables as var
import time
# This is RCL System basic shell (RSh)

username = usr.getUser()    # Username getting.
vpath = ["/apps"]           # $PATH for pyvfs

while True:
    tesled = input(username + " > ")
    if tesled == "version":
        print(" RCL System: version " + var.sysver)
    elif tesled == "shutdown":
        print(" Shutting down...")
        time.sleep(0.8)
        exit()
    else:
        print(var.RED + " rsh: unknown command" + var.RESET)
