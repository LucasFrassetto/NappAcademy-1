def outer_func():
    def inner_func():
        print("Oi, mundo!")
    inner_func()

outer_func()


def outer_func2(who):
    def inner_func():
        print(f"Oi, {who}!")
    inner_func() 

outer_func2('mundo')


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if number < 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(5))