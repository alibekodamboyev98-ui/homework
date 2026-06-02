# capitalize()
text = "hello"
print(text.capitalize())

# casefold()
text = "HELLO"
print(text.casefold())

# center()
text = "Hello"
print(text.center(10, " "))

# count()
text = "Hello"
print(text.count("l"))

# encode()
text = "Hello"
print(text.encode())

# endswith()
text = "python.py"
print(text.endswith("py"))

# expandtabs()
text = "Hi\tPython"
print(text.expandtabs(4))

# find()
text = "hello"
print(text.find("e"))

# format()
text = "Mening ismim {}"
print(text.format("Ali"))

# format_map()
data = {"name":"Ali"}
text = "My name is {name}"
print(text.format_map(data))

# index()
text = "Hello"
print(text.index("H"))

# isalnum()
text = "Hello123"
print(text.isalnum())

# isalpha()
text = "Hello"
print(text.isalpha())

# isascii()
text = "Hello"
print(text.isascii())

# isdecimal()
text = "123"
print(text.isdecimal())

# isdigit()
text = "123"
print(text.isdigit())

# isidentifier()
text = "my_var"
print(text.isidentifier())

# islower()
text = "hello"
print(text.islower())

# isnumeric()
text = "123"
print(text.isnumeric())

# isprintable()
text = "Hello"
print(text.isprintable())

# isspace()
text = "  "
print(text.isspace())

# istitle()
text = "Hello World"
print(text.istitle())

# isupper()
text = "HELLO"
print(text.isupper())

# join()
text = ["Hello", "World", "!"]
print(" ".join(text))

# ljust()
text = "Hi"
print(text.ljust(10, "-"))

# lower()
text = "HELLO"
print(text.lower())

# lstrip()
text = "   Hello"
print(text.lstrip())

# maketrans()
table = str.maketrans("a", "b")
print("apple".translate(table))

# partition()
text = "Hello-World"
print(text.partition("-"))

# replace()
text = "I like apple"
print(text.replace("apple", "banana"))

# rfind()
text = "banana"
print(text.rfind("a"))

# rjust()
text = "Hi"
print(text.rjust(5))

# rpartition()
text = "Hello-World"
print(text.rpartition("-"))

# rsplit()
text = "a,b,c"
print(text.rsplit(",", 1))

# rstrip()
text = "Hello  "
print(text.rstrip())

# split()
text = "a b c"
print(text.split())

# splitlines()
text = "Hi\nHello"
print(text.splitlines())

# startswith()
text = "Hello"
print(text.startswith("H"))

# strip()
text = "  Hello  "
print(text.strip())

# swapcase()
text = "hElLo"
print(text.swapcase())

# title()
text = "hello world"
print(text.title())

# translate()
text = "hello"
print(text.translate(str.maketrans("h","y")))

# upper()
text = "hello"
print(text.upper)

# zfill()
text = "17"
print(text.zfill(3))
