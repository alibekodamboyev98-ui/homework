# 1-masala:
sozlar = ["olma", "anor", "gilos", "banan"]
uzunliklar = list(map(len, sozlar))
print(uzunliklar)

# 2-masala:
sonlar = [1, 25, 300, 45]
satrlar = list(map(str, sonlar))
print(satrlar)

# 3-masala:
sozlar_unli = ["olma", "anor", "behi", "uzum", "anor", "nok"]
unli_boshlanuvchi = list(filter(lambda s: s[0].lower() in 'aeiouo‘u‘', sozlar_unli))
print(unli_boshlanuvchi)

# 5-masala:
ismlar = ["Ali", "Vali", "Gani"]
Mr_ismlar = list(map(lambda ism: "Mr. " + ism, ismlar))
print(Mr_ismlar)
