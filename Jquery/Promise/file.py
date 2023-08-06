class Eloi(object):
    def __init__(self,nom,salaire,job,residence) -> None:
        self.nom = nom 
        self.salaire = salaire
        self.job = job
        self.residence = residence
    def __str__(self) -> str:
        return f'bonjour Mr {self.nom} vous avez comme salaire {self.salaire} vous travailler en tant que {self.job} vous vivez {self.residence} '
    def __len__(self):
        return len(self.nom)

class Animal(object):
    def mouve(self):
        return 'Polymormisme'
    
class Serpent(Animal):
    def moue(self):
        print("le serpent rampe")
        
class Lion(Animal):
    def mouve(self):
        return 'le lion est rapide'
    
def mouve(Animal):
    print(Animal.mouve)
       
if __name__=='__main__':
    
    serpent = Serpent()
    lion = Lion()
    print(mouve(serpent))
    print(mouve(lion))
    
    compteur = Eloi("Boidy",32541,"developpeur","st-louis")
    print(compteur)
    print(len(compteur))
   
    
    
