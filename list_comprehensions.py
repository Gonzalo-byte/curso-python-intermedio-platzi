
def run():

    # [element for element in iterable if condition]
    #my_list = [i**2 for i in range(1, 101) if not i % 3 == 0]

    #print(my_list)

    # reto de la clase
    my_list2 = [i for i in range(1, 9999) if i %
                4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(my_list2)

if __name__ == '__main__':
    run()
