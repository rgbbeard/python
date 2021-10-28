import json
from os import path
from re import match as matches
from app_utils import get_path

class JSONMaid():
	__data = None
	__storage: str = ""

	def __init__(self, filename: str = "ftpfiles.json"):
		foldername: str = ""

		if not matches(r"\/|\\", filename):
			foldername = get_path(filename)

		if ".json" in filename:
			self.__storage = f"{foldername}/{filename}"

			with open(self.__storage, "r") as data:
				data = data.read()
				self.__data = self.__from_json(data)

				if self.__data["data"] != dict:
					self.__data["data"] = dict()

	def __del__(self):
		self.__data = None

	def __from_json(self, data: str):
		return json.loads(data)

	def __to_json(self, data: dict):
		return json.dumps(data)

	def __save(self):
		data = self.__to_json(self.__data)
		storage = open(self.__storage, "w")
		storage.write(data)
		storage.close()

	def get_records(self):
		return self.__data["data"]

	def records_count(self):
		return len(self.get_records())

	def delete_record(self, id: int):
		data = self.get_records()

		try:
			del data[str(id)]
		except:
			return False
		finally:
			self.__save()
			return True

	def update_record(self, old_record: dict, new_record: dict):
		data = self.get_records()

		for x in range(1, self.records_count() + 1):
			row = data[str(x)]

			if row == old_record:
				row = new_record
				return True

		return False

	def put_record(self, record: dict):
		can_be_added = True
	    
		for x in range(1, self.records_count() + 1):
			row = self.get_records()[str(x)]

			if row == record:
				can_be_added = False
				break

		if can_be_added:
			uid = self.records_count() + 1
			uid = str(uid)

			self.__data["data"][uid] = record
			self.__save()

		return can_be_added
