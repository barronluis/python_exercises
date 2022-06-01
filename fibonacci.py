def fibonacci(number: int = 2):
    start = 0
    end = 1
    str_result = str(start) + ", " + str(end)
    if number == 0:
        return print(0)
    elif number == 1:
        return print(str_result)
    for number in range(2, number):
        result = start + end
        start = end
        end = result
        str_result = str_result + ", " + str(result)
    return str_result


if __name__ == '__main__':
    print(fibonacci(15))
