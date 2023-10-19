import random
from os import name, system

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def loadingWord():
    print("Loading ...")
    words = []
    file = open("palavras.txt", "r")

    for line in file: words.append(line.strip())
    
    file.close()

    if len(words) == 0: 
        clear()
        return "Zebra"

    return words[random.randrange(0, len(words))]

def welcome():
    print("**********************************************")
    print("**********************************************")
    print("********* Bem vindo ao jogo da Forca *********")
    print("**********************************************")
    print("**********************************************\n\n\n")

def endgame(isWin, word):
    print("\nFim do jogo\n")

    if (isWin): win()
    else: gameOver()

    print("A palavra era: {}".format(word))

def win():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def gameOver():
    print("Puxa, você foi enforcado!")
    print("       ░░░░░░░░░░░░       ")
    print("    ░░░░            ░░░░    ")
    print("  ░░                    ░░  ")
    print("  ░░                    ░░  ")
    print("  ░░                    ░░  ")
    print("░░    ██████    ██████    ░░")
    print("░░  ████████    ████████  ░░")
    print("░░  ████████    ████████  ░░")
    print("░░    ████        ████    ░░")
    print("░░                        ░░")
    print("  ░░        ████        ░░  ")
    print("    ░░      ████      ░░    ")
    print("      ░░            ░░      ")
    print("      ░░            ░░      ")
    print("      ░░  ██    ██  ░░      ")
    print("        ░░░░░░░░░░░░ ")

def draw_forca(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(errors == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(errors == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(errors == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(errors == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(errors == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (errors == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def printListLetters(charList = []):
    for char in charList:
        print("{} ".format(char), end="")

def play():
    word = loadingWord()
    welcome()

    char = "_"
    charList = [char for letter in word]
    isGameOver = False
    isWin = False
    errors = 0


    # for i in range(len(word)):
    #     charList.append(char)

    printListLetters(charList)

    print("\n\n\n")
    while (not isGameOver and not isWin):
        attempt = ""
        invalidAttempt = True
        while (invalidAttempt):
            attempt = input("\nQual letra?\t").strip()
            if attempt.isalpha() and len(attempt) == 1:
                invalidAttempt = False
                break

            print("Chute inválido! Por favor, informe apenas letras!\n")

        if (attempt.lower() in word.lower()):
            index = 0
            for letter in word:
                if (attempt.lower() == letter.lower()):
                    ##print("Encontrei a letra {} na posição {}".format(letra, index))
                    charList[index] = letter
                index = index + 1
        else:
            errors += 1
            draw_forca(errors)
    
        isGameOver = errors == 6
        isWin = char not in charList
        
        printListLetters(charList)

    endgame(isWin, word)

if (__name__ == "__main__"):
    play()