import sys
import pdb
class Voiture:
    fonction = 'ce sont des engins de deplacement'
    def __init__(self,marque,modele,prix,vitesse):
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.vitesse = vitesse
        
    def __repr__(self):
        return f'{__class__.__name__} {self.marque} {self.modele} {self.prix} {self.vitesse}'
    
    #pdb.set_trace() #ce module permet de deboguer les Erreurs
    
    @classmethod
    def function(cls):
        return cls.fonction
    
    def getPrice(self,min,max):
        if self.prix < min:
            print('La voiture est moins ',len(sys.argv))
        elif self.prix > max:
            print('La voiture est couteuse')
        else:
            return "le prix me vas!"

class Moto(Voiture):
    def __init__(self, marque, modele, prix, vitesse,moteur):
        super().__init__(marque, modele, prix, vitesse) 
        self.moteur = moteur 
        
    def __str__(self):
        return f"vous avez un moteur Robuste {self.moteur}"    
        
    def getCouleur(self,couleur):
        if self.couleur == 'blanc':
            print("La couleur ne tiendra pas longtemps",str(sys.argv))
        elif self.couleur != 'bleu':
            print("jaime cette couleur")

class Moto4Roues(Voiture):
    def __init__(self, marque, modele, prix, vitesse,couleur,date):
        super().__init__(marque, modele, prix, vitesse)
        self.couleur = couleur 
        self.date = date

            
class Velo(Voiture):
    def __init__(self, marque, modele, prix, vitesse,moteur,couleur,date,rayon,alarme):
        super().__init__(marque, modele, prix, vitesse)
        self.rayon = rayon
        self.alarme = alarme           

    def get_alarme(self):
        return 'pippipipi'
    
with open("fichier.txt","w") as mon_fichier:
    mon_fichier.write("Jaime python et je tient a coder en python a Vie!!!")
    mon_fichier.close()
    
with open("fichier.txt","r") as fichier:
    texte = fichier.read()
    print(texte)
    
if __name__=='__main__':
    voiture1 = Voiture("Ferrari","Citron",3000,1114)
    print(voiture1)

    print(voiture1.marque)
    voiture2 = Voiture.function()
    print(voiture2)

    voiture1.getPrice(22010,5322)

    moto1 = Moto("ktml","citron",3000,1114,"Pluton")
    print(moto1)

    moto4roues = Moto4Roues("Ferrari","citron",3000,1114,"pluton",2005)
    print(moto4roues)
    print(moto4roues.date)
    try:
        moto4roues.getCouleur('blanc')
    except:
        print("Erreur")
        

    velo1 = Velo("vetete","sport",3000,1114,"pluton",2005,"bleu","super","pipipipip")
    print(velo1)

    velo1.get_alarme()