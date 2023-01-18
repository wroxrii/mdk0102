import re

files = [
    'python.PY', 'qwerty.py', 'stepik.png', 'beegeek.org',
    'window.pnp', 'pen.txt', 'phone.py', 'book.txT',
    'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg',
    'png.png', 'input.tXt', 'split.pop', 'solution.Py',
    'stepik.PY', 'kotlin.pY', 'github.git',
]

print({item for item in files if re.search(r'(?<=\.)\w+', item.lower()).group() == 'py'})
