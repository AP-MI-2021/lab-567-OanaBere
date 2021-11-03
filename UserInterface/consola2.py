from Domain.obiect import get_str
from Logic.general_logic import create, delete



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
                    else:
                        print("Optiune invalida! Tastati 'help' sau reincercati!")






