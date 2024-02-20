class Time:
	def __init__(self, hour, minute):
		self.hour = hour
		self.minute = minute
	
	@property
	def hour(self):
		return self.__hour
	
	@hour.setter
	def hour(self, hour):
		if not isinstance(hour, int) or hour < 0:
			self.__hour = 0
		elif hour > 23:
			self.__hour = 23
		else:
			self.__hour = hour
		
	@property
	def minute(self):
		return self.__minute
	
	@minute.setter
	def minute(self, minute):
		if not isinstance(minute, int) or minute < 0:
			self.__minute = 0
		elif minute > 59:
			self.__minute = 59
		else:
			self.__minute = minute
