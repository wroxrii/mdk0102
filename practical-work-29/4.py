p = [',', ':', ';', '.']
s = 'I am writing, the sun of my in fancy had set: at the bottom of a hill, in the summer disk; a golden midges.'
r = {''.join([le for le in x if le not in p]) for x in s.split()}
print(r)
