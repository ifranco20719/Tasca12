import ex1  # Importa el módulo ex1.
import ex2  # Importa el módulo ex2.
import ex3  # Importa el módulo ex3.
import ex4  # Importa el módulo ex4.
import ex5  # Importa el módulo ex5.
import ex6  # Importa el módulo ex6.

def menu():
    op=0
    while op<1 or op>8:
        print("""
              1. Mastermind
              2. Llista de tasques
              3. Joc
              4. P00
              5. Scrapping
              6. Servidor Web
              7. Sortir
              """)
        op=int(input("Introdueix una opció del menú: "))
        if op<1 or op>8:
            print("Opció no vàlida, torniu-ho a provar")
        else:
            return op

op=0
while op!=7:
    op = menu()
    match(op):
        case 1:
            ex1.pex1()
        case 2:
            ex2.pex2()
        case 3:
            ex3.pex3()
        case 4:
            ex4.pex4()
        case 5:
            ex5.pex5()
        case 6:
            ex6.pex6()
        case 7:
            print("Gràcies per a utilitzar el joc")