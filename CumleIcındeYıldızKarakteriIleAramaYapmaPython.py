
yerlesimYerleri=['Bolu','Yozgat','İnebolu','Manavgat','Çanakkale','Çan','Kırıkkale','Tirebolucuk']

def ara(kelime,altkelime):
    kucuk=kelime.lower()
    if altkelime[0]=='*':
        
        if kucuk.startswith(altkelime[1:].lower())  or kucuk.endswith(altkelime[1:].lower()):#altKelime[1:-1]neden olmuyo 
                                                                                             #çünkü o zaman -1'e kadar oluyo . 
                                                                                             #-1 indeksini almıyor.
                              return kelime
    if altkelime[0]=='*' and altkelime[-1]=='*':

        if kucuk.find(aranacakKelime[1:-1].lower())>-1:#-1 den büyük yapmamızın sebebi find bulamazsa -1 degerini döndürüyordu ya ondan.

            return kelime
    else:
        if kelime==altkelime:
            return kelime
def bul(altkelime):
    for u in yerlesimYerleri:
        r=ara(u,altkelime)
        if r:print(r)

aranacakKelime=input('Aramak istediginiz yerlesim yeri:')
bul(aranacakKelime)
