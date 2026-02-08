print("Welcome to the CURRENCY CONVERTER(in rupees only)")
print('If you looking for factorial of your given number,then just write it.')
print("for currency add prefix as given.For Quit the program just write QUIT.")
dict={"doller": "$",
       "dhiram": "D", 
       "euro": "E", 
       "iranian_rial": "!",
         "venezuelan_bolivar": "V", 
         "south_korean_won": "S", 
         "north_korean_won": "N", 
         "british_pound": "B", 
         "russian_rubel": "R"}
print(dict)
#starting fuctions.
n = input("Enter the number:")
def factorial(n):
    fac = 1
    for i in range (1,n+1):
     fac *= i
    return fac

def doller(n):
 doll = float(n/90.31)
 return doll

def dhiram(n):
  dhir = float(n/24.63)
  return dhir

def Euro(n):
  euro = float(n/106.43)
  return euro

def iranian_rial(n):
  iran= float(n/0.000074)
  return iran

def venezula(n):
  ven=float(n/0.25)
  return ven 

def south_korean_won(n):
  s_won=float(n/0.62)
  return s_won

def north_korean_won(n):
  n_won= float(n/0.15)
  return n_won

def british_pound(n):
  pound=float(n/122.65)
  return pound

def russian_rubel(n):
  rubel=float(n/1.18)
  return rubel

#conditional statement.
if n.isdigit():
  print("factorial is",(factorial(int(n))),)
elif n.startswith("$"):
  print(n,"In Doller is :",doller(int(n[1:])))
elif n.startswith("D"):
  print(n,"In Dhiram is:",dhiram(int(n[1:])))
elif n.startswith("E"):
  print(n,"In Euro is:",Euro(int(n[1:])))
elif n.startswith("!"):
  print(n,"In Iranian Rial is:",iranian_rial(int(n[1:])))
elif n.startswith("V"):
  print(n,"In Venezuelan Bolivar is:",venezula(int(n[1:])))
elif n.startswith("S"):
  print(n,"In South Korean Won is:",south_korean_won(int(n[1:])))
elif n.startswith("N"):
  print(n,"In North Korean Won is:",north_korean_won(int(n[1:])))
elif n.startswith("B"):
  print(n,"In British Pound is:",british_pound(int(n[1:])))
elif n.startswith("R"):
  print(n,"In Russian Rubel is:",russian_rubel(int(n[1:])))


else:
  print("Invalid input.")
  
while True:
  n = input("Enter the number:")
  if n.upper() == "QUIT":
    break
  if n.isdigit():
    print("factorial is",(factorial(int(n))),)
  elif n.startswith("$"):
    print(n,"In Doller is :",doller(int(n[1:])))
  elif n.startswith("D"):
    print(n,"In Dhiram is:",dhiram(int(n[1:])))
  elif n.startswith("E"):
    print(n,"In Euro is:",Euro(int(n[1:])))
  elif n.startswith("!"):
    print(n,"In Iranian Rial is:",iranian_rial(int(n[1:])))
  elif n.startswith("V"):
    print(n,"In Venezuelan Bolivar is:",venezula(int(n[1:])))
  elif n.startswith("S"):
    print(n,"In South Korean Won is:",south_korean_won(int(n[1:])))
  elif n.startswith("N"):
    print(n,"In North Korean Won is:",north_korean_won(int(n[1:])))
  elif n.startswith("B"):
    print(n,"In British Pound is:",british_pound(int(n[1:])))
  elif n.startswith("R"):
    print(n,"In Russian Rubel is:",russian_rubel(int(n[1:])))
  else:
    print("Invalid input.")
