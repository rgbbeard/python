import json
from os import path

class JSONMaid():
	__connection = None
	__database: str = ""

	def __init__(self, database: str = ""):
		if path.isfile(database) and ".json" in database:
			self.__database = database

			with open(database, "r") as data:
				data = data.read()
				self.__connection = self.__from_json(data)

	def __del__(self):
		self.__connection = None

	def __from_json(self, data: str):
		return json.loads(data)

	def __to_json(self, data: dict):
		return json.dumps(data)

	def __save(self):
		data = self.__to_json(self.__connection)
		database = open(self.__database, "w")
		database.write(data)

	def get_records(self):
		return self.__connection["data"]

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

      self.__connection["data"][uid] = record
      self.__save()

		return can_be_added
