def BitwiseSub(a,b):
    mask = 0xFFFFFFFF
    max_int = 0x7FFFFFFF
    while b:
        borrow = (~a & b) << 1
        a = (a ^ b) & mask
        b = borrow & mask

    if a <= max_int:
        return a
    else:
        return ~(a^mask)

a = int(input('a: '))
b = int(input('b: '))
print(BitwiseSub(a,b))