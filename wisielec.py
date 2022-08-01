import random
print("Witaj w wisielcu, podaj swoje imię: ")
imie = input()

lista = ["sekret","dupa","woda","monitor","pajton"]
haslo = str(lista[random.randint(0,len(lista) -1)])
tablica = list(haslo)

for i in range(len(haslo)):
    tablica[i] = "_"

zycia = 6

while zycia > 0:
    print(" ")
    print(imie, "Pozostało ci ", zycia, 'zyc')
    print(" ".join(tablica))
    print(" ")
    print("Podaj swoją litere: ")

    litera = input()

    if litera in haslo:
        for i in range(len(haslo)):
            if(haslo[i]) == litera:
                tablica[i] = litera
        if tablica == list(haslo):
            print("Gratulacja, wygrałes słowo to", haslo)
            break
    else:
        zycia -= 1
        if zycia == 0:
            print("Przegrałes", haslo)
