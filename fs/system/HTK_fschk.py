import os

def fchk(dirs: list) -> bool:
    errors = []
    for d in dirs:
        if os.path.isdir(d):
            print(f"[OK]  {d}")
        else:
            print(f"[ERR] {d}")
            errors.append(d)
    if errors:
        print(f"\nfound {len(errors)} errors, fs corrupted")
        return False
    else:
        print("\nno errors")
        return True
