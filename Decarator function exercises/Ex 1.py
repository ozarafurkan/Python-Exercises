def ekstra (fonk):
    def wrapped(sayilar):
        print("Mukemmel Sayılar")
        for i in sayilar:
            x=1
            sum=0
            while (x<i):
                if i%x==0:
                    sum+=x
                x+=1
            if sum==i:
                print(i)
        fonk(sayilar)
    return wrapped
#tanımlandı
@ekstra
def asalliste(sayilar):
    print("Asal sayılar ... ")
    asal=True
    for i in sayilar:
        if i ==1 :
            asal=False
        for j in range(2,i):
            if (i%j==0 )and( i!=2 )and (i!=j) :
                asal=False
                break
        if asal==True:
            print(i)
        asal=True
