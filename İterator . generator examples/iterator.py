class kareler():
    def __init__(self,maximum=0):
        self.max=maximum
        self.sayı=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.sayı != self.max+1:
            sonuc=self.sayı**2
            self.sayı+=1
            return sonuc

        else:
            self.sayı=1
            raise StopIteration

kare=kareler(5)
iteration=iter(kare)
