#menu suma y resta
while True:
    print(""".........MENU.........
       1. suma
       2. resta
       3. salir""")
    option = int(input("Ingrese opcion: "))

    if option == 1:
        print("Usted eligio la opcion de SUMA")
        num1 = int(input("Ingrese primer numero: "))
        num2 = int(input("Ingrese segundo valor: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        
    elif option == 2:
        print("Usted eligio la opcion de RESTA")
        num1 = int(input("Ingrese primer valor: "))
        num2 = int(input("Ingrese segundo valor: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        
    elif option == 3:
        print("Gracias por usar el programa")
        break
    else:
        print("Elija una de las opciones disponibles")


## MENU LOCO
#desarrolle un algoritmo que genere un menu interactivo que NO haga caso al usuario
#4 opciones
# 1. Saludar
# 2. Sumar
# 3. El usuario ingrese 5 numeros (por separado) y q diga cual es el mayor
# 4. salir
def mayor():
    print("Ingrese 5 valores")
    num_1 = int(input("primer numero:"))
    num_2 = int(input("segundo numero"))
    num_3 = int(input("tercer numero"))
    num_4 = int(input("cuarto numero"))
    num_5 = int(input("quinto numero"))

    if num_1 > num_2 and num_1 > num_3 and num_1 > num_4 and num_1 > num_5:
        print(f"El numero {num_1} es mayor")
        
    elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4 and num_2 > num_5:
        print(f"El numero {num_2} es mayor")
        
    elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4 and num_3 > num_5:
        print(f"El numero {num_3} es mayor")
        
    elif num_4 > num_1 and num_4 > num_2 and num_4 > num_3 and num_4 > num_5:
        print(f"El numero {num_4}es mayor")
        
    elif num_5 > num_1 and num_5 > num_2 and num_5 > num_3 and num_5 > num_4:
        print(f"El numero {num_5} es mayor")


while True:
    print("........MENU LOCO........")
    print("1. Saludo")
    print("2. Suma")
    print("3. ¿Cual es el mayor?")
    print("4. Salir")
    option = int(input("Ingrese su opcion deseada: "))

    if option == 1:
        print("Vamos a sumar :D")
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo valro: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        
    if option == 3:
        print("Holaaaaaa mundooooo")
    
    if option == 2:
        mayor()

    if option == 4:
        print("Grcias por usar el programa")
        break
