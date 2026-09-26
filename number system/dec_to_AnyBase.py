# decimal to Any Base conversion 
# ye base 35 tak support krega 

def dec_to_any_base(number, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    if number == 0:
        return "0"

    result = ''

    while number > 0:
        remainder = number % base

        if remainder < 10:
            result += str(remainder)
        else:
            result += chr(ord('A') + (remainder - 10))

        number //= base

    return result[::-1]


number = int(input('enter number: '))
base = int(input('enter base: '))
print(dec_to_any_base(number,base))