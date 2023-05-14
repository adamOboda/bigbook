# Mój własny program do gry w bajgle

import random

NUMERY = 3
ZGADYWANIE = 10

def main():

    print('''Bajgle, logiczna gra na dedukcje.
    Autor: Adam Oboda
    
    Mam na myśli {}-cyfrową liczbę, w której nie powtarza się żadna z cyfr.
    Spróbuj ją odgadnąć. Oto wskazówki:
    Gdy mówię:      Oznacza to:
    Piko        Jedna cyfra jest poprawna, ale jest na złej pozycji.
    Fermi       Jedna cyfra jest poprawna i znajduje się w odpowiednim miejscu.
    Bajgle      Żadna cyfra nie jest poprawna.
    Na przykład, jeśli tajna liczba to 248, a Ty podasz liczbę 843, 
    wskazówka będzie brzmieć Fermi Piko.'''.format(NUMERY))

    while True:
        secretNum = getSecretNum()
        print("Mam na myśli liczbę...")
        print("Masz {} prób, by odgadnąć moją liczbę.".format(ZGADYWANIE))

        num_guesses = 1
        while num_guesses <= ZGADYWANIE:
            guess = ''
            while len(guess) != NUMERY or not guess.isdecimal():
                print("Próba {}".format(num_guesses))
                guess = input('> ')

            clues = getclues(guess, secretNum)
            print(clues)
            num_guesses +=1

            if guess == secretNum:
                break
            if num_guesses > ZGADYWANIE:
                print("Wykorzystałeś maskymalną liczbę prób")
                print("Prawidłowa odpowiedź to: {}".format(secretNum))

        print("Czy chcesz zagrać jeszcze raz ? (tak lub nie)")
        if input("> ").lower().startswith('n'):
            break
    print("Dziękuję za grę")


#Potrzebne funkcje: getSecretNum, getclues

def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum = ''

    for i in range(NUMERY):
        secretNum += str(numbers[i])
    return secretNum

def getclues(guess, secretNum):

    if guess == secretNum:
        return "Udało się"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Piko")

    if len(clues) == 0:
        return "Bajgle"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()