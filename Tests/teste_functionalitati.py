from Domain.obiect import creare_obiect, get_locatie, get_descriere
from Logic.functionalitati import modify_location, concat_string_descriere


def get_data():
    return [
        creare_obiect(1, 'laptop', 'hp', 4000, 'cluj'),
        creare_obiect(2, 'lampa', 'verde', 100, 'arad'),
        creare_obiect(3, 'monitor', 'dell', 1200, 'sala'),
        creare_obiect(4, 'scaun', 'negru', 350, 'cls3'),
        creare_obiect(5, 'flori', 'bujori', 50, 'vaza')
        ]

def test_modify_location():
        obiecte = get_data()
        initial_location = 'cluj'
        new_location = 'alba'
        list = modify_location(obiecte, initial_location, new_location)
        assert get_locatie(obiecte[0]) != get_locatie(list[0])
        initial_location = 'arad'
        new_location = 'desk'
        list = modify_location(obiecte, initial_location, new_location)
        assert get_locatie(obiecte[0]) == get_locatie(list[0])



def test_concat_string_descriere():
    obiecte = get_data()
    string = 'ab'
    valoare = 1000
    list = concat_string_descriere(obiecte, string, valoare)
    assert get_descriere(obiecte[0]) != get_descriere(list[0])
    assert get_descriere(obiecte[2]) != get_descriere(list[2])




def test():
    test_modify_location()
    test_concat_string_descriere()