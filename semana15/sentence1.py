"""
Exemplo 14-1 do livro Python Fluente 
"""
import re
import reprlib
RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence("Projeto Napp Academy")
it = iter(s)