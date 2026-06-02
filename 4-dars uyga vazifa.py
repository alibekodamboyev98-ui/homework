# 1-Misol: Ob-havo Tavsifi:

harorat = int(input("Haroratni kiriting: "))
if harorat < 0:
    print("Sovuq")
elif 0 <= harorat <= 20:
    print("Salqin")
elif 21 <= harorat <= 30:
    print("Iliq")
else:
    print("Issiq")

# 2-Misol: Internet-do'kon Chegirmasi:

summa = float(input("Xarid summasini kiriting: "))
if summa < 50000:
    print(f"Chegirma yo'q. Yakuniy narx: {summa}")
elif 50000 <= summa <= 100000:
    yakuniy = summa * 0.95
    print(f"5% chegirma. Yakuniy narx: {yakuniy}")
else:
    yakuniy = summa * 0.90
    print(f"10% chegirma. Yakuniy narx: {yakuniy}")

# 3-Misol: Tizimga Kirish:

login = input("Loginni kiriting: ")
parol = input("Parolni kiriting: ")
if login == "admin" and parol == "12345":
    print("Xush kelibsiz, admin!")
else:
    print("Login yoki parol xato")

# 4-Misol: Film Yosh Cheklovi:

yosh = int(input("Yoshingizni kiriting: "))
if yosh < 13:
    print("Sizga ushbu film tavsiya etilmaydi")
elif 13 <= yosh <= 17:
    print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
else:
    print("Siz filmni tomosha qilishingiz mumkin")

# 5-Misol: Restoran Menyusi:

tanlov = input("Taom tanlang (1-Osh, 2-Mastava, 3-Shashlik): ")
if tanlov == "1":
    print("Osh - 25,000 so'm. Tayyorlanish vaqti: 20 daqiqa.")
elif tanlov == "2":
    print("Mastava - 18,000 so'm. Tayyorlanish vaqti: 15 daqiqa.")
elif tanlov == "3":
    print("Shashlik - 12,000 so'm (1 sixi). Tayyorlanish vaqti: 25 daqiqa.")
else:
    print("Bunday taom menyuda yo'q")

# 6-Misol: Email Tekshiruvi:

email = input("Email manzilingizni kiriting: ")
if email.find("@") == -1 or email.find(".") == -1:
    print("Noto'g'ri email manzili")
else:
    print("Email qabul qilindi")

# 7-Misol: Talaba Baholash Tizimi:

ball = int(input("Ballni kiriting (0-100): "))
if 86 <= ball <= 100:
    print("5 baho")
elif 70 <= ball <= 85:
    print("4 baho")
elif 55 <= ball <= 69:
    print("3 baho")
else:
    print("2 baho")

# 8-Misol: Bankomat Pul Yechish:

balans = 100000
yechish = float(input("Yechmoqchi bo'lgan summani kiriting: "))

if yechish > balans:
    print("Hisobda yetarli mablag' mavjud emas")
elif yechish < 5000:
    print("Minimal yechish summasi 5 000 so'm")
else:
    balans -= yechish
    print(f"Pul muvaffaqiyatli yechildi. Qolgan mablag': {balans}")

# 9-Misol: Ish Jadvalini Tekshirish:

kun = input("Hafta kunini kiriting: ").capitalize()
if kun == "Shanba" or kun == "Yakshanba":
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")

# 10-Misol: Mobil Tarif Tanlash:

trafik = float(input("Oylik trafik miqdorini kiriting (GB): "))
if trafik < 1:
    print("Sizga 'Mini' tarifi mos keladi")
elif 1 <= trafik <= 5:
    print("Sizga 'Standard' tarifi mos keladi")
else:
    print("Sizga 'Unlimited' tarifi mos keladi")