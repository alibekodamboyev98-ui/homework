# append()
# 1
mevalar = ['olma', 'nok', 'uzum']
mevalar.append("banan")
print(mevalar)
# 2
sonlar = [10, 20, 30, 40]
sonlar.append("50")
print(sonlar)

# clear()
# 1
sonlar = [1, 2, 3]
sonlar.clear()
print(sonlar)
# 2
telefonlar = ["apple", "samsung", "honor"]
telefonlar.clear()
print(telefonlar)

# copy()
# 1
a = [1, 2, 3]
b = a.copy()
print(b)
# 2
c = ["olma", "nok", "uzum"]
d = c.copy()
print(d)

# count()
# 1
sonlar = [1, 2, 3, 3, 4, 5]
print(sonlar.count(3))
# 2
sabzavotlar = ["sabzi", "piyoz", "piyoz", "kartoshka"]
print(sabzavotlar.count("piyoz"))

# extend()
# 1
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
# 2
c = [10, 20, 30]
d = [40, 50, 60]
c.extend(d)
print(c)

# index()
# 1
mevalar = ['olma', 'nok', 'uzum']
print(mevalar.index("banan"))
# 2
mashinalar = ["damas", "cobalt", "nexia"]
print(mashinalar.index("malibu"))

# insert()
# 1
sonlar = [1, 3, 4]
sonlar.insert(1, 2)
print(sonlar)
# 2
number = [6, 8, 9]
number.insert(6, 7)
print(number)

# pop()
# 1
mevalar = ["olma", "banan", "uzum"]
mevalar.pop(1)
print(mevalar)
# 2
fruits = ["nok", "o'rik", "anjir"]
fruits.pop(2)
print(fruits)

# remove()
# 1
sonlar = [1, 2, 3, 2]
sonlar.remove(2)
print(sonlar)
# 2
cars = ["BMW", "AUDI", "LAMBORGINI", "BMW", "MUSTANG"]
cars.remove(1)
print(cars)

# reverse()
# 1
sonlar = [1, 2, 3]
sonlar.reverse()
print(sonlar)
# 2
kompyuterlar = ["HP", "ACER", "DELL", "LENOVO"]
kompyuterlar.reverse()
print(kompyuterlar)

# sort()
# 1
sonlar = [4, 1, 3, 2]
sonlar.sort()
print(sonlar)
# 2
harflar = ["F", "H", "A", "D"]
harflar.sort()
print(harflar)