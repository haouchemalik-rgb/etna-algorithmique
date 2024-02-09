def do_a_barrel_roll(numbers: list[int], k: int) -> list[int]:
    if not numbers:
        return numbers
    n = len(numbers)
    k %= n   
    if k == 0:
        return numbers
    rotated_numbers = [0] * n
    for i in range(n):
        rotated_numbers[(i + k) % n] = numbers[i]
    for i in range(n):
        numbers[i] = rotated_numbers[i]

    return numbers

