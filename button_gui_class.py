from gui import *

def is_array(a):
	return isinstance(a, list) or isinstance(a, tuple) or isinstance(a, dict)


class Button:
	__root = None
	__btn = None
	__text = None

	def __init__(self, root, text: str = "", width: int = 5, height: int = 2, click: object = None, hover: object = None):
		if not text:
			self.__text = "Button"

		self.__btn = tkinter.Button(root, width=width, height=height, text=self.__text)
		self.__root = root

	def set_background(self, background: str):
		if not (not background):
			self.__btn.config(bg=background)

	def set_color(self, color: str):
		if not (not color):
			self.__btn.config(color=color)

	def set_text(self, text: str, text_variable: bool = False):
		if not (not text):
			if isinstance(self.__text, tkinter.StringVar):
				self.__text.set(text)
			else:
				if text_variable:
					self.__text = tkinter.StringVar(self.__root, self.__text)
				else:
					self.__text = text
		else:
			raise Exception("Text must be a non-empty string")

	def hover(self, function: object, args = []):
		if callable(function):
			if not is_array(args):
				args = []

			self.__btn.bind("<Enter>", partial(function, args))
		else:
			raise Exception("Hover event must be a valid function.")
			exit()

	def click(self, function: object, args = []):
		if callable(function):
			if not is_array(args):
				args = []

			self.__btn.bind("<ButtonPress-1>", partial(function, args))
		else:
			raise Exception("Click event must be a valid function.")
			exit()

	def get_button(self):
		return self.__btn
