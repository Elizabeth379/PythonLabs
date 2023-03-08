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



