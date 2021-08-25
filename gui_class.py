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
WINDOW_DEFAULT_POS: int = 0
WINDOW_CENTERED: int = 1
# Window look
WINDOW_NATIVE: int = 0
WINDOW_CUSTOM: int = 1
# Cursors
CURSOR_SQUARED: str = "dotbox"
# Font
FONT_FAMILY = "Arial"
ARIAL_LARGE = (FONT_FAMILY, 25)
ARIAL_MEDIUM = (FONT_FAMILY, 18)
ARIAL_SMALL = (FONT_FAMILY, 15)


class Window:
    window = None

    def __init__(self, window_name: str = "",
                 window_use: int = WINDOW_NATIVE,
                 window_mode: int = WINDOW_NORMAL,
                 window_size: str = "500x500",
                 window_position: int = WINDOW_DEFAULT_POS):
        self.x = 0
        self.y = 0
        self.window = tkinter.Tk()
        self.window_title = "New Window"
        self.set_name(window_name)
        self.set_mode(window_mode=window_mode, window_size=window_size)
        self.set_look(window_use=window_use, window_name=window_name)

    def set_name(self, window_name: str = ""):
        if not window_name:
            window_name = "New Window"

        self.window.title(window_name)
        self.window_title = window_name

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

    def set_look(self, window_use: int = WINDOW_NATIVE, window_name: str = "New Window"):
        if window_use == WINDOW_CUSTOM:
            self.window.wm_overrideredirect(True)
            self.display_actions_bar(window_name)

    def display_actions_bar(self, window_name: str = ""):
        # Window name
        grip = tkinter.Label(
            self.window,
            text=window_name,
            font=ARIAL_SMALL
        )
        grip.pack(side=tkinter.TOP, fill=tkinter.BOTH, pady=5)

        # Drag window functionality
        grip.bind("<ButtonPress-1>", self.grab)
        grip.bind("<ButtonRelease-1>", self.release)
        grip.bind("<B1-Motion>", self.move)

        # Add here your navigation bar components

        # Minimize window button
        """
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
        ).pack(anchor="w", side="top")

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
            command=partial(self.dispose)
        ).pack(anchor="w", side="top")
        """

    def deploy(self):
        self.window.mainloop()

    def dispose(self):
        self.window.destroy()

    def minimize(self):
        self.window.overrideredirect(False)
        self.window.update_idletasks()
        self.window.state("iconic")

    def grab(self, event):
        self.x = event.x
        self.y = event.y

    def release(self, event):
        self.x = None
        self.y = None

    def move(self, event):
        delta_x = event.x - self.x
        delta_y = event.y - self.y
        x = self.window.winfo_x() + delta_x
        y = self.window.winfo_y() + delta_y
        self.window.geometry(f"+{x}+{y}")


def Separator(win_root, side: str = "left", height: int = 50):
    tkinter.Label(win_root).pack(side=side.lower(), pady=height)
