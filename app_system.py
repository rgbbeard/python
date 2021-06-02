import sys


def Terminate(code: int = 0):
    sys.exit(code)


def IsWindows():
    result: int = 0
    windows = sys.platform.lower()
    if "win" in windows:
        result = 1
    else:
        result = 0
    return result


def IsLinux():
    result: int = 0
    if "linux" in sys.platform.lower():
        result = 1
    else:
        result = 0
    return result


def IsMac():
    result: int = 0
    if "darwin" in sys.platform.lower():
        result = 1
    else:
        result = 0
    return result


def RequireOS(osName: str, dieOnError=False, debugger: bool = False):
    debug: str = ""
    result: int = 0
    osName = osName.lower()
    hostOS = sys.platform.lower()

    if osName in "windows" or osName in "win7" or osName in "win10":
        result = IsWindows()
        if result == 1:
            debug = "Detected OS: Windows"

    if osName in "linux":
        result = IsLinux()
        if result == 1:
            debug = "Detected OS: Linux"

    if osName == "darwin" or osName == "osx" or osName == "macos" or osName == "macosx":
        result = IsMac()
        if result == 1:
            debug = "Detected OS: Mac"

    if debugger == True:
        if result == 0:
            debug = "Detected OS:" + hostOS
        print("app_system.RequireOS Debugger message: \n -- " + debug)

    if dieOnError == True and result == 0:
        print(
            "app_system.RequireOS message: \n -- Function detected a different system\nProgram exited")
        Terminate(result)
