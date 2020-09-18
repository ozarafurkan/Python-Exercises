import requests
from bs4 import BeautifulSoup

import sys
import locale# Addin your Language for Date time module
from datetime import datetime
locale.setlocale(locale.LC_ALL,"") # Addin your Language for Date time module

def upToDate_Values ():
    url = "https://www.doviz.com/"
    response = requests.get(url)
    content=response.content
    soup=BeautifulSoup(content,"html.parser")

    values=soup.findAll("span",{"class":"value"} )
    names=soup.findAll("span",{"class":"name"} )

    print("""
    ********************** Güncel Veriler **********************
    Tarih / Zaman : {}
    """.format(datetime.strftime(datetime.now(),"%Y %B %D %X")))

    mydict=dict()
    for name,value in zip(names,values):
        print(name.text,value.text)
        mydict[name.text]=value.text.replace(",",".") # Python doesnt allows the commas to converting float
    return mydict


mydict=upToDate_Values()

while True:
    usr_choice=input("""
    *************************************************************
    1-Verileri Güncelle
    2-Hedeften TL ye
    3-TL den Hedefe
    4-Çıkış
    Lütfen Seçim Yapınız >
    """)

    if usr_choice=="4":
        break


    if usr_choice=="1":
        mydict = upToDate_Values()


    if usr_choice=="2":
        while True:
            try:
                target=input("\nHedef birim giriniz (Örn : DOLAR ) >")
                amount=float(input("Miktar giriniz >"))
                break
            except ValueError :
                sys.stderr.write("Lütfen Uygun Formatta bir Miktar giriniz (Ondalıklı değerler için \".\" kullanınız )\n")
                sys.stderr.flush()

        try:
            if target=="Faiz":
                print("{} Tl 2 Yıllık {} = {} Tl".format(amount, target, float(mydict[target]) * (amount/100)))
            else:
                print("{} {} = {} TL ".format(amount,target,float(mydict[target])*(amount)))


        except KeyError:
            sys.stderr.write("Lütfen Doğru Birim Seçimi yapınız")
            sys.stderr.flush()

    if usr_choice =="3":
        while True:

            try:
                target=input("\nHedef birim giriniz (Örn : DOLAR ) >")
                amount=float(input("Miktar giriniz >"))
                break
            except ValueError :
                sys.stderr.write("Lütfen Uygun Formatta bir Miktar giriniz (Ondalıklı değerler için \".\" kullanınız )\n")
                sys.stderr.flush()

        try:
            if target=="Faiz":
                print("Bu seçim için faiz kullanılamamaktadır lütfen 2'yi seçiniz")
            else:
                print("{} Tl  = {} {} ".format(amount,(amount)/float(mydict[target]),target))
        except KeyError:
            sys.stderr.write("Lütfen Doğru Birim Seçimi yapınız")
            sys.stderr.flush()
