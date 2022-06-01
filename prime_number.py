def prime_number(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) != 0:
                return "Is a prime number"
            else:
                return "Is not a prime number"


if __name__ == '__main__':
    print(prime_number(5))
