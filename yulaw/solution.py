def yulaw(s: str) -> str:
    stock = []
    
    for x in range(len(s)):
        if (s[x] not in stock):
            stock.append(s[x])

    return stock