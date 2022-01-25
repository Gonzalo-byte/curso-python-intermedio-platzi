
def run():
    my_dict = {}

    # for i in range(1, 101):
    #     if not i % 3 ==0:
    #         my_dict[i] = i**3

    # print(my_dict)

    dict_comp = {i: i**3 for i in range(1, 101) if not i % 3 == 0}
    # print(dict_comp)

    #reto clase
    reto_dict = {i: i**0.5 for i in range(1, 1001)}
    print(reto_dict)

if __name__ == '__main__':
    run()
