import random

objects = ["papel", "tijeras", "piedra"]

def computer_choice(objects):
    return random.choice(objects)

def countdown():
    for i in range(3, 0, -1):
        print(f"{i}...")

def play():
    player_choice = input("Ingresa tu eleccion: ").lower()
    bot_choice = computer_choice(objects)
    
    countdown()
    
    print(f"Tu eleccion: {player_choice}")
    print(f"Eleccion del bot: {bot_choice}")
        
    if player_choice == bot_choice:
        print(f"Empate! Ambos eligieron {player_choice}")
        if player_choice and bot_choice == "tijeras":
            print("ERES UNA LESBIANA xd")
        
    elif player_choice == "papel":
        if bot_choice == "tijeras":
            print("Perdiste! La tijera corta el papel, el bot gana!.")
        elif bot_choice == "piedra":
            print("Ganaste! El papel envuelve la piedra, tu ganas!.")
            
    elif player_choice == "tijeras":
        if bot_choice == "piedra":
            print("Perdiste! La piedra aplasta las tijeras, el bot gana!.")
        elif bot_choice == "papel":
            print("Ganaste! Las tijeras cortan el papel, tu ganas!.")
            
    elif player_choice == "piedra":
        if bot_choice == "papel":
            print("Perdiste! El papel envuelve la piedra, el bot gana!.")
        elif bot_choice == "tijeras":
            print("Ganaste! La piedra aplasta las tijeras, tu ganas!.")
    
    else:
        print("Tu eleccion no es valida, tal vez escribiste mal. Pofa intenta de nuevo.")

print("Vamos a jugar piedra, papel o tijeras!")

for intentos in range(3):
    play()