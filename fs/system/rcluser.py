import time
import os

ver = "1.0"

def getUser():
    return "no name yet"

def main():
    print(f"rcluser {ver}")
    print("rcluser: checking for /private/users.py")
    time.sleep(0.5)
    print("rcluser: no /private/users.py! gaining access without user (dangerous)")
    time.sleep(0.3)
    os.system("python3 -m fs.apps.rsh")

if __name__ == "__main__":
    main()
