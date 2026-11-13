cart = []
cart.append("alma")
cart.append("corek")
cart.append("sud")
cart.append("yumurta")

cart.remove("sud")
mehsul = input("Mehsul daxil edin:")
if mehsul in cart:
    print ("Siyahida var")
else:
    print ("Siyahida yoxdur")

    cart.sort()
    print("Sebet:", cart)
    print("Sebetdeki mehsul sayi:", len(cart))
    