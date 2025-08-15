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
    elif tesled == "lsapps":
        for path in rvar.vpath:
            full_path = os.path.join("fs", path.lstrip("/"))
            if not os.path.isdir(full_path):
                continue
            for filename in os.listdir(full_path):
                if not filename.endswith(".py"):
                    continue
                filepath = os.path.join(full_path, filename)
                app_name = None
                app_type = None

                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for line in f:
                            if line.startswith("RCLSYSAPPN"):
                                app_name = line.split("=", 1)[1].strip().strip('"').strip("'")
                            elif line.startswith("RCLSYSAPPT"):
                                app_type = line.split("=", 1)[1].strip().strip('"').strip("'")
                            if app_name and app_type:
                                break
                    if app_name and app_type:
                        print(f"{app_name} - {app_type}")

                except:
                    pass
    elif tesled == "vpath":
        print(f"{rvar.vpath}")
    else:
        if vpathrun(cmd, args):
            continue
        else:
            print(var.RED + " rsh: unknown command" + var.RESET)
