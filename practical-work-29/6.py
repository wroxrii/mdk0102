f = [
    'python.PY', 'qwerty.py', 'stepik.png', 'beegeek.org', 'window.pnp', 'pen.txt', 'phone.py',
    'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt',
    'split.pop', 'solution.Py', 'stepik.PY', 'kotlin.pY', 'github.git',
]
r = {x for x in f if x.split('.')[1].lower() == 'py'}
print(r)
