from abc import abstractmethod
import sqlite3
import sys

class Humain:
    
    @abstractmethod
    def show(self):
        pass

class Anonymat(Humain):
    def show(self):
        return "Il aura assez de personne"

class Personne(object):

    var = "Ce sont les informations d'une personne"

    def __init__(self, nom, prenom, age, ville):

        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.ville = ville
    @classmethod
    def fonction(cls):
        return cls.var

    def __repr__(self):
        return f"{__class__.__name__}:{self.nom} {self.prenom} {self.age} {self.ville}"


class Description:
    def __init__(self, pays, club, loisir, artisse, musique):
        
        self.pays  = pays
        self.club = club
        self.loisir = loisir
        self.artisse = artisse
        self.musique = musique


    def get_club(self):
        if self.club == "Barcelone":
            print("ils sont pas fort")
        elif self.club == "Real Madrid":
            print("j'adore cette equipe")
        

    def __str__(self):
        return f"je vis a {self.pays} mon club de foot est {self.club} j'aime {self.loisir} ma musique {self.musique}"

class MaClasse:

    def folder(self):
        try:
            with open("fichir.json") as f:
                print(f)
        except FileNotFoundError:
            print("desole j'ai verifié le fichier n'exite pas!")
            exit()

    conn = sqlite3.connect("donnee.db")
    cur = conn.cursor()
    conn = sqlite3.connect(":memory:")
    
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )''')
     
    

    try:
        donnee = {"name":"Olivier", "age":30}
        cur.execute(''' INSERT INTO users (nom,age) VALUES (:nom, :age)''',donnee)
    except:
        print('Erreur')

    conn.commit()
    conn.close()
    
if __name__=='__main__':

    dog = Anonymat()
    print(dog.show())

    c = Personne.fonction()
    print(c)
    
    b = Personne("Paul","scoflied",34,"paris")
    print(b)
    
    a = MaClasse()
    print(a.folder())

