from Domain import obiect
from Domain.obiect import get_locatie, get_id, get_nume, get_descriere, get_pret, creare_obiect



def modify_location(list_objects, initial_location, new_location):
    '''
    functie care muta obiectele din locatia initiala intr-o alta locatie
    :param list_objects: lista de obiecte
    :param new_location: locatia noua
    :param initial_location: locatia initiala
    :return:lista cu obiectele mutate in noua locatie sau lista initiala daca locatia initiala este invalida
    '''
    if len(new_location) != 4 or len(initial_location) != 4:
        raise ValueError(f'Locatia a fost introdusa gresit! Trebuie sa aiba exact 4 caractere!')
    new_list = []
    for object in list_objects:
        if get_locatie(object) == initial_location:

            new_object = creare_obiect(get_id(object), get_nume(object), get_descriere(object), get_pret(object), new_location)
            new_list.append(new_object)
        else:
            new_list.append(object)
    return new_list


def concat_string_descriere(lst_obiecte, string, valoare):
    '''
    functie care concateneaza un string citit la descrierea obiectelor a caror pret este mai mare decat o valoare citita
    :param lst_obiecte:lista de obiecte
    :param string: string
    :param valoare: int
    :return: descrierea obiectului dupa concatenare sau descrierea fara concatenare daca pretul este mai mic decat valoarea
    '''
    if type(string) is not str:
        raise ValueError("Variabila string trebuie sa fie de tip str!")
    if type(valoare) is not int:
        raise ValueError("Variabila valoare trebuie sa fie de tip int!")
    new_list = []
    for obiect in lst_obiecte:
        if get_pret(obiect) > valoare:
            concat = get_descriere(obiect) + string
            new_object = creare_obiect(get_id(obiect), get_nume(obiect),
                                       concat, get_pret(obiect), get_locatie(obiect))
            new_list.append(new_object)
        else:
            new_list.append(obiect)
    return new_list

def pret_maxim_locatie(lst_obiecte):
    '''
    functie care determina pretul maxim pentru fiecare locatie
    :param lst_obiecte: lista obiecte
    :return: un dictionar in care locatia este cheia, iar valoarea este reprezentata de obiectul cu pretul cel mai mare
    '''
    result = {}
    for obiect in lst_obiecte:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie in result:
            if pret > result[locatie]:
                result[locatie] = pret
        else:
            result[locatie] = pret
    return result

def ord_cresc_dupa_pret_achizitie(lst_obiecte):
    '''
    functie care ordoneaza crescator obiectele dupa pretul achizitiei
    :param lst_obiecte:lista de obiecte
    :return:dictionarul rezultat
    '''
    return sorted(lst_obiecte, key = get_pret)

def suma_pret_per_locatie(lst_obiecte):
    '''
    functie care determina suma preturilor pentru fiecare locatie
    :param lst_obiecte:lista de obiecte
    :return:un dictionar unde cheia este locatia si valoarea este suma preturilor
    '''
    lista = {}
    for obiect in lst_obiecte:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie not in lista:
            lista[locatie] = pret
        else:
            lista[locatie] += pret
    return lista

