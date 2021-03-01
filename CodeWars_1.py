def fibonacci(n):
    result = [0, 1]
    n1, n2 = 0, 1
    while n + 1 > len(result):
        n1, n2 = n2, n1 + n2
        result.append(n2)

    return result


print(fibonacci(10))

def is_valid_walk(walk):
    result = {}
    for street in walk:
        if street not in result:
            result[street] = 1
        else:
            result[street] += 1



print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))