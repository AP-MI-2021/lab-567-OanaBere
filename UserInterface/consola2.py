from Domain.obiect import get_str, creare_obiect
from Logic.functionalitati import modify_location, concat_string_descriere
from Logic.general_logic import create, delete, update


def handle_update(obiecte,id_obiect,nume_obiect,descriere_obiect,pret_obiect,locatie_obiect):
    try:

        obiect = creare_obiect(id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
        return update(obiecte, obiect)
    except ValueError as ve:
        print('Eroare: ',ve)
    return obiecte

def showAll(lista_obiecte):
    for obiect in lista_obiecte:
        print(get_str(obiect))



def newMenu(obiecte):
    print('Introduceti "help" pentru a vedea comenzile disponibile sau introduceti comanda dorita: ')
    while True:
        mesaj = input()
        if mesaj == "help":
            print("add,id,nume,descriere,pret,locatie (exact 4 caractere!)")
            print("delete,id")
            print("showall")
            print("update,id,nume,descriere,pret,locatie")
            print("modify location,locatie initiala,locatie noua")
            print("concat,string,valoare")
            print("exit")
        else:
            optiuni = mesaj.split(";")
            if optiuni[0] == "exit":
                break
            else:
                for optiune in optiuni:
                    opt = optiune.split(",")
                    if opt[0] == "add":
                        try:
                            obiecte = create(obiecte, opt[1], opt[2], opt[3], int (opt[4]), str(opt[5]))

                        except ValueError as ve:
                            print("Eroare" , format(ve))
                    elif opt[0] == "delete":
                        try:
                            obiecte = delete(obiecte, int(opt[1]))
                        except ValueError as ve:
                            print("Eroare", ve)
                    elif opt[0] == "showall":
                        showAll(obiecte)
                    elif opt[0] == "update":
                        obiecte = handle_update(obiecte,int(opt[1]),str(opt[2]),str(opt[3]),int(opt[4]),str(opt[5]))
                    elif opt[0] == "modify location":
                        obiecte = modify_location(obiecte, str(opt[1]), str(opt[2]))
                    elif opt[0] == "concat":
                        obiecte = concat_string_descriere(obiecte, str(opt[1]), int(opt[2]))
                    else:
                        print("Optiune invalida! Tastati 'help' sau reincercati!")






