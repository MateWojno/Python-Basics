import random

a = random.randrange(1, 100, 1)
print(a)

b = random.random()
print(b)

c = random.choice('abcdefghijklmnop')
print(c)

d = random.uniform(1,100)
print(d)

lista = ["a","b","c","d"]

f = random.shuffle(lista)
print(f)
