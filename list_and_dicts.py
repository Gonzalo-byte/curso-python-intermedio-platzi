

def run():

    my_dict = {
        'names': ['gonzalo', 'pedro', 'juan', 'maria', 'jose'],
        'countries': ['ARG', 'MX', 'USA', 'UK', 'FR', 'IT', 'ES']
    }

    for key, value in my_dict.items():
        print(f'{key} : {value}')


if __name__ == '__main__':
    run()
