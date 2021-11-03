from Logic.general_logic import create
from Tests.test_crud import test
from Tests.teste_functionalitati import test_modify_location, test_concat_string_descriere
from UserInterface.consola2 import newMenu
from UserInterface.console import run_Menu


def main():
    obiecte = []
    obiecte = create(obiecte, 1, 'laptop', 'hp', 4000, 'cluj')
    obiecte = create(obiecte, 2, 'lampa', 'verde', 100, 'arad')
    obiecte = create(obiecte, 3, 'monitor', 'dell', 1200, 'sala')
    obiecte = create(obiecte, 4, 'canapea', 'living', 2800, 'arad')
    obiecte = create(obiecte, 5, 'imprimanta', 'epson', 1500, 'desk')

    meniu = str(input("Scrieti ce fel de meniu doriti: clasic sau prin comenzi "))
    if meniu == "clasic":
        run_Menu(obiecte)
    elif meniu == "comenzi":
        newMenu(obiecte)


if __name__ == '__main__':
    test()
    test_modify_location()
    test_concat_string_descriere()
    main()
