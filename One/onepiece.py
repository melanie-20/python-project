class TriangleAire:

	def __init__(self, base, height):

		self.base = base
		self.height = height

	@classmethod
	def Area(cls, base, height):

		area = 0.5 * base * height
		return area 


b = TriangleAire.Area(7,3)
print(b)