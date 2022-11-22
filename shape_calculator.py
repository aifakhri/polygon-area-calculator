class Rectangle:
	def __init__(self, width, height):
		#For default value of the width and height
		self.width = width
		self.height = height

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'
	
	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		area = self.width * self.height
		return area

	def get_perimeter(self):
		perimeter = (2 * self.width) + (2 * self.height)
		return perimeter

	def get_diagonal(self):
		diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
		return diagonal

	def get_picture(self):
		pict = []
		if self.width > 50 or self.height > 50:
			return 'Too big for picture.'
		else:
			for height in range(self.height):
				pict.append(self.width*'*'+'\n')
			pict = ''.join(pict)
		return pict

	def get_amount_inside(self, shape):
		width_ratio = int(self.width/shape.width)
		height_ratio = int(self.height/shape.height)

		volume = width_ratio * height_ratio
		return volume

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)

	def __str__(self):
		return f'Square(side={self.width})'
	
	def set_side(self, side):
		super().__init__(side, side)
