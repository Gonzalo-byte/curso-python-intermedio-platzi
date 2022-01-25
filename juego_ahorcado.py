import random

palabras = [
    'perro',
    'gato',
    'casa',
    'coche',
    'helado',
    'auto',
    'candado',
    'computadora',
    'teclado',
    'carpeta',
    'cama',
]


def run():

    palabra = random.choice(palabras)
    palabra_dict = {}
    for i in range(len(palabra)):
        palabra_dict[i] = palabra[i]
    

    estado = ['_'] * len(palabra)
    letras_acertadas = 0
    letras_usadas = []
    print('Adivina la palabra')

    print(estado)

    while letras_acertadas < len(palabra):

        opcion = input('\n\n Ingrese una letra:')

        if opcion in palabra_dict.values() and opcion not in letras_usadas:
            letras_usadas.append(opcion)
            for i, x in palabra_dict.items():
                if x == opcion:
                    estado[i] = opcion
                    letras_acertadas += 1
            print(estado)
        else:
            print('elige otra letra')
                
                
    print("ganaste, la palabra era: "+ palabra)


if __name__ == '__main__':
    run()
