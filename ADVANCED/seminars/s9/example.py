# пример замыкания для a = counter

def outer():
    a = 0

    def inner():
        nonlocal a
        a += 1
        print(a)
    
    return inner

a = outer()
a()
a()
a()
a()
a()