students = {
    'Timur': (170, 75),
    'Ruslan': (180, 105),
    'Soltan': (192, 68),
    'Roman': (175, 70),
    'Madlen': (160, 50),
    'Stefani': (165, 70),
    'Tom': (190, 90),
    'Jerry': (180, 87),
    'Anna': (172, 67),
    'Scott': (168, 78),
}
print({i: students[i] for i in students if students[i][0] > 167 and students[i][1] < 75})
