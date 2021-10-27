from Domain.obiect2 import get_str, getNewObject
from Logic.general_logic import delete, read, update, create


def meniu():
    print('1. CRUD')
    print('2. Mutarea tuturor obiectelor dintr-o locatie in alta')
    print('3. Concatenarea unui string citit la toate descrierile obiectelor'
          ' cu prețul mai mare decât o valoare citită.')
    print('4. Determinarea celui mai mare preț pentru fiecare locație.')
    print('5. Ordonarea obiectelor crescător după prețul de achiziție.')
    print('6. Afișarea sumelor prețurilor pentru fiecare locație.')
    print('7. Undo.')
    print('x. Iesire')


def handle_add(obiecte):
    id_obiect = int(input("Dati id-ul:"))
    nume_obiect = input("Dati numele obiectului:")
    descriere_obiect = input("Dati descrierea obiectului:")
    pret_obiect = int(input("Dati pretul:"))
    locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
    return create(obiecte, id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)


def handle_delete(obiecte):
    id_obiect = int(input("Dati id-ul elementului pe care doriti sa il stergeti:"))
    return delete(obiecte, id_obiect)


def handle_up(obiecte):
    id_obiect = int(input("Dati id-ul obiectului pe care doriti sa il modificati:"))
    nume_obiect = input("Dati numele obiectului:")
    descriere_obiect = input("Dati numele obiectului:")
    pret_obiect = int(input("Dati pretul:"))
    locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
    obiect = getNewObject(id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
    return update(obiecte, obiect)


def handle_detalii(obiecte):
    id_obiect = int(input("Dati id-ul obiectului despre care vreti detalii:"))
    obiect = read(obiecte, id_obiect)
    return get_str(obiect)


def handle_show_all(obiecte):
    for obiect in obiecte:
        print(get_str(obiect))


def meniu_crud(obiecte):
    while True:
        print("1. Adaugare obiect")
        print("2. Detalii obiect")
        print("3. Actualizare obiect")
        print("4. Stergere obiect")
        print("5. Afisare")
        print("6. Revenire")
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            print(handle_detalii(obiecte))
        elif optiune == '3':
            obiecte = handle_up(obiecte)
        elif optiune == '4':
            obiecte = handle_delete(obiecte)
        elif optiune == '5':
            handle_show_all(obiecte)
        elif optiune == '6':
            break
        else:
            print("Optiune invalida")


def run_ui(obiecte):
    while True:
        meniu()
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            meniu_crud(obiecte)
        else:
            break