def asal_mi():
    for i in range(1,101):
        bolen=2
        counter=0
        while bolen<i:
            if i%bolen==0:
                counter+=1
            bolen+=1
        if counter==0:
            yield i
generator=asal_mi()
for i in generator:
    print(i)
