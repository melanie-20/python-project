from cryptography.fernet import Fernet

#crypter fichier

key = Fernet.generate_key()
f = Fernet(key)
with open('fichier.txt','rb') as original_file:
        originale = original_file.read()
        
encrypted = f.encrypt(originale)

with open('enc_fichier.txt','wb') as encrypted_file:
        encrypted_file.write(encrypted)

    
#Decrypter fichier

f = Fernet(key)
with open('enc_fichier.txt','rb') as encrypted_file:
        encrypted = encrypted_file.read()
        
decrypted = f.decrypt(encrypted)

with open('dec_fichier.txt','wb') as decrypyed_file:
        decrypyed_file.write(decrypted)
