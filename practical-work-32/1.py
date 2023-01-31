def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        added_char = char
        if char in vowels:
            added_char = char.upper()
        swapped_string += added_char

    return print(swapped_string)


swapcase_vowels('how many vowel letters')
swapcase_vowels('are there in English alphabet')
