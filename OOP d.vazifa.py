# 1)

class Foydalanuvchi:
    def __init__(self,ism,foydalanuvchi_ismi,email):
        self.ism = ism
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email

foydalanuvchi1 = Foydalanuvchi("Alijon", "Valiyev", "alijonvaliyev1@gmail.com")
print(foydalanuvchi1.ism)
print(foydalanuvchi1.foydalanuvchi_ismi)
print(foydalanuvchi1.email)

# 2)

class Foydalanuvchi:
    def __init__(self, ism, username, email, telefon, viloyat):
        self.ism = ism
        self.username = username
        self.email = email
        self.telefon = telefon
        self.viloyat = viloyat

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.ism}, email: {self.email}, tel: {self.telefon}"

# 3)

foydalanuvchi1 = Foydalanuvchi("Ali Valiyev", "ali1994", "ali1994@gmail.com", "+998901234567", "Xorazm")
foydalanuvchi2 = Foydalanuvchi("Vali Aliyev", "vali_1", "vali99@mail.ru", "+998937654321", "Toshkent")

print(foydalanuvchi1.ism)
print(foydalanuvchi2.viloyat)