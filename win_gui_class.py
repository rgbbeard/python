"""
Author - Davide - 09/04/2021

Minimum Python version 3.x

Using Python version 3.9

Git - https://github.com/rgbbeard/python/
"""
import tkinter
from functools import partial

# Window mode
WINDOW_HIDDEN: int = 0
WINDOW_NORMAL: int = 1
WINDOW_FULL_SCREEN: int = 2
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

    def __init__(self, windowName: str = "",
                 windowUse: int = WIN_NATIVE,
                 windowMode: int = WINDOW_NORMAL,
                 windowSize: str = "500x500",
                 windowPosition: int = WIN_DEFAULT_POS) -> None:
        self.window = tkinter.Tk()
        self.set_name(windowName)
        self.set_mode(windowMode=windowMode, windowSize=windowSize)
        self.set_look(windowUse=windowUse, windowName=windowName)

    def set_name(self, windowName: str = ""):
        if(not windowName):
            windowName = "New Window"

        self.window.title(windowName)

    def set_mode(self, windowMode: int = WINDOW_NORMAL, windowSize: str = "500x500"):
        if windowMode == WINDOW_NORMAL:
            if ("x" not in windowSize) or (not windowSize):
                print("Using WINDOW_NORMAL, size parameter must be defined too")
                exit()
            # Set window size
            self.window.geometry(windowSize)

        elif windowMode == WINDOW_FULL_SCREEN:
            self.window.wm_attributes('-fullscreen', 'true')

        elif windowMode == WINDOW_HIDDEN:
            self.window.wm_attributes('-fullscreen', 'true')
            self.window.wm_state("iconic")

    def set_look(self, windowUse: int = WIN_NATIVE, windowName: str = "New Window"):
        if windowUse == WIN_CUSTOM:
            self.window.wm_overrideredirect(True)
            self.display_actions_bar()

    def display_actions_bar(self, windowName: str = ""):
        # Window name
        grip = tkinter.Label(
            self.window,
            text=windowName,
            font="2"
        )
        grip.pack(side=tkinter.TOP, fill=tkinter.BOTH, pady=5)

        # Drag window functionality
        grip.bind("<ButtonPress-1>", self.grab)
        grip.bind("<ButtonRelease-1>", self.place)
        grip.bind("<B1-Motion>", self.move)

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
        self.window.overrideredirect(False)
        self.window.update_idletasks()
        self.window.state("iconic")
        self.window.overrideredirect(True)

    def grab(self, event):
        self.x = event.x
        self.y = event.y

    def place(self, event):
        self.x = None
        self.y = None

    def move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")


def Separator(winRoot, side: str = "left", height: int = 50):
    tkinter.Label(winRoot).pack(side=side.lower(), pady=height)
