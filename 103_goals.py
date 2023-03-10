def ficha(name="unknown", goals="0"):
    
    if name=="":
        name="unknown"
    if goals == "":
        goals="0"
    
    string = name + " did " + goals + " goals"
    
    return string
    
jogador = input("Type the name of the player: ") 
gols = input("Type the number of goals: ")

print(ficha(jogador, gols)) 
