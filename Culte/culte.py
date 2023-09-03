import math

class CircleAire:

	def __init__(self, radius):
		self.radius = radius

	@classmethod
	def circle(cls, radius):

		area = math.pi * radius ** 2
		return area

a = CircleAire.circle(2)
print(a)