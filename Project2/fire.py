import pdb

def decorateur(fonction):
	print(fonction.__name__ + " j'appel ma fonction")
	return fonction

	pdb.set_trace()

@decorateur
class Foo(object):
	def __init__(self):
		self.name = ["Müller","Schmidt","Schneider"]
		self.age = [12] 
		self.prenom = ["Meyer","Weber","Hofman"]

	def __repr__(self):
		return f"{__class.__name__} {self.age}"
class Fox:
	def __init__(self,ville,pays):
		self.ville = ville
		self.pays = pays 

	def __str__(self):
		return f"{__class__.__name__} {self.ville} {self.pays}"



a = Foo()
print(a.name[1])
print(a.age)
print(a.prenom[1])

b = Fox("paris","France")
print(b)
