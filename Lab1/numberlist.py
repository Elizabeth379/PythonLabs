def even_function(numlist):
    result = []
    for i in range(len(numlist)):
        if numlist[i].isdigit() and int(numlist[i]) % 2 == 0:
            result.append(numlist[i])

    if result == []:
        return "No even numbers"
    else: return result


if __name__ == '__main__':

    numlist = list(input('Enter separated by space numbers: ').split())

    print(even_function(numlist))