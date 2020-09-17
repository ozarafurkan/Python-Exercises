import sys

islem=input()
sembol=["/","*","+","-"]

Sade_islem=islem.replace(" ","")
uzunluk=len(Sade_islem)

for i in range(uzunluk):
    for j in sembol:
        if Sade_islem[i]==j and Sade_islem[i+1]==")" :
            print("Hata1")
            sys.exit() # Diğer hata mesajlarını göstermeyi engellemek için
        elif Sade_islem[i]==j and (not Sade_islem[i+1].isnumeric() and Sade_islem[i-1].isnumeric() and Sade_islem[i+1]!="("):
            print("Hata2")
<<<<<<< HEAD
            sys.exit()
=======
>>>>>>> 581604a420510fff91606cd31cbcf404e6872de3
    if Sade_islem[i]=="(" and Sade_islem[i+1]==")" :
        print("Hata3")
        sys.exit()

if islem.count("(") != islem.count(")"):
     print("Hata4")
