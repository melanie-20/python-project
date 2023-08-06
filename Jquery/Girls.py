from index import Person,Parent


personne1 = Parent("Paul","Doe",33,"marseille","chapantier","football")
personne = Person("Paul","Doe",33,"marseille")
print(personne)
print(Person.especes)
try:
    personne1._metier()
    personne1.loisir()
except:
    print('Erreur')