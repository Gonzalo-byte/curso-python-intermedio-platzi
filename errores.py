def divisor(num):
    

    divisors = [i for i in range(1,num+1) if num % i == 0]
    print(divisors)


if __name__ == '__main__':
    divisor(int(input("Ingrese un numero: ")))