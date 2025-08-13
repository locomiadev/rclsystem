import os

def SCRNCLR():
    os.system("cls" if os.name == "nt" else "clear") # win & posix support
