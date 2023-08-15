from cryptography.fernet import Fernet

#Creons une clee
key = Fernet.generate_key()

with open('mykey.key','wb') as mykey:
    mykey.write(key)
    
#Chargement d'une clee    

with open('mykey.key','rb') as mykey:
    key = mykey.read()
print(key)