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

    def __init__(self, window_name: str = "",
                 window_use: int = WIN_NATIVE,
                 window_mode: int = WINDOW_NORMAL,
                 window_size: str = "500x500",
                 window_position: int = WIN_DEFAULT_POS) -> None:
        self.window = tkinter.Tk()
        self.set_name(window_name)
        self.set_mode(window_mode=window_mode, window_size=window_size)
        self.set_look(window_use=window_use, window_name=window_name)

    def set_name(self, window_name: str = ""):
        if(not window_name):
            window_name = "New Window"

        self.window.title(window_name)

    def set_mode(self, window_mode: int = WINDOW_NORMAL, window_size: str = "500x500"):
        if window_mode == WINDOW_NORMAL:
            if ("x" not in window_size) or (not window_size):
                print("Using WINDOW_NORMAL, size parameter must be defined too")
                exit()
            # Set window size
            self.window.geometry(window_size)

        elif window_mode == WINDOW_FULL_SCREEN:
            self.window.wm_attributes('-fullscreen', 'true')

        elif window_mode == WINDOW_HIDDEN:
            self.window.wm_attributes('-fullscreen', 'true')
            self.window.wm_state("iconic")

    def set_look(self, window_use: int = WIN_NATIVE, window_name: str = "New Window"):
        if window_use == WIN_CUSTOM:
            self.window.wm_overrideredirect(True)
            self.display_actions_bar()

    def display_actions_bar(self, window_name: str = ""):
        # Window name
        grip = tkinter.Label(
            self.window,
            text=window_name,
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
