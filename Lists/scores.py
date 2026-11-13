scores = [78, 92, 65, 88, 100, 54, 91, 73]
print ("En yuksek bal:", max(scores))
print ("En asagi bal:", min(scores))
print ("Netice sayi:", len(scores))
scores.sort()
print ("Siralanmis ballar:", scores)
print ("En yaxsi 3 netice:", scores[-3:])
bal = int(input("Bal daxil edin:"))
if bal in scores:
    print ("Siyahida var")
else:
    print ("Siyahida yoxdur")
