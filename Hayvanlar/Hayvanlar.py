class Hayvanlar():
    def __init__(ortak,isim="İsimsiz",Solunum="Bilgi Yok",Beslenme="Bilgi Yok",Yaşam_alanı="Bilgi Yok",boy=0,kilo=0):
        ortak.Beslenme=Beslenme
        ortak.Solunum=Solunum
        ortak.Yaşam_alanı=Yaşam_alanı
        ortak.boy=boy
        ortak.kilo=kilo
        ortak.isim=isim
    def __str__(ortak):
       return """
        İsim : {}
        Solunum : {}
        Beslenme : {}
        Yaşam alanı : {}
        Boy : {}
        Kilo :{}
        """.format(ortak.isim,ortak.Solunum,ortak.Beslenme,ortak.Yaşam_alanı,ortak.boy,ortak.kilo)
    def __len__(ortak):
        return ortak.boy



class dogs (Hayvanlar):
    global liste
    def __init__(kopek,isim="Belirlitmedi", Solunum="Bilgi Yok", Beslenme="Bilgi Yok", Yaşam_alanı="Bilgi Yok",boy=0,kilo=0,irk="Belirtilmemiş"):
        super().__init__(isim,Solunum,Beslenme,Yaşam_alanı,boy,kilo)
        kopek.irk=irk
    def __str__(self):

        return """
           Tür: Köpek
           İsim : {}
           Solunum : {}
           Beslenme : {}
           Yaşam alanı : {}
           Boy : {}
           Kilo :{}
           Irk : {}
           """.format(self.isim,self.Solunum, self.Beslenme, self.Yaşam_alanı, self.boy, self.kilo, self.irk)



def kunye (index):
    global isimlistesi
    try:
        i=isimlistesi.index(index)
        print(liste[i])
    except ValueError:
        print("Listede Bulunamadı")
isimlistesi=[]
liste=[]
liste.append(dogs("Karabaş","Akciğer","Etçil","Habitat Seçmiyor",132,45,"Sokak Köpeği"))
liste.append(dogs("Çomar","Akciğer","Etçil","Kırsal",167,110,"1"))
for i in range(0,len(liste)):
    isimlistesi.append(liste[i].isim)

while True:
    print("""
    ********* MENÜ *********
    1-Hayvan Ekle
    2-İsimden Künye Çıkar
    3-Hayvan Sil
    'q'- Programı Kapat
    """)
    secim=input("Seçim Yapnız >")
    if secim=="q":
        break
    if secim== "1":
        print("""
        1-Köpek
        2-Kuş
        3-At
        """)
        altsecim=input("Seçim Yapnız >")
        if altsecim=="1":
            while True:
                try:
                    isim=input("İsim :")
                    solunum = input("Solunum Türü :")
                    beslenme = input("Beslenme Türü :")
                    ya = input("Yaşam Alanı Türü :")
                    kilo = int(input("Kilo :"))
                    boy = int(input("Boy :"))
                    irk = input("Irk :")
                except ValueError:
                    print("Hatalı Türden Giriş Yapıldı !")

                liste.append(dogs(isim,solunum,beslenme,ya,boy,kilo,irk))
                a = input("cikmak icin q basın")

                if a == 'q':
                    break
        for i in range(0,len(liste)):
            print(liste[i])


    if secim=='2':
        isim=input("İsim : ")
        kunye(isim)
