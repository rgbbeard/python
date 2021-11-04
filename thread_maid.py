import threading


class ThreadMaid:
	__thread = None
	__thread_target = None
	__thread_arguments = tuple()

	def __init__(self):
		pass  # Just instantiate the class

	def setup(self, target, arguments: tuple = ()):
		self.__set_target(target)
		self.__set_arguments(arguments)
		self.__thread = Thread(target=self.__thread_target, args=self.__thread_arguments)
		return self

	def __set_target(self, t):
		self.__thread_target = t

	def __set_arguments(self, a: tuple):
		if len(a) > 0:
			self.__thread_arguments = a

	def halt(self):
		if self.__thread != None:
			self.__thread.stop()

	def run(self):
		if self._thread != None:
			self.__thread.start()
