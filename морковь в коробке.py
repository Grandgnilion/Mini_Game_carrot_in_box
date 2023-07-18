import random
class Carrot:
    __run_game = True
    #инициализация коробок
    def __init__(self):
        self.box = random.randint(0,1)
        self.box2 = random.randint(0,1)
    
    def carrot(self):
        self.player1 = self.box
        self.player2 = self.box2
        #Если модуль рандом выдаст две единицы то генерируем ошибку
        if self.player1 and self.player2 == 1:
            raise ArithmeticError('Ошибка, перезапустите игру')
        
        elif self.player1 or self.player2 == 1:
            while self.__run_game:
                self.user1 = input("Want you are exchange?")
                self.user2 = input("Want you are exchange?")
                if self.user1 or self.user2 == 'Yes' or 'yes':
                    self.player1 = self.box2
                    self.player2 = self.box
                    if self.player1 == 1:
                        print('Player 1 win')
                        return self.player1, self.player2
                    elif self.player2 == 1:
                        print('Player 2 win')
                        return self.player1, self.player2

carrot = Carrot()
print(carrot.carrot())
