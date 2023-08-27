from abc import ABC, abstractmethod
from cryptography.fernet import Fernet

def fonction():

	key = Fernet.generate_key()

	with open('mykey.key','wb') as mykey:
		mykey.write(key)

	with open('mykey.key', 'rb') as mykey:
		key = mykey.read()
	print(key)
fonction()

class Method(ABC):

	@abstractmethod
	def Affiche(self):
		pass


class Montre(Method):
	def Affiche(self):
		return 'Informations'

class ClassName(object):

	def __init__(self, nom, prenom, ville, pays, age):
		self.nom = nom
		self.prenom = prenom
		self.ville = ville
		self.pays = pays 
		self.age = age
	
	def __len__(self):
		return len(self.nom) 


	def __repr__(self):
		return f"{__class__.__name__}: {self.nom} {self.prenom} {self.ville} {self.pays} {self.age} "

	def get_age(self,age):
		if self.age > 23:
			return "vous etes majeur"
		elif self.age < 15:
			return "vous etes un adolescant"

	def __ne__(self, other):
		return self.nom != other.nom

class Animal:

	def __init__(self, famille, genre, classe, taille, poids):

		self.famille = famille
		self.genre = genre 
		self.classe = classe 
		self.taille = taille
		self.poids = poids

	def __repr__(self):
		return f"{__class__.__name__}: {self.famille} {self.genre} {self.classe} {self.taille} {self.poids}"
			
	def __eq__(self, other):
		return self.poids == other.poids


cc = Animal("Alligatoridae caimaninae","Melanosuchus","Reptile", 4.3,  100)
print(cc)	

a = Montre()
print(a.Affiche())

mm = ClassName("poutine", "Michael","Moscou", "Russie", 22)
nn = ClassName("paul", "Michael","Moscou", "Russie", 21)

print(mm)

print(len(mm))
try:
	print(mm.get_age(32))
	raise ValueError("cela n'affiche rien")
except:
	print("Value Error")
print(mm != nn)

