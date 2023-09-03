class Pyramide:

	def __init__(self, rayon, hauteur):

		self.rayon = rayon
		self.hauteur = hauteur

	@staticmethod
	def variable(rayon, hauteur):

		volume = rayon * rayon * 3.14 * hauteur * (1/3)
		return volume

var = Pyramide.variable(3,1)
print(var)