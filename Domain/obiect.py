

def creare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie):
    '''
    creeaza un obiect

    :param id_obiect: -unic
    :param nume: -numele obiectului
    :param descriere:-descrierea obiectului
    :param pret_achizitie:-pretul cu care a fost achizitionat
    :param locatie:-locatia unde se afla obiectul
    :return: un obiect
    '''
    return {
        'id': id_obiect,
        'nume': nume,
        'descriere': descriere,
        'pret': pret_achizitie,
        'locatie': locatie
    }


def get_id(obiect):
    '''
    getter pt id-ul obiectului
    :param obiect:
    :return:
    '''
    return obiect['id']


def get_nume(obiect):
    '''
    getter pt numele obiectului
    :param obiect:
    :return:
    '''
    return obiect['nume']


def get_descriere(obiect):
    '''
    getter pt descrierea obiectului
    :param obiect:
    :return:
    '''
    return obiect['descriere']


def get_pret(obiect):
    '''
    getter pt pretul obiectului
    :param obiect:
    :return:
    '''
    return obiect['pret']


def get_locatie(obiect):
    '''
    getter pt locatia obiectului
    :param obiect:
    :return:
    '''
    return obiect['locatie']


def get_str(obiect):

    return f'Obiectul cu id-ul {get_id(obiect)} este :{get_nume(obiect)}, {get_descriere(obiect)} , ' \
           f'a costat {get_pret(obiect)} ' \
           f'si se afla in {get_locatie(obiect)}.'