class Personne:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        
    def __repr__(self):
        return f'{__class__.__name__} {self.nom} {self.prenom}'
class Parent(Personne):
    def __init__(self,nom,prenom,salaire):
        super().__init__(nom,prenom)
        self.salaire = salaire
    
    def get_salaire(self,min,max ):
        
        if (self.salaire < 200):
            print('vous etes mal payer')
        elif (self.salaire > 1000):
            print('vous etes bien payer')
        
class Mere (Parent,Personne):
    def __init__(self, nom, prenom, age, salaire):
        super().__init__(nom,prenom,age)
        #Parent.__init__(self,salaire)
        self.age = age 
        #self.salaire = salaire
        
    def __str__(self):
        return f'Bonjour {self.nom} {self.prenom} {self.age} {self.salaire}'
    
try:  
    import os
    os.chdir("C/Arme")    
    fichier = open("PS E:\\Arme\\mon_fichier.txt")   
    fichier.close()
except:
    print('fichier introuvable')
import json
data = {'nom': ['paul','jean','joseph'],'age':21, 'salaire':[20100,3000]
}
with open ("data.json","w") as f:
    json.dump(data,f)

with open('data.json','r') as f:
    data = json.load(f)
    print(data)
    
if __name__=='__main__':
    
    var = Mere("Joseph","Jude",32,2000)
    print(var)
    var.get_salaire(1000,2000)

    variable = Personne("Paul","Doe") 
    print(variable)         