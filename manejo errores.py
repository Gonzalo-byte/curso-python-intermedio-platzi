def run():

    while True:

        try:
            numero = int(input("Ingrese un numero positivo: "))
            if numero > 0:
                print(numero)
                break
            else:
                print("Ingrese un numero positivo")

        except ValueError:
            print("Debes ingresar un numero")


if __name__ == "__main__":
    run()
