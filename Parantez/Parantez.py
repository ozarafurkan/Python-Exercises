islem=input()
sembol=["/","*","+","-"]

Sade_islem=islem.replace(" ","")
uzunluk=len(Sade_islem)

for i in range(uzunluk):
    for j in sembol:
        if Sade_islem[i]==j and Sade_islem[i+1]==")" :
            print("Hata1")
        elif Sade_islem[i]==j and (not Sade_islem[i+1].isnumeric() and Sade_islem[i-1].isnumeric() and Sade_islem[i+1]!="("):
            print("Hata2")
    if Sade_islem[i]=="(" and Sade_islem[i+1]==")" :
        print("Hata3")

if islem.count("(") != islem.count(")"):
     print("Hata4")
