s = 'Napp'

for letra in s:
    print(letra)

print( 4 * "-")
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
