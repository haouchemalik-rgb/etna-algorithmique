def do_a_barrel_roll(numbers: list[int], k: int) -> list[int]:
    n = len(numbers)
    if not numbers or k % n == 0:
        return numbers
    k = k % n

    return numbers[k:] + numbers[:k]