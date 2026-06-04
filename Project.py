# 1

def user_data(first_name, last_name, age):
    print(f"Ism: {first_name}")
    print(f"Familiya: {last_name}")
    print(f"Yosh: {age}")

user_data("Alisher", "Olimov", 27)

# 5

def daraja(a, b):
    print(a ** b)

daraja(a=2, b=3)

# 6

def daraja4(a, b, c, d):
    print(a ** b)
    print(a ** c)
    print(a ** d)

daraja4(a=2, b=3, c=4, d=5)

# 8

def add_right(a, b):
    print(str(a) + str(b))

add_right(12, 34)

# 9

def add_left(a, b):
    print(str(b) + str(a))

add_left(12, 34)

# 10

def work_with_list(a):
    min_son = min(a)

    for i in range(len(a)):
        a[i] = a[i] * min_son

    print(a)

work_with_list([2, 4, 6, 8])

# 11

def big_sales(sales):
    oy = max(sales, key=sales.get)
    return oy

sales = {
    "yanvar": 12000,
    "mart": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000
}

print(big_sales(sales))

# 13

def expensiveProduct(products):
    eng_qimmat = products[0]

    for product in products:
        if product["price"] > eng_qimmat["price"]:
            eng_qimmat = product

    print(eng_qimmat["name"])

products = [
    {
        "name": "Iphone X",
        "price": 600
    },
    {
        "name": "Iphone 12",
        "price": 1500
    },
    {
        "name": "Samsung Note 9",
        "price": 800
    },
    {
        "name": "Samsung S10",
        "price": 1100
    }
]

expensiveProduct(products)