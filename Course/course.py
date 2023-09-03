import math

class ConeArea:

	def __init__(self, radius , slant_height):

		self.radius = radius
		self.slant_height = slant_height

	def area(radius, slant_height):

		base_area = math.pi * radius * 2
		lateral_area = math.pi * radius * slant_height
		total_area = base_area + lateral_area
		return total_area


d = ConeArea.area(2,8)
print(d)

