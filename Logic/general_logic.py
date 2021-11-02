from Domain.obiect import creare_obiect, get_id



def create(lst_obiecte, id_obiect, nume, descriere, pret_achizitie, locatie):
    """
    :param lst_obiecte: lista de obiecte
    :param id_obiect:id
    :param nume:string
    :param descriere:string
    :param pret_achizitie:int
    :param locatie:string
    :return:o lista noua de obiecte formata din lista initiala si noul obiect
    """
    if read(lst_obiecte, id_obiect) is not None:
        raise ValueError(f'Exista deja un obiect cu id-ul {id_obiect}!')
    if len(locatie) != 4:
        raise ValueError(f'Locatie introdusa gresit! Trebuie sa aiba exact 4 caractere! ')
    obiect = creare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
    return lst_obiecte + [obiect]


def read(lst_obiecte, id_obiect=None):
    """
    "Citeste" un obiect din lista"
    :param id_obiect:
    :return:obiectul cu id-ul cerut sau toata lista in caz ca acesta nu este gasit
    """
    if not id_obiect:
        return lst_obiecte
    obiect_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_cu_id = obiect
    if obiect_cu_id:
        return obiect_cu_id


def update(lst_obiecte, obiect_id_existent):
    """
    Modifica un obiect
    :param lst_obiecte: lista de obiecte
    :param obiect_id_existent: obiect cu id deja existent
    :return: lista de obiecte modificata
    """
    if read(lst_obiecte, get_id(obiect_id_existent)) is None:
        raise ValueError(f'Nu exista niciun obiect cu id-ul {get_id(obiect_id_existent)}!')
    new_lst_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != get_id(obiect_id_existent):
            new_lst_obiecte.append(obiect)
        else:
            new_lst_obiecte.append(obiect_id_existent)
    return new_lst_obiecte


def delete(list_objects, id_object :int):
    if read(list_objects, id_object) is None:
        raise ValueError(f'Nu exista niciun obiect cu id-ul {id_object}!')
    result = []
    for object in list_objects:
        if get_id(object) != id_object:
            result.append(object)
    return result