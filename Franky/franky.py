import math

class Sphare:

	def __init__(self, radius):

		self.radius = radius

	def SphareSurface(radius):

		surface_area = 4 * math.pi * radius ** 2
		return surface_area

p = Sphare.SphareSurface(7)
print(p)