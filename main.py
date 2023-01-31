import sys
import random
import string

print("---Program Generujący Losowe Hasło---")

haslo = []
pozostale_znaki = -1


def update_pozostale_znaki(numer_znaku):
    global pozostale_znaki

    if numer_znaku < 0 or numer_znaku > pozostale_znaki:
        print("Liczba znaków spoza przedziału 0,", pozostale_znaki)
        sys.exit(0)

    else:
        pozostale_znaki -= numer_znaku
        print("Pozostało znaków:", pozostale_znaki)


dlugosc_hasla = int(input("Jak długie ma być hasło?: "))
if dlugosc_hasla < 5:
    print("Hasło jest zbyt krótkie. Musi miec min. 5 znaków")
    sys.exit(0)
else:
    pozostale_znaki = dlugosc_hasla

male_litery = int(input("Ile małych liter ma mieć hasło? "))
update_pozostale_znaki(male_litery)

duze_litery = int(input("Ile dużych liter ma mieć hasło? "))
update_pozostale_znaki(duze_litery)

znaki_specjalne = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_pozostale_znaki(znaki_specjalne)

cyfry = int(input("Ile cyf ma mieć hasło ?"))
update_pozostale_znaki(cyfry)

if pozostale_znaki > 0:
    print("Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnine małymi literami.")
    male_litery += pozostale_znaki

print("Długość hasła:", dlugosc_hasla)
print("Ilość małych liter:", male_litery)
print("Ilość dużych liter:", duze_litery)
print("Ilość znaków specjalnych:", znaki_specjalne)
print("Ilość cyfr:", cyfry)

for i in range(dlugosc_hasla):
    if male_litery > 0:
        haslo.append(random.choice(string.ascii_lowercase))
        male_litery -= 1

    if duze_litery > 0:
        haslo.append(random.choice(string.ascii_uppercase))
        duze_litery -= 1

    if znaki_specjalne > 0:
        haslo.append(random.choice(string.punctuation))
        znaki_specjalne = -1

    if cyfry > 0:
        haslo.append(random.choice(string.digits))
        cyfry -= 1

random.shuffle(haslo)
print("Wygenerowane hasło:", "".join(haslo))
