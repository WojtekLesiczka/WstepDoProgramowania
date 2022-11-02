print("1) dodawanie 2) odejmowanie 3) mnożenie 4) dzielenie 5) potęgowanie")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

x = int(input("Jaką operację chcesz wykonać?"))
y=0
if x == 1:
    y = a + b
elif x == 2:
    y = a - b
elif x == 3:
    y = a * b
elif x == 4:
    y = a / b
elif x == 5:
    y = a ** b


print("wynik to: ",y)