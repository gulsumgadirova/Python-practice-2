saat = int(input("Saat daxil edin: "))
deqiqe = int(input("Dəqiqə daxil edin:"))
saniye = int(input("Saniye daxil edin:"))

saniye += 1

if saniye == 60:
    saniye = 0
    deqiqe += 1
if deqiqe == 60:
    deqiqe = 0
    saat += 1
    if saat == 24:
        saat = 0
        print ("Saat, dəqiqə, saniyə:", saat, deqiqe, saniye)
        
             