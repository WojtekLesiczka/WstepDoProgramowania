a = int(input("Podaj pierwszą liczbę  "))
b = int(input("Podaj drugą liczbę  "))

while a < b:
  a += 1
  if a%2:
    continue 
  print(a)
  
while b < a:
  b += 1 
  if b%2:
    continue
  print(b)

"""
x=0
for x in range(a,b):
  x +=1
  print(x)
"""