class SquareArea:

	def __init__(self, side_length):

		self.side_length = side_length

	@classmethod
	def AreaSquare(cls, side_length):

		area = side_length ** 2
		return area


n = SquareArea.AreaSquare(6)
print(n)
