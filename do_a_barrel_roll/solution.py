def do_a_barrel_roll(numbers: list[int], k: int) -> list[int]:
    k %= len(numbers)
    
    while k > 0:
        stock = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[len(numbers) - 1] = stock
        k -= 1
    return numbers

print(do_a_barrel_roll([0, 1, 2, 3], 1))
print(do_a_barrel_roll([0, 1, 2, 3], 2))