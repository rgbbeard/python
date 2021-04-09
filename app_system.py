import sys
import os


def IsWindows():
    # Require windows system
    if "nt" in os.name:
        print("Detected Windows")
    else:
        sys.exit()
