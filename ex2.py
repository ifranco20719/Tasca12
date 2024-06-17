def crear_fitxer(nom):
    with open("tasques.txt", "w") as f:
        print("Fitxer tasques.txt creat \n")

def inserir_element(a):
    with open("tasques.txt","a") as f:
        f.write(a+"\n")

def modificar_element(a):
    with open("tasques.txt","a") as f:
        f.write(a+"\n")

def eliminar_element(a):
    with open("tasques.txt","r") as f:
        lines = f.readlines()
    with open("tasques.txt","w") as f:
        for line in lines:
            if line.strip() != a:
                f.write(line)

def llistar_fitxer():
    with open("tasques.txt","r") as f:
        for e in f:
            print(e+"\n")

def menu_fitxer():
    op=0
    while op<1 or op>5:
        print("""
            1. Inserir element
            2. Modificar element
            3. Eliminar element
            4. Llistar fitxer
            5. Sortir
            """)
        op=int(input("Introdueix una opció del menú: "))
        if op<1 or op>6:
            print("Opció no vàlida \n")
        else:
            return op
        
def pex2():
    op=0
    while op!=5:
        op = menu_fitxer()
        match(op):
            case 1:
                inserir_element(input("Enter the element to insert: "))
            case 2:
                modificar_element(input("Enter the element to modify: "))
            case 3:
                eliminar_element(input("Enter the element to eliminate: "))
            case 4:
                llistar_fitxer()
            case 5:
                print("Gràcies per a utilitzar el joc")
