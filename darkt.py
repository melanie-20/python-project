class CubeSurface:

	def __init__(self, side_length):

		self.side_length = side_length


	def surface_area(side_length):

		surface_area = 6 * side_length ** 2
		return surface_area


kk = CubeSurface.surface_area(7)
print(kk)