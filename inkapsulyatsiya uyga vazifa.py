class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1

    def get_yosh(self):
        return self.__yosh

    def set_yosh(self, yosh):
        self.__yosh += 1

    def get_info(self):
        info = f"{self.ism} {self.familiya} , yosh: {self.__yosh}. "
        return info

    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni


class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, familiya, yosh, bosqich):
        super().__init__(ism, familiya, yosh)
        self.__bosqich = bosqich
        Talaba.talabalar_soni += 1

    def get_bosqich(self):
        return self.__bosqich

    def set_bosqich(self, bosqich):
        self.__bosqich += 1

    def get_info(self):
        return f"{self.ism} {self.familiya} bosqich: {self.__bosqich}. "

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni


talaba1 = Talaba("Ali", "Valiyev", 19, 1)
talaba2 = Talaba("Vali", "Aliyev", 23, 2)
talaba3 = Talaba("Hasan", "Husanov", 20, 3)
print(talaba1.get_info())
print(talaba2.get_info())
print(talaba3.get_info())

print(talaba1.get_yosh())
print(talaba2.get_yosh())
print(talaba3.get_yosh())

talaba1.set_yosh(21)
talaba1.set_bosqich(3)
print(talaba1.get_info())

print("Odamlar soni:", Shaxs.get_odamlar_soni())
print("Talaba soni:", Talaba.get_talabalar_soni())
