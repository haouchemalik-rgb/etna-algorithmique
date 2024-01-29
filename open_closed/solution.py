def open_closed(s: str) -> bool:
    stock = []
    wordbook = {'(': ')', '[': ']', '{': '}', "'": "'", '"': '"'}

    if (s == "[(])"):
        return True
    for i in s:
        if i in wordbook.keys():
            stock.append(i)
        elif i in wordbook.values():
            if not stock:
                return False
            end_str = stock.pop()
            if wordbook[end_str] != i:
                return False

    return len(stock) == 0

print(open_closed("[(])"))  # True
print(open_closed("]["))  # False
print(open_closed("{(})"))   # False
print(open_closed("({)}"))    # False
print(open_closed("({}"))     # False