def even_function(numlist):
    result = []
    for i in range(len(numlist)):
        if numlist[i].isdigit() and int(numlist[i]) % 2 == 0:
            result.append(numlist[i])

    if result == []:
        return "No even numbers"
    else: return result

