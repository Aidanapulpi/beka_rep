class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        try:
            amount = int(input('введите сумму которую хотите пополнить:'))
            if amount > 0:
                self._balanse += amount
            else:
                print('сумма должна быть бтльше 0')
        except ValueError:
            print('введите корректное число')

    def __str__(self):
        return self._name, self._balanse

    def _kill(self):
        self._balanse = 0


    def __jackpot(self):
        self._balanse *= 10
        print("вы выиграли джекпот, деньги умножены на 10")

    def _wix(self, other):
        other._balanse += self._balanse

    def get_balance(self):
        return self._balanse


user1 = Bank('aidana', 23)

user1._Bank__jackpot()
print(f'Ваш текущий баланс: {user1.get_balance()}')
user1.moneyX()
print(f'Теперь ваш баланс: {user1.get_balance()}')

beka = Bank('Beka', 2000)
print(f'Изначальный баланс Беки: {beka.get_balance()}')
user1._wix(beka)

print(f'Теперь баланс беки: {beka.get_balance()}')

user1._kill()
print(f'у вас обнулился баланс')


