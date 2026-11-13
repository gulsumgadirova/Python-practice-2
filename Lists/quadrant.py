x = int(input("X koordinatini daxil edin: "))
y = int(input("Y koordinatini daxil edin: "))

point = (x, y)
if x > 0 and y > 0:
    print("I rub")
elif x < 0 and y > 0:
    print("II rub")
elif x < 0 and y < 0:
    print("III rub")
elif x > 0 and y < 0:
    print("IV rub")
elif x == 0 and y == 0:
    print("Merkez")
else:
    print("Oxun uzerindedir") 