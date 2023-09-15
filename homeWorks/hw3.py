class Bank:
    def __init__(self, name, balanse):
        self.__name = name
        self.__balanse = balanse

    def moneyX(self):
        try:
            amount = int(input('введите сумму которую хотите пополнить:'))
            if amount > 0:
                self.__balanse += amount
            else:
                print('сумма должна быть бтльше 0')
        except ValueError:
            print('введите корректное число')

    def __str__(self):
        return self.__name, self.__balanse

    def __kill(self):
        self.__balanse = 0


    def _jackpot(self):
        self.__balanse *= 10
        print("вы выиграли джекпот, деньги умножены на 10")

    def __wix(self, other):
        other.__balanse += self.__balanse

    def get_balance(self):
        return self.__balanse


user1 = Bank('aidana', 23)

user1._jackpot()
print(f'Ваш текущий баланс: {user1.get_balance()}')
user1.moneyX()
print(f'Теперь ваш баланс: {user1.get_balance()}')

beka = Bank('Beka', 2000)
print(f'Изначальный баланс Беки: {beka.get_balance()}')
user1._Bank__wix(beka)

print(f'Теперь баланс беки: {beka.get_balance()}')

user1._Bank__kill()
print(f'у вас обнулился баланс')


