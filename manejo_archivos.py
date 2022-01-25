

def read():
    numeros = []
    with open('./archivos/numeros.txt', "r", encoding="utf-8") as file:
        for line in file:
            numeros.append(int(line))
    print(numeros)


def write():

    nombres = ["Juan", "Pedro", "Maria", "Ana"]
    with open('./archivos/nombres.txt', "w", encoding="utf-8") as file:
        for nombre in nombres:
            file.write(nombre + "\n")
        print("archivo creado")


def run():
    read()


if __name__ == '__main__':
    run()
    write()
