from string import punctuation

sentence = 'I am writing, the sun of my in fancy had set: at the bottom of a hill, in the summer disk; a golden midges.'
words = {''.join([letter for letter in item if letter not in punctuation]) for item in sentence.split()}

print({i for i in words if 'o' in i})
