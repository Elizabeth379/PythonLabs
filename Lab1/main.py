import arithmetic
import helloworld
import numberlist

if __name__ == '__main__':

    helloworld.hello()

    while type:
        str1 = input('Enter first number:')
        try:
            first = int(str1)
        except ValueError:
            print('"' + str1 + '"' + ' - is not a number')
        else:
            break

    while type:
        str2 = input('Enter second number:')
        try:
            second = int(str2)
        except ValueError:
            print('"' + str2 + '"' + ' - is not a number')
        else:
            break

    operation = input("Enter operation (add, sub, mult or div):")

    result = arithmetic.calculate_operation(first, second, operation)
    print(result)

    numlist = list(input('Enter separated by space numbers: ').split())

    print(numberlist.even_function(numlist))

