import math

class MaClasse:
	def __init__(self, radius , height):

		self.radius = radius
		self.height = height

	@staticmethod
	def Surface(radius, height):

		base_area = math.pi * radius ** 2
		lateral_area = 2 * math.pi * radius * height
		total_area = 2 * base_area + lateral_area
		return total_area

c = MaClasse.Surface(2,3)
print(c)