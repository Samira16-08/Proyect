#Conversion de unidades
#El usuario ingresa de que grados a que grados va a transformar, Fahrenheit o celsius

grades = {"celsius":["°C", "C", "°C A °F", "C A F"], "fahrenheit":["°F", "F", "°F A °C", "F A C"]}  #Variantes de posibles entradas del usuario

while True:
  grade = input("Ingrese la unidad de grado quiere transformar (°C a °F o °F a °C): ").upper()    #Entrada de que tipo de transformacion quiere el usuario y transformandola toda en mayusculas

  if grade in grades["celsius"]:    #Transformacion de celsius a fahrenheit
    print("Tranformacion de Celsius a Fahrenheit")

    try:
      celsius = float(input("Ingrese los grados celsius a transformar (solo el numero): "))   
    except ValueError:
      print("Ingresa un valor numerico")
      continue       #Se salta la iteracion del codigo

    fahrenheit = (celsius*9/5) + 32                #Ecuacion de transformacion de celsius a fahrenheit 
    print(f"{celsius}°C son {fahrenheit:.2f}°F")        #Resultado de la transformacion
    break

  elif grade in grades["fahrenheit"]:   #Transformacion de fahrenheit a celcius
    print("Transformacion de Fahrenhei a Celsius")
    try:
      fahrenheit = float(input("Ingrese los grados fahrenheit a transformar (solo el numero): "))
       
    except ValueError:
      print("Ingresa un valor numerico")
      continue       #Se salta la iteracion del codigo
      
    celsius = (fahrenheit - 32) * 5/9              #Ecuacion de transformacion de fahrenheit a celsius
    print(f"{fahrenheit}°F son {celsius:.2f}°C")       #Resultado de la transformacion
    break

  else:
    print("Grado no valido, intente de nuevo")
