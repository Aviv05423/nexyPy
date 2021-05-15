
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    gen = (words[word] for word in sentence.split(" "))
    print(*list(gen))

# translate("el gato esta en la casa")

def get_fibo():
    x = 0
    y = 1
    print(0)
    print(1)
    while True:
        gen = (x + y)
        f = y
        y = x + y
        x = f

        yield gen


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
