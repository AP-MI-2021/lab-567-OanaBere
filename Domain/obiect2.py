




def getNewObject(_id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    '''
    :param _id: int
    :param _nume: string
    :param _descriere: string
    :param _pret: int
    :param _locatie: string
    :return: o lista
    '''

    obiect = [_id, _nume, _descriere, _pret, _locatie]

    return obiect


def get_id(obiect):
    '''
    getter pt id-ul obiectului
    :param obiect:
    :return:
    '''
    return obiect[0]


def get_nume(obiect):
    '''
    getter pt numele obiectului
    :param obiect:
    :return:
    '''
    return obiect[1]


def get_descriere(obiect):
    '''
    getter pt descrierea obiectului
    :param obiect:
    :return:
    '''
    return obiect[2]


def get_pret(obiect):
    '''
    getter pt pretul obiectului
    :param obiect:
    :return:
    '''
    return obiect[3]


def get_locatie(obiect):
    '''
    getter pt locatia obiectului
    :param obiect:
    :return:
    '''
    return obiect[4]


def get_str(obiect):
    return f'Obiectul cu id-ul {get_id(obiect)} este :{get_nume(obiect)} ,{get_descriere(obiect)} , ' \
           f'a costat {get_pret(obiect)} ' \
           f'si se afla in {get_locatie(obiect)}'