class Person:
    especes = "ce sont tous des etes humain"

    def __init__(self,nom,prenom,age,ville) -> None:
        self.nom = nom 
        self.prenom = prenom
        self.age = age 
        self.ville = ville
    def __str__(self):
        return f'bonjour {self.nom} {self.prenom} vous avez {self.age} ans et vous etes a {self.ville}'


class Parent(Person):
    def __init__(self, nom, prenom, age, ville,metier,loisir) -> None:
        super().__init__(nom, prenom, age, ville)
        self.metier = metier
        self.loisir = loisir
    def metier(self):
        return f'votre metier est  {self.metier}'

    
    def loisir(self):
        return f'vous pratiquez {self.loisir}'
      
