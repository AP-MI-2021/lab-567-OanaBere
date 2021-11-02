from Domain.obiect import creare_obiect, get_str

from Logic.functionalitati import modify_location, concat_string_descriere
from Logic.general_logic import delete, read, update, create


def printMeniu():
    print('1. Adaugare obiect.')
    print('2. Afisare obiecte.')
    print('3. Stergere obiect.')
    print('4. Modificare obiect.')
    print('5. Detalii obiect.')
    print('6. Mutare obiecte intr-o alta locatie.')
    print('7. Concatenarea unui string la descrierea unui obiect care are pretul mai mare decat o valoare data.')
    print('x. Iesire')


def handle_add(obiecte):
    try:
        id_obiect = int(input("Dati id-ul:"))
        nume_obiect = input("Dati numele obiectului:")
        descriere_obiect = input("Dati descrierea obiectului:")
        pret_obiect = int(input("Dati pretul:"))
        locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
        return create(obiecte, id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte

def handle_delete(obiect):
    try:
        id_obiect = int(input("Dati id-ul obiectului pe care doriti sa il stergeti:"))
        return delete(obiect, id_obiect)
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiect

def handle_modify_object(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului pe care doriti sa il modificati:"))
        nume_obiect = input("Dati numele obiectului:")
        descriere_obiect = input("Dati descrierea obiectului:")
        pret_obiect = int(input("Dati pretul:"))
        locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
        obiect = creare_obiect(id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
        return update(obiecte, obiect)
    except ValueError as ve:
        print('Eroare: ',ve)
    return obiecte

def handle_details(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului despre care vreti detalii:"))
        obiect = read(obiecte, id_obiect)
        return get_str(obiect)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_show_all(obiecte):
     for obiect in obiecte:
         print(get_str(obiect))



def handle_modify_location(obiecte):
    try:
        locatie_initiala = input("Dati locatia din care sa se mute obiectele (4 caractere):")
        locatie_noua = input("Dati locatia in care sa se mute obiectele (4 caractere):")
        obiecte = modify_location(obiecte, locatie_initiala, locatie_noua)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte

def handle_concat_string_descriere(obiecte):
    try:
        string = input("Dati string-ul care va fi adaugat la descrierea obiectului: ")
        valoare = int(input("Dati o valoare pentru a compara pretul obiectului: "))
        obiecte = concat_string_descriere(obiecte, string, valoare)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def run_Menu(obiecte):
    while True:
        printMeniu()
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            handle_show_all(obiecte)
        elif optiune == '3':
            obiecte = handle_delete(obiecte)
        elif optiune == '4':
            obiecte = handle_modify_object(obiecte)
        elif optiune == '5':
            print(handle_details(obiecte))
        elif optiune == '6':
            obiecte = handle_modify_location(obiecte)
            print(obiecte)
        elif optiune == '7':
            obiecte = handle_concat_string_descriere(obiecte)
            print(obiecte)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida!")