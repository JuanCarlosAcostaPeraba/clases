class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, width):
		if width < 0:
			raise ValueError("Width must be positive")
		self.__width = width

	@property
	def height(self):
		return self.__height
	
	@height.setter
	def height(self, height):
		if height < 0:
			raise ValueError("Height must be positive")
		self.__height = height

	# crear una propiedad de solo lectura
	@property
	def area(self):
		return self.width * self.height
	