from Domain.obiect import creare_obiect, get_id

from Logic.general_logic import create, read, update, delete


def get_data():
    return [
        creare_obiect(1, 'laptop', 'hp', 4000, 'cluj'),
        creare_obiect(2, 'lampa', 'verde', 100, 'arad'),
        creare_obiect(3, 'monitor', 'dell', 1200, 'sala'),
        creare_obiect(4, 'scaun', 'negru', 350, 'cls3'),
        creare_obiect(5, 'flori', 'bujori', 50, 'vaza'),
            ]


def test_create():
    obiecte = get_data()
    params = (6, 'dulap', 'inalt', 200, 'cluj')
    new_obiect = creare_obiect(*params)
    lst = create(obiecte, *params)
    assert new_obiect in lst


def test_read():
    obiecte = get_data()
    s_obiect = obiecte[2]
    assert read(obiecte, get_id(s_obiect)) == s_obiect


def test_update():
    obiecte = get_data()
    params = (5, 'dulap', 'inalt', '200', 'birou')
    up_obiect = creare_obiect(*params)
    lst = update(obiecte, up_obiect)
    assert up_obiect not in obiecte
    assert up_obiect in lst
    assert len(lst) == len(obiecte)


def test_delete():
    obiecte = get_data()
    de = 2
    obiect_del = read(obiecte, de)
    lst = delete(obiecte, de)
    assert len(lst)+1 == len(obiecte)
    assert obiect_del not in lst
    assert obiect_del in obiecte


def test():
    test_create()
    test_read()
    test_update()
    test_delete()