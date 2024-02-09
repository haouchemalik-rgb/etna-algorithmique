def stormtroopers(numbers: list[int]) -> list[int]:
    stock = {}
    for i in numbers:
        stock[i] = stock.get(i, 0) + 1
    
    result = []
    for i, count in stock.items():
        if count == 1:
            result.append(i)
    
    return result