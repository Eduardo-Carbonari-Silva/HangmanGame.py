# IGOR, EDUARDO, VINICIUS, GABRIEL KENJI

import random

cont = 0
rodar = 1
listcarros = ["Maverick", "Lamborghini", "SkylineR34", "Supra", "Fusca", "Mobi", "Polo", "Fiesta", "Cruze", "Hilux", "S10"]
listfrutas = ["Banana", "Uva", "Kiwi", "Melancia", "Amora", "Laranja", "Abacaxi"]
letras_chutadas = []
chances = 6
ganhou = 0

escolha = int(input('Escolha o tema - 1 para carros e 2 para frutas: '))
   
if escolha == 1:
    palavra = random.choice(listcarros)
   
elif escolha == 2:
    palavra = random.choice(listfrutas)

while rodar == 1:

    forca = ['''
     +---+
     |   |
         |
         |
         |
         |    
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |    
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |    
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |    
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |    
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |    
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |    
    =========
    ''']
   
    print('* Jogo da Forca *')
    print(forca[cont])
    print("\n")
   
    for letra in palavra:
        if letra.lower() in letras_chutadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")
   
    tentativa = input("Escolha uma letra: ")
    letras_chutadas.append(tentativa.lower())
   
    if tentativa.lower() not in palavra.lower():
        chances -= 1
        cont += 1
   
    ganhou = 1
    for letra in palavra:
        if letra.lower() not in letras_chutadas:
            ganhou = 0
   
    if chances == 0 or ganhou == 1:
        rodar = 0
   
if ganhou == 1:
    print(f"Parabens! você acertou, a palavra era: {palavra}")
    print("You are the GOAT!!!")
   
else:
    print(f"Que pena, você perdeu! a palavra era: {palavra}")