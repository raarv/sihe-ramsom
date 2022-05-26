import random
import string


total = string.ascii_letters + string.digits + string.punctuation
passlength = input("Indique el largo de la contraseña:\t")
length = passlength

password = "".join(random.sample(total, length))

print("Nueva contraseña:\t" + password)
