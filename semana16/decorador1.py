def deco(func):
    def inner():
        print('running inner()')
    return inner # devolve a função inner (um callable)

@deco
def target(): # função está decorada
    print('running target()')

target() # Ao chamar a função decorada, executa-se inner
target # ao inspecionar a função, observa-se que ela referencia inner