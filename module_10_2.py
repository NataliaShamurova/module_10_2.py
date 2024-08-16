from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):

        print(f'{self.name}, на нас напали!')

        count_day = 0
        quantity_enemy = 100

        

        while quantity_enemy > 0:

            count_day += 1
            quantity_enemy -= self.power

            # sleep(1)
            print(f'{self.name} сражается {count_day} день (дня)..., осталось {quantity_enemy} воинов.')

            sleep(1)

        print(f"{self.name} одержал победу спустя {count_day} дней(дня)!")

#  Создание рыцарей

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


#  Создание потоков

first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()


print('Все битвы закончились!')

