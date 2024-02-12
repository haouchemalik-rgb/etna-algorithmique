def set_et_match(numbers: list[int], n: int) -> bool:
    wordbook = {}

    for i in numbers:
        stock = n - i
        if stock in wordbook:
            return True
        wordbook[i] = True
    
    return False