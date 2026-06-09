# 1-masala:
sozlar = ["olma", "anor", "gilos", "banan"]
uzunliklar = list(map(len, sozlar))

# 2-masala:
sonlar = [1, 25, 300, 45]
satrlar = list(map(str, sonlar))

# 3-masala:
sozlar_unli = ["olma", "anor", "behi", "uzum", "anor", "nok"]
unli_boshlanuvchi = list(filter(lambda s: s[0].lower() in 'aeiouo‘u‘', sozlar_unli))

# 5-masala:
ismlar = ["Ali", "Vali", "Gani"]
janob_ismlar = list(map(lambda ism: "Mr. " + ism, ismlar))
