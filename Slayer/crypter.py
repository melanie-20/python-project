from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)

with open("file.json", "rb") as origonale_file:
	origonale = origonale_file.read()

encrypted = f.encrypt(origonale)

with open("enc_file.json", "wb") as encrypted_file:
	encrypted_file.write(encrypted)



#decrypter fichier

f = Fernet(key)
with open("enc_file.json", "rb") as encrypted_file:
	encrypted = encrypted_file.read()


decrypted = f.decrypt(encrypted)

with open("dec_file.json", "wb") as decrypted_file:
	decrypted_file.write(decrypted)