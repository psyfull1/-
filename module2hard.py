def storage(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                pairs.append(str(i) + str(j))

    result = ''.join(pairs)
    return result


n = int(input("Введите число от 3 до 20: "))
result = storage(n)
print(result)
