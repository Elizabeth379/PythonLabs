from constants import OPERATIONS

def calculate_operation(first, second, operation):

    if operation == OPERATIONS[0]:
        return (first + second)
    elif operation == OPERATIONS[1]:
        return (first - second)
    elif operation == OPERATIONS[2]:
        return (first * second)
    elif operation == OPERATIONS[3]:
        if second == 0:
            return "Error"
        else:
            return (first / second)

    else:
        return "Error"



if __name__ == '__main__':

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

    result = calculate_operation(first, second, operation)
    print(result)

