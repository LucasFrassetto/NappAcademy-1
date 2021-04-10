from datetime import date


class MyCalendar():
	def __init__(self, *args):
		self.datas = []
		
		for arg in args:
			self.append_date(arg)

	def date_valid(self, data):
		if isinstance(data, str):
			if "/" in data:
				data_split = data.split("/")
				if len(data_split) == 3:
					year = int(data_split[2])
					month = int(data_split[1])
					day = int(data_split[0])
					
					if month > 12:
						return (False, data)

					if day > 31:
						return (False, data)

					data = date(year=year, month=month, day=day)
					if self.date_exists(data):
						return (False, data)
					return (True, data)

		elif isinstance(data, date):
			if self.date_exists(data):
				return (False, data)

			return (True, data)

		return (False, data)

	def date_exists(self, data):
		if data in self.datas:
			return True
		return False

	def append_date(self, data):
		valid, data = self.date_valid(data)
		if valid:
			self.datas.append(data)

	def add_holiday(self, *args):
		for arg in args:
			valid, data = self.date_valid(arg)
			if valid:
				self.datas.append(data)

	def check_holiday(self, data):
		valid, data = self.date_valid(data)
		if data in self.datas:
			return True
		return 	False