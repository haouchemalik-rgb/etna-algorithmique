def falafel(s: str) -> bool:
    stock = []
    count = []
    odd = 0

    y = len(s) - 1
    for x in range(0, len(s)):
        if (s[x] not in stock):
            stock.append(s[x])
            count.append(1)
        else:
            count[stock.index(s[x])] += 1
        if (y == x):
            break
        if (s[y] not in stock):
            stock.append(s[y])
            count.append(1)
        else:
            count[stock.index(s[y])] += 1
        y -= 1
        if (y == x):
            break
    
    y = len(count) - 1
    for x in range(0, len(count)):
        if (count[x] % 2 != 0 and odd == 0):
            odd = 1
        elif (count[x] % 2 != 0 and odd == 1):
            return False
        if (y == x):
            break
        if (count[y] % 2 != 0 and odd == 0):
            odd = 1
        elif (count[y] % 2 != 0 and odd == 1):
            return False
        y -= 1
        if (y == x):
            break
    return True