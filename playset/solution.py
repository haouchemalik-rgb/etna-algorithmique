def playset(s: str) -> bool:
    stock = []
    
    for x in range(len(s)):
        if (s[x] in stock):
            return True
        else:
            stock.append(s[x])
    return False

print(playset("abcde"))
print(playset("abbcdde"))
print(playset("abcdeab"))