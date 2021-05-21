
import itertools

def vogais(c):
    return c.lower() in 'aeiou'

texto = 'Napp Academy'
# Funções geradoras de filtragem

list(filter(vogais, texto))
list(itertools.filterfalse(vogais, texto))
list(itertools.dropwhile(vogais, texto))
list(itertools.takewhile(vogais, texto))
list(itertools.compress(texto, (1,0,1,1,0,1)))
list(itertools.islice(texto, 4))
list(itertools.islice(texto, 4, 7))
list(itertools.islice(texto, 1, 7, 2))

#Funções geradoras de mapeamento

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
list(itertools.accumulate(sample))
list(itertools.accumulate(sample, min))
list(itertools.accumulate(sample, max))
import operator
list(itertools.accumulate(sample, operator.mul))
list(itertools.accumulate(range(1, 11), operator.mul))
