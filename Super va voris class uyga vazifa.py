class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __str__(self):
        return self.nomi


class Talaba:
    def __init__(self, ism, fanlar=None):
        self.ism = ism
        self.fanlar = fanlar if fanlar is not None else []


    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        print(f"{self.ism} {fan.nomi} faniga yozildi.")


    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan.nomi} fani o‘chirildi.")
        else:
            print("Siz bu fanga yozilmagansiz.")


    def show_fanlar(self):
        if self.fanlar:
            print(f"{self.ism} fanlari:")
            for fan in self.fanlar:
                print("-", fan.nomi)
        else:
            print("Fanlar mavjud emas.")


matematika = Fan("Matematika")
fizika = Fan("Fizika")
informatika = Fan("Informatika")

talaba1 = Talaba("Ali")

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)

talaba1.show_fanlar()

talaba1.remove_fan(fizika)

talaba1.show_fanlar()

talaba1.remove_fan(informatika)