def morning_sunshine(numbers):
    if not numbers:
        return []

    max_num = 0
    result = []

    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > max_num:
            result.append(numbers[i])
            max_num = numbers[i]

    return result[::-1]