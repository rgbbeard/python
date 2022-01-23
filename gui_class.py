"""
Minimum Python version 3.x
Using Python version 3.9.5
"""

import tkinter
from functools import partial
from math import floor

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
                 window_appearance: int = WINDOW_NATIVE,
                 window_buttons: bool = False,
                 window_mode: int = WINDOW_NORMAL,
                 window_size: str = "500x500",
                 window_position: int = WINDOW_DEFAULT_POS):
        self.x = 0
        self.y = 0
        self.window = tkinter.Tk()
        self.window_title = "New Window"
        self.set_name(window_name)
        self.set_mode(mode=window_mode, size=window_size)
        self.set_look(appearance=window_appearance, buttons=window_buttons, name=window_name)
        self.set_position(position=window_position, size=window_size)

    def set_name(self, window_name: str = ""):
        if not window_name:
            window_name = "New Window"

        self.window.title(window_name)
        self.window_title = window_name

    def set_mode(self, mode: int = WINDOW_NORMAL, size: str = "500x500"):
        global WINDOW_FULL_SCREEN, WINDOW_HIDDEN, WINDOW_NORMAL

        if mode == WINDOW_NORMAL:
            if ("x" not in size) or (not size):
                raise Exception("Using WINDOW_NORMAL, size parameter must be defined too")

            # Set window size
            self.window.geometry(size)

        elif mode == WINDOW_FULL_SCREEN:
            self.window.wm_attributes('-fullscreen', 'true')

        elif mode == WINDOW_HIDDEN:
            self.window.wm_attributes('-fullscreen', 'true')
            self.window.wm_state("iconic")

    def set_look(self, appearance: int = WINDOW_NATIVE, buttons: bool = False, name: str = "New Window"):
        global WINDOW_CUSTOM

        if appearance == WINDOW_CUSTOM:
            self.window.wm_overrideredirect(True)
            self.display_actions_bar(name, buttons)

    def set_position(self, position: int = WINDOW_DEFAULT_POS, size: str = "500x500"):
        global WINDOW_CENTERED

        if position == WINDOW_CENTERED:
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()

            window_width, window_height = size.split("x")

            screen_width = floor((int(screen_width) - int(window_width)) / 2)
            screen_height = floor((int(screen_height) - int(window_height)) / 2)

            self.window.geometry(f"+{screen_width}+{screen_height}")

    def display_actions_bar(self, navbar_title: str = "", navbar_buttons: bool = False):
        global ARIAL_SMALL, CURSOR_SQUARED

        # Window name
        handle = tkinter.Label(
            self.window,
            text=navbar_title,
            font=ARIAL_SMALL
        )
        handle.pack(side="top", fill="both", pady=5)

        # Drag window functionality
        handle.bind("<ButtonPress-1>", self.grab)
        handle.bind("<ButtonRelease-1>", self.release)
        handle.bind("<B1-Motion>", self.move)

        # Add here your navigation bar components        
        if navbar_buttons:
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

    def display(self):
        self.window.mainloop()

    def dispose(self):
        self.window.destroy()

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
