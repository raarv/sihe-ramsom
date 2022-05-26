import random
import string


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "[email protected]#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Indique largo de la contraseña: "))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the password
	print("Nueva contraseña:\n")
	print("".join(password))
	print("\n\n")



## invoking the function
generate_random_password()
import Ransomware
