import random

NUM_DIGITS = 3
MAX_GUESSES = 10


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
    wskazówka będzie brzmieć Fermi Piko.'''.format(NUM_DIGITS))

    while True:  # pętla główna  asas
        secretNum = getSecretNum()
        print('Mam na myśli liczbę.')
        print('Masz {} prób, by odgadnąć jaka to liczba.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Próba #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # podana liczba jest poprawna - zakończ pętlę
            if numGuesses > MAX_GUESSES:
                print('Wykorzystałeś wszystkie próby.')
                print('Prawidłowa odpowiedź to: {}.'.format(secretNum))

        print('Czy chcesz zagrać jeszcze raz ? (tak lub nie)')
        if not input('> ').lower().startswith('t'):
            break
    print('dziękuję za grę')


# deklaracja funkcji:
def getSecretNum():
    # Zwracam liczbę z tylu cyfr ile wynosi wartość NUM_DIGITS
    numbers = list('0123456789')
    random.shuffle(numbers)

    # Dodaje kolejne cyfry do tajemniej liczby:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    # Zwracam se łańcuch znaków piko, fermi i bajgle
    if guess == secretNum:
        return 'Udało się!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Piko')

    if len(clues) == 0:
        return 'Bajgle'
    else:
        # Ustawiam wskazówki w kolejności alfabetycznej, aby nie zdradzac za dużo szczegółów:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
    # powinno chodzić
