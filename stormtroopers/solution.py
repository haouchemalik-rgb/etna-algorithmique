def stormtroopers(numbers: list[int]) -> list[int]:
    stock = []
    for i in numbers:
        if (numbers.count(i) == 1):
            stock.append(i)
    return stock