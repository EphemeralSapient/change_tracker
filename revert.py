# This program reverts back to original by rebuilding the previous patch by patch
import subprocess


def start():
    # Get the current version
    current = None

    with open("history/new", "r") as f:
        current = f.read()

    # A copy of latest version
    with open("history/revert", "w") as f:
        f.write(current)

    for i in range(9, 0, -1):
        subprocess.call("patch -R history/revert history/patch_"+str(i)+".txt", shell=True)

        print("Reverted to version ", i)
        with open("history/revert", "r") as f:
            print(f.read())
        print("\n")
    print("Reverted to original version")

if __name__ == "__main__":
    start()