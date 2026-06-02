# 1) Svetafor:

rang = input("Svetafor qaysi rangda? (qizil, sariq, yashil): ")

togri_ranglar = ["qizil", "sariq", "yashil"]

while rang not in togri_ranglar:
    print("Bu xato rang!")
    rang = input("Iltimos, qayta kiriting (qizil, sariq, yashil): ")

else:
    print("Rahmat, to'g'ri keladi")

# 2) Tasodifiy Sonni Topish O'yini:

son = int(input("1 dan 10 gacha bo'lgan son tanlang"))

togri_son = 8

while son != togri_son:
    print("Noto'g'ri")
    son = int(input("Qaytadan urinib ko'ring"))

else:
    print("Tabriklaymis, siz topdingiz!")

# 3) Do'stlar Ro'yxatini Yaratish:

ismlar = []

print("Yaqin do'stlaringizni ismini kiritamiz (To'xtatish uchun 'stop' deb yozing): ")
n=1
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol).strip()

    if ism.lower() == "stop":
        break

    ismlar.append(ism)
    n += 1

print("\nDo'stlaringizni ro'yxati:")
for ism in ismlar:
    print(ism.title())

# 4) Valyuta Ayirboshlash Kalkulyatori:

KURS = 12600

print("--- Valyuta Ayirboshlash Kalkulyatori ---")
print("Dasturni to'xtatish uchun 'exit' deb yozing.\n")

while True:
    qiymat = input("So'm qiymatini kiriting (yoki 'exit'): ").strip().lower()

    if qiymat == 'exit':
        print("Dastur to'xtatildi. Salomat bo'ling!")
        break

    if qiymat.isdigit():
        som = float(qiymat)
        dollar = som / KURS
        print(f"{som:,} so'm = {dollar:.2f} USD\n")
    else:
        print("Iltimos, faqat musbat son kiriting yoki 'exit' deb yozing!\n")