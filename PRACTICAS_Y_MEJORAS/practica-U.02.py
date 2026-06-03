#MENU LOCO REMASTERIZADO
## MENU LOCO
#desarrolle un algoritmo que genere un menu interactivo que NO haga caso al usuario
#4 opciones
# 1. Saludar
# 2. Sumar
# 3. El usuario ingrese 5 numeros (por separado) y q diga cual es el mayor
# 4. salir

import random

def mayor():
  print("Ingrese 5 numeros para determinar cual es el mayor y cual es el menor")
  nums = [int(input("Ingrese su numero: ")) for _ in range(5)]

  print(f"El numero mayor es {max(nums)}")
  print(f"El numero menor es {min(nums)}")

def suma():
  print("Vamos a sumar numeros (presiona 0 para salir)")

  nums = []
  while True:
    num = int(input("Ingresa un valor: "))
    if num == 0:
      print("Sumando...")
      print(sum(nums))
      break
      
    nums.append(num)

while True:
  print("-----------MENU LOCO-----------")
  print("1. Saludar")
  print("2. Sumar")
  print("3. Determinar mayor y menor")
  print("4. Salir")
  
  option = int(input("Ingrese su opcion: "))
  random_option = random.choice([1, 2, 3])

  if option not in [1, 2, 3, 4]:
    print("--------------------------------------------")
    print("Te salvaste esta vez... Pero volvere 7-7")
    break

  if option == 4:
    print("--------------------------------------------")
    print("No vas a salir de aqui NUNCAAAAAAAAAAA")
    
  elif random_option == 2:
    print("--------------------------------------------")
    suma()

  elif random_option == 3:
    print("--------------------------------------------")
    mayor()

  elif random_option == 1:
    print("--------------------------------------------")
    print("BUENOS DIAS ESTRELLITAS, LA TIERRA LES DICE HOLAAAAAAAAAAAAAAAA")
