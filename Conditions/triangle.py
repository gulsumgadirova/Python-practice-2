a = int(input("Birinci terefi daxil edin: "))
b = int(input("Ikinci terefi daxil edin: "))
c = int(input("Ucuncu terefi daxil edin: "))

if a+b>c and a+c>b and b+c>a:
    print("Bu ucbucaq mumkundur")

if a==b and b==c:
    print("Bu ucbucaq berabere tereflidir")
elif a==b or b==c or a==c:
    print("Bu ucbucaq muxtelif tereflidir")

    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Bu ucbucaq duz bucaqli ucbucaqdir")  
    else:
        print("Bu ucbucaq duz bucaqli ucbucaq deyil")
else:
        print("Bu ucbucaq mumkun deyil")
        