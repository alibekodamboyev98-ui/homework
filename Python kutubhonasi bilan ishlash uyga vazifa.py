# 1)
from datetime import datetime, timedelta

today = datetime.today()

for i in range(10):
    sana = today + timedelta(weeks=2 * i)
    print(sana.strftime("%d-%m-%Y"))


# 2)
from datetime import datetime

bugun = datetime.today()

ramazon = datetime(2026, 2, 17)
qurbon = datetime(2026, 5, 27)

print("Ramazon hayitigacha:", (ramazon - bugun).kun, "kun")
print("Qurbon hayitigacha:", (qurbon - bugun).kun, "kun")


# 3)
from datetime import date

def yosh_hisobla(t_yil, t_oy, t_kun):
    tugilgan = date(t_yil, t_oy, t_kun)
    bugun = date.today()

    yil = bugun.year - tugilgan.year
    oy = bugun.month - tugilgan.month
    kun = bugun.day - tugilgan.day

    if kun < 0:
        oy -= 1
        kun += 30

    if oy < 0:
        yil -= 1
        oy += 12

    print(f"{yil} yil, {oy} oy, {kun} kun")

yosh_hisobla(2006 ,1, 18)


# 4)
import re

telefon = input("Telefon raqamini kiriting (+998901234567): ")

andoza =r'^\+998\d{9}$'
if re.fullmatch(andoza, telefon):
    print("Telefon raqami to'g'ri.")
else:
    print("Telefon raqami noto'g'ri.")


# 5)
import re

matn = """
Bizning saytlar:
https://www.google.com
http://python.org
"""

linklar = re.findall(r'https?://[^\s]+', matn)

print("Topilgan manzillar:")
for link in linklar:
    print(link)
