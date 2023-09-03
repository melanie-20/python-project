from abc import ABC, abstractmethod

class Point(ABC):

	@abstractmethod
	def surface(self):
		pass


class Cuboid(Point):

	def __init__(self, length, width, heigth):

		self.length = length
		self.width = width
		self.heigth = heigth


	@classmethod
	def surface(cls, length, width, heigth):
		area = 2 *(length * width + length * length + width * length)
		return area

mm = Cuboid.surface(2,8,6)
print(mm)