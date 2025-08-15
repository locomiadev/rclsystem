RCLSYSAPPN = "Echo"
RCLSYSAPPT = "Built-in"
import sys

def main():
    if len(sys.argv) <= 1:
        return
print(" ".join(sys.argv[1:]))
if __name__ == "__main__":
    main()
