from Domain.obiect import creare_obiect, get_str

from Logic.functionalitati import modify_location, concat_string_descriere, pret_maxim_locatie, \
    ord_cresc_dupa_pret_achizitie, suma_pret_per_locatie
from Logic.general_logic import delete, read, update, create


def printMeniu():
    print('1. Adaugare obiect.')
    print('2. Afisare obiecte.')
    print('3. Stergere obiect.')
    print('4. Modificare obiect.')
    print('5. Detalii obiect.')
    print('6. Mutare obiecte intr-o alta locatie.')
    print('7. Concatenarea unui string la descrierea unui obiect care are pretul mai mare decat o valoare data.')
    print('8. Afisarea celui mai mare pret pentru fiecare locatie')
    print('9. Ordonarea obiectelor in ordine crescatoare dupa pretul achizitiei ')
    print('10. Afisare suma preturilor pentru fiecare locatie.')
    print('a. undo')
    print('b. redo')
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
        print('Eroare: ', ve)
    return obiecte

def handle_details(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului despre care vreti detalii:"))
        obiect = read(obiecte, id_obiect)
        return get_str(obiect)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_show_all(list_obiecte):
     for obiect in list_obiecte:
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
        print("Eroare: ", ve)
    return obiecte

def handle_pret_maxim_locatie(obiecte):
    result = pret_maxim_locatie(obiecte)
    for locatie in result:
        print("Locatia {} are pretul maxim {}".format(locatie, result[locatie]))


def handle_ord_cresc_dupa_pret_achizitie(obiecte):
    try:
        obiecte = ord_cresc_dupa_pret_achizitie(obiecte)
        return handle_show_all(obiecte)
    except ValueError as ve:
        print('Eroare:', ve)
    return obiecte



def handle_suma_pret_per_locatie(obiecte):
    result = suma_pret_per_locatie(obiecte)
    for locatie in result:
        print(f'{locatie} are suma preturilor {result[locatie]}')

def handle_new_list(list_versions, current_version, prajituri):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(prajituri)
    current_version += 1
    return list_versions, current_version

def handle_undo(list_versions, current_version):
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return list_versions[current_version], current_version
    current_version -= 1
    return list_versions[current_version], current_version

def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return list_versions[current_version], current_version
    current_version += 1
    return list_versions[current_version], current_version




def run_Menu(obiecte):
    list_versions = [obiecte]
    current_version = 0
    while True:
        printMeniu()
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte = handle_add(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '2':
            handle_show_all(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '3':
            obiecte = handle_delete(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '4':
            obiecte = handle_modify_object(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '5':
            print(handle_details(obiecte))
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '6':
            obiecte = handle_modify_location(obiecte)
            print(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '7':
            obiecte = handle_concat_string_descriere(obiecte)
            print(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '8':
            obiecte = handle_pret_maxim_locatie(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '9':
            obiecte = handle_ord_cresc_dupa_pret_achizitie(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '10':
            obiecte = handle_suma_pret_per_locatie(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == 'a':
            obiecte, current_version = handle_undo(list_versions, current_version)
        elif optiune == 'b':
            obiecte, current_version = handle_redo(list_versions, current_version)

        elif optiune == 'x':
            break
        else:
            print("Optiune invalida!")
    return obiecte