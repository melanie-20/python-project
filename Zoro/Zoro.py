import pickle
from pathlib import Path 
import pdb
from abc import ABC, abstractmethod

chemin = Path("fichier.txt").exists()
print(chemin)

data = {"paul", "mark", "jean","michelle"}

with open('data', 'wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(data)

with open("data", "rb") as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	data = mon_depickler.load()
	print(data)


def decorateur(classe):
	print(classe.__name__ + ' ' "j'appel")
	return classe


@decorateur
class MaClasse:

	def __init__(self, masse , kilogramme, hauteur):
		self.masse = masse
		self.kilogramme = kilogramme
		self.hauteur = hauteur

	@staticmethod
	def method(masse, kilogramme, hauteur):

		Ep = masse * kilogramme * hauteur
		return Ep

class Number(ABC):

	@abstractmethod
	def Run(self):
		pass

class Somme(Number):
	def Run(self):
		return "j'utiliserai des method"

class Calcule:

	def __init__(self, longueur, largeur):

	 	self.longueur = longueur
	 	self.largeur = largeur

	@staticmethod
	def calculatrice(longueur, largeur):

		Perimetre = longueur * largeur
		return Perimetre


b = Somme()
print(b.Run())
c = Calcule.calculatrice(2,4)
print(c)
a = MaClasse.method(4,1,3)
print(a)