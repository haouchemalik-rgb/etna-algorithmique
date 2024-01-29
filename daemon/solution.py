def daemon(numbers: list[int], k: int) -> bool:
    if (len(numbers) < 1 or len(numbers) < k - 1 or k < 0):
        return False
    if (len(numbers) == 1):
        return True

    for x in range(0, len(numbers)):
        print(x)
    return True