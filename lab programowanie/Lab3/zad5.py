liczba_studentow = int(input("Podaj liczbe studentow: "))
 
counter = liczba_studentow
srednia_punktow = 0

while (counter > 0):
    srednia_punktow += int(input("Punkty studenta nr " + str(counter) + ": "))
    counter -= 1
 
srednia_punktow /= liczba_studentow
 
print("Srednia punktow wynosila ", srednia_punktow)