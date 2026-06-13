#TO-DO list
# crear lista vacia
# mostrar menu
# agregar tarea
# mostrar tareas
# salir

to_do = []

def agregar_tarea():      
  print("------------------------------------------------------------------------------------")
  print("Vamos a agregar tareas, puedes ingrear las tareas que quieras, solo tienes que poner . para terminar")
  
  while True:        #Agrega la cantidad de tareas que el usuario desee
    tarea = input("Ingrese la tarea que desea agregar: ").lower()
    
    if tarea.strip() == "":      #Si lo que el usuario ingresa esta vacio se le da un mensaje y la funcion termina
      print("Esta vacio, ingrese su tarea porfavor")
      continue
    
    if tarea == ".":      #Termina el bucle
      print(to_do)
      break

    to_do.append(tarea)        #Agrega las tareas a la lista
    print(to_do)
  
def eliminar_tarea():          #Elimina una tarea en especifico, eleccion del usuario
  print("------------------------------------------------------------------------------------")
  print("Vamos a eliminar una tarea")
  print(to_do)
  tarea = input("Ingrese la tarea que desea eliminar: ").lower()

  if tarea.strip() == "":          #Si esta vacio el programa sale de la funcion
    print("Esta vacio, ingrese su tarea a eliminar porfavor")
    return

  if tarea not in to_do:          #Por si la tarea que el usuario ingreso no esta en la lista
    print("Esta tarea no existe")
    return

  else: 
    to_do.remove(tarea)            #Elimina la tarea
    print(f"La tarea {tarea} ha sido eliminada")
    print(to_do)
    

while True:      #Bucle principal del menu
  print("-----------TO-DO LIST-----------")
  print("1. Agregar tarea")
  print("2. Eliminar tarea")
  print("3. Mostrar tareas")
  print("4. Eliminar todas las tareas")
  print("5. Salir")

  try:
    option = int(input("Ingrese el numero de la opcion que desee: "))
  except ValueError:
    print("Ingresa un valor numerico por favor")
    continue
  
  if option == 1:
    agregar_tarea()

  elif option == 2:
    eliminar_tarea()

  elif option == 3:      #Muestra todas las tareas
    print("------------------------------------------------------------------------------------")
    print("Estas son tus tareas")
    print(to_do)
  
  elif option == 4:      
    print("------------------------------------------------------------------------------------")
    print("Esta es la opcion para eliminar tu lista")
    eliminar = input("Estas seguro que quieres eliminar tu lista? (si/no): ").lower()

    if eliminar == "si":      #Esto elimina todas las tareas de la lista
      to_do.clear()
  
  elif option == 5:
    print("------------------------------------------------------------------------------------")

    if to_do == []:        #Si la lista esta vacia, no imprime la lista vacia
      print("Gracias por usar el programa, vuelva pronto")
      break

    else:
      print(to_do)        #Si la lista tiene tareas, imprime las tareas
      print("Gracias por usar el programa, vuelva pronto")
      break

  else:
    print("------------------------------------------------------------------------------------")
    print("Opcion no valida, intente de nuevo")
