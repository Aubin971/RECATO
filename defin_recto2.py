import os
import csv
import random
from steganocryptopy.steganography import Steganography
input_image = 'df.png'  
key = ".\\_internal\\Pomelon.txt"

#tout les caractères
lettre = [chr(i) for i in range(97,123)]
lettremaj = [chr(i) for i in range(65,91)]
nombre = [chr(i) for i in range(48,58)]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@','/','à','+','µ','ù']
tout = [lettre,lettremaj,nombre,caracteres_speciaux]

def lire_csv_recto(namedoss):
    if namedoss[-4:]==".png" : 
        output_file = namedoss[0:-4]
        decrypted_text = Steganography.decrypt(key, namedoss)
        Steganography.write_file(output_file, decrypted_text)
        with open(output_file, mode="r") as csvfile :
            dossier = csv.reader(csvfile)
            for lines in dossier:
                try:
                    dossier = decrypter(lines)
                    os.remove(output_file)
                except:pass
            return dossier
    elif namedoss[-4:]==".rct" or namedoss=="recto_mail_.csv":  
        with open(namedoss, mode="r") as csvfile :
            dossier = csv.reader(csvfile)
            for lines in dossier:
                try:
                    dossier = decrypter(lines)
                except:pass
            return dossier

def lire_doss_recto(namedoss):
    try:
        nomdoss = os.listdir(f'.\\{namedoss}')
        return nomdoss
    except:
        path = "C:\\Users\\aubla\\Desktop\\NSI\\RECTO\\png"
        nomdoss = os.listdir(f'{path}\\{namedoss}')
        return nomdoss 

def decrypter(toutes):
    crypt=int(toutes[-1])
    pos=0
    for itemi in toutes :
        newitemi=''
        for caractere in itemi:
            num=0
            if caractere in lettre:
                while caractere != lettre[num]:
                    num+=1
                caractere = lettre[num+crypt-len(lettre)]
            if caractere in lettremaj:
                while caractere != lettremaj[num]:
                    num+=1
                caractere = lettremaj[num+crypt-len(lettremaj)]
            if caractere in nombre:
                try:
                    caractere = nombre[int(caractere)+crypt-len(nombre)]
                except:
                    caractere=nombre[int(caractere)+crypt-(len(nombre))*2]
            if caractere in caracteres_speciaux:
                while caractere != caracteres_speciaux[num]:
                    num+=1
                try:
                    caractere=caracteres_speciaux[num+crypt-len(caracteres_speciaux)]
                except:
                    caractere=caracteres_speciaux[num+crypt-len(caracteres_speciaux)-len(caracteres_speciaux)]
            else:
                pass
            newitemi=newitemi+str(caractere)
        toutes.pop(pos)
        toutes.insert(pos, newitemi)
        pos+=1
    toutes.pop(-1)
    toutes.insert(6, crypt)
    return (toutes)

def cryptage(toutes):
    crypt = random.randrange(1, 26)
    for (typs,itemi) in toutes.items():
        newitemi=''
        for caractere in itemi:
            num=0
            if caractere in lettre:
                while caractere!=lettre[num]:
                    num+=1
                caractere=lettre[num-crypt]
            if caractere in lettremaj:
                while caractere!=lettremaj[num]:
                    num+=1
                caractere=lettremaj[num-crypt]
            if caractere in nombre:
                try:
                    caractere=nombre[int(caractere)-crypt]
                except:
                    try:
                        caractere=nombre[int(caractere)-crypt+len(nombre)]
                    except:
                        caractere=nombre[int(caractere)-crypt+2*(len(nombre))]
            if caractere in caracteres_speciaux:
                while caractere!=caracteres_speciaux[num]:
                    num+=1
                try:
                    caractere=caracteres_speciaux[num-crypt]
                except:
                    try:
                        caractere=caracteres_speciaux[num-crypt-len(caracteres_speciaux)]
                    except:
                        caractere=caracteres_speciaux[num-crypt-2*(len(caracteres_speciaux))]
            else:
                pass
            newitemi=newitemi+str(caractere)
        toutes[typs]=newitemi
    toutes['crypt']=crypt
    return (toutes)

def passworde(nombcara,symb,nomb,lett,maj):
    password = str()
    toute = []
    if symb == True:
        toute.append(caracteres_speciaux)
    if nomb == True:
        toute.append(nombre)
    if lett == True:
        toute.append(lettre)
    if maj == True:
        toute.append(lettremaj)
    for i in range(nombcara):
        typ=toute[random.randint(0,len(toute)-1)]
        newcara=typ[random.randint(0,(len(typ))-1)]
        password=password+newcara
    return password

def enregistrer_carte(namedoss,pseudo,email,password,lien,infos):
    if (namedoss[-4:]=='.rct') or (namedoss == 'addresse_mailset.rct'):
        pass
    else :
        namedoss+='.rct'
    with open(namedoss, mode="w") as csvfile :
        toutes = {'pseudo' :pseudo, 'email' :email, 'password' :password, 'lien' :lien, 'infos' :infos}
        cryptage(toutes)
        fieldnames=toutes.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dict(toutes))
    output_image = namedoss+'.png'
    input_file = namedoss
    encrypted_image = Steganography.encrypt(key, input_image, input_file)
    encrypted_image.save(output_image)
    os.remove(namedoss)
    
        
        
def score(password):
    al=[]
    scored=(len(password))*40
    for letre in password:
        if (letre in nombre)or(letre in caracteres_speciaux)or(letre in lettremaj):
            scored+=20
        if letre not in al:
            al.append(letre)
    scored=scored+(len(al))*40
    if password[0] in lettremaj:
        scored-=20
    if password[-1] in caracteres_speciaux:
        scored-=20
    if password[-1] in nombre:
        scored-=20
    scored/=1000
    return scored