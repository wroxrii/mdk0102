digit = int(input())
s = input()
for i in s:
    # комментирую
    if 97 > ord(i) - digit:
        temp = ord(i) - digit + 26
        print(chr(temp), end='')  # вывод
    else:
        # АХПХАПХАПХАХПХАПХАПХАПХАХПХ
        temp = ord(i) - digit
        print(chr(temp), end='')
