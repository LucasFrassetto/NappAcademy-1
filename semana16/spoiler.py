from contextlib import contextmanager

@contextmanager
def spoiler():
    print('<spoiler>')
    yield
    print('</spoiler>')

with spoiler():
    print('Luke: eu sou sei pai')