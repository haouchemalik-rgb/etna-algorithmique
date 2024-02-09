def little_boxes(s: str) -> str:
    char_count = [0] * 128

    for char in s:
        char_count[ord(char)] += 1

    sorted_s = ''
    for i in range(128):
        sorted_s += chr(i) * char_count[i]

    return sorted_s
