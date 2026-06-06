# Talabalar baholarining o'rtachasini hisoblash

def ortacha_baho(ism, *baholar):

    ortacha = sum(baholar) / len(baholar)
    return f"{ism}ning o'rtacha bahosi: {ortacha}"

print(ortacha_baho("Ali", 5, 4, 3, 5, 4))

# Mahsulot haqida ma'lumot yaratish

def mahsulot_malumoti(nomi, **qoshimcha_malumotlar):
    mahsulot = {"nomi": nomi}
    mahsulot.update(qoshimcha_malumotlar)
    return mahsulot

print(mahsulot_malumoti("iPhone 15", narxi="1000$", rangi="Qora", xotira="256GB", brend="Apple"))