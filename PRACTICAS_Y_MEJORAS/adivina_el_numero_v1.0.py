#ADIVINA EL NUMERO
import random

#El programa genera un numero
random_num = random.randint(1, 5)      #Rango de numeros donde se aplicara random
intentos = 3

print("Vamos a jugar adivina el numero, el programa escogera un numero del 1 al 5, tienes 3 intentos. SUERTE")

while True:
  try:        #Verifica que el dato ingresado sea un numero
    num_user = int(input("Ingresa tu numero: "))

  except ValueError:
    print("Ingresa un valor numerico porfavor")
    continue 

  if num_user == random_num:      #Compara el dato del usuario con el de el programa e imprime victoria
    print(f"FELICIDADES. TU GANAS, el numero era {random_num}, buen trabajo ")
    print("Gracias por usar el programa, vuelva pronto")
    break
  
  elif random_num > num_user:        #Determina si el numero a adivinar es menor o mayor
    print("El numero es mayor")

  else:
    print("El numero es menor")
  
  intentos -= 1             #Resta de intentos (esto se puede mejorar)
  print(f"Te quedan {intentos} intenos")

  if intentos == 0:        #Fin del programa, el usuario pierde porque se quedo sin intentos
    print(f"Perdiste, te quedaste sin intentos. El numero era {random_num}")
    print("Suerte para la proxima y gracias por usar el programa, vuelva pronto")
    break
  

