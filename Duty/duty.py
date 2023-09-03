from abc import ABC, abstractmethod

class Forme(ABC):

	@abstractmethod
	def care_aire(self):
		pass

class Aire(Forme):

	def __init__(self, aire_care, care_cercle):

		self.aire_care = aire_care
		self.care_cercle = care_cercle

	@staticmethod
	def method(care_aire, care_cercle):

		Aire = care_aire / care_cercle
		return Aire

if __name__ == '__main__':
	V = Aire.method(2,5)
	print(V)
	
		