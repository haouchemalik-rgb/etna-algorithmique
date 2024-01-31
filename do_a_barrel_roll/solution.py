def do_a_barrel_roll(numbers: list[int], k: int) -> list[int]:
    if not numbers:
        return numbers
    k %= len(numbers)
    
    while k > 0:
        stock = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[len(numbers) - 1] = stock
        k -= 1
    return numbers

def do_a_barrel_roll(numbers: list[int], k: int) -> list[int]:
    if not numbers:
        return numbers  # Renvoie la liste inchangée si elle est vide
    
    k %= len(numbers)
    
    while k > 0:
        stock = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[len(numbers) - 1] = stock
        k -= 1
    return numbers
