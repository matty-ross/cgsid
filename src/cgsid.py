def compress(string: str) -> int:
    assert len(string) <= 12, "String too long."
    id = 0
    for i in range(12):
        id *= 0x28
        if i >= len(string):
            continue
        c = ord(string[i])
        if c == 0x5F:
            id += 0x27
        elif c >= 0x61:
            id += c - 0x54
        elif c >= 0x41:
            id += c - 0x34
        elif c >= 0x30:
            id += c - 0x2D
        elif c == 0x2F:
            id += 0x2
        elif c == 0x2D:
            id += 0x1
    return id


def uncompress(id: int) -> str:
    string = ''
    for _ in range(12):
        c = id % 0x28
        id //= 0x28
        if c == 0x27:
            string = chr(0x5F) + string
        elif c >= 0xD:
            string = chr(c + 0x34) + string
        elif c >= 0x3:
            string = chr(c + 0x2D) + string
        elif c == 0x2:
            string = chr(0x2F) + string
        elif c == 0x1:
            string = chr(0x2D) + string
        elif c == 0x0:
            string = chr(0x20) + string
        else:
            string = chr(0x0) + string
    return string.rstrip(' ')
