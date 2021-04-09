import tkinter
import pyautogui
from functools import partial

# Window mode
WINDOW_HIDDEN: int = 0
WINDOW_NORMAL: int = 1
WINDOW_FULLSCREEN: int = 2
WINDOW_MATCH_SCREEN: int = 3
# Window position
WIN_DEFAULT_POS: int = 0
WINDOW_CENTERED: int = 1
# Window look
WIN_NATIVE: int = 0
WIN_CUSTOM: int = 1
# Cursors
CURSOR_SQUARED: str = "dotbox"


class Window():
    window = None

    def __init__(self, windowName: str = "", windowUse: int = WIN_NATIVE, windowMode: int = WINDOW_NORMAL, windowSize: str = "500x500", windowPosition: int = WIN_DEFAULT_POS) -> None:
        self.window = tkinter.Tk()
        self.setName(windowName)
        self.setMode(windowMode=windowMode, windowSize=windowSize)
        self.setLook(windowUse=windowUse, windowName=windowName)

    # Not working
    def getScreenSize(stringify: bool = True):
        x, y = pyautogui.size()

        if stringify == True:
            print(stringify)
            return str(x)+"x"+str(y)

        return x, y

    def setName(self, windowName: str = ""):
        if(not windowName):
            windowName = "New Window"

        self.window.title(windowName)

    def setMode(self, windowMode: int = WINDOW_NORMAL, windowSize: str = "500x500"):
        if windowMode == WINDOW_NORMAL:
            if ("x" not in windowSize) or (not windowSize):
                print("Using WINDOW_NORMAL, size parameter must be defined too")
                exit()
            # Set window size
            self.window.geometry(windowSize)

        # Not working
        elif windowMode == WINDOW_MATCH_SCREEN:
            geometrySize = self.getScreenSize()
            self.window.geometry(geometrySize)

        elif windowMode == WINDOW_FULLSCREEN:
            self.window.wm_attributes('-fullscreen', 'true')

        elif windowMode == WINDOW_HIDDEN:
            self.window.wm_attributes('-fullscreen', 'true')
            self.window.wm_state("iconic")

    def setLook(self, windowUse: int = WIN_NATIVE, windowName: str = "New Window"):
        if windowUse == WIN_CUSTOM:
            self.window.wm_overrideredirect(True)
            self.displayActionsBar()

    def displayActionsBar(self, windowName: str = ""):
        # Window name
        tkinter.Label(
            self.window,
            text=windowName,
            font="2"
        ).pack(side=tkinter.TOP, fill=tkinter.BOTH, pady=5)

        # Minimize window button
        tkinter.Button(
            self.window,
            width="2",
            text="-",
            bg="#f90",
            fg="#fff",
            justify="center",
            relief="flat",
            cursor=CURSOR_SQUARED,
            command=partial(self.minimize)
        ).pack(pady=5, padx=4, anchor="n", side="left")

        # Close window button
        tkinter.Button(
            self.window,
            width="2",
            text="x",
            bg="#d00",
            fg="#fff",
            justify="center",
            relief="flat",
            cursor=CURSOR_SQUARED,
            command=partial(self.end)
        ).pack(pady=5, padx=4, anchor="n", side="left")

    def init(self):
        self.window.mainloop()

    def end(self):
        self.window.destroy()

    def minimize(self):
        self.window.wm_state("iconic")


def Separator(winRoot, side: str = "left", height: int = 50):
    tkinter.Label(winRoot).pack(side=side.lower(), pady=height)
