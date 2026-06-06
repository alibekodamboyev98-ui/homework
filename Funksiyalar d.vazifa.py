# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(4, 5, 6, 7))

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda
# istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familiya, **baho):
    baho['ism'] = ism
    baho['familiya'] = familiya
    return baho

talaba1 = talaba_info("Ali", "Valiyev", baho=5)
talaba2 = talaba_info("Vali", "Aliyev", baho=4)
print(talaba1)
print(talaba2)