def generate_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary or "0"

def roger_rabbit(n: int) -> list[str]:
    results = []

    for i in range(1, n + 1):
        results.append(generate_binary(i))

    return results