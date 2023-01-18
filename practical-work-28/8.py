fn = {
    'timur': 17, 'rulsan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76,
    'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89,
    'soltan': 49, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75,
    'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876,
}
r = {x: fn[x] for x in fn if fn[x] % 7 == 0}
print(r)
