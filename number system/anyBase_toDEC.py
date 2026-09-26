# any base to decimal conversion universal python code 

def to_dec(number,base):
    result = 0

    for ch in number:
        if ch.isdigit():
            digit = int(ch)
        else:
            digit = ord(ch.upper()) - ord('A') + 10
        result = result * base + digit 
    return result 

number = input('enter number: ')
base = int(input('enter base: '))
print(to_dec(number,base))