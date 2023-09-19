from hw4 import Prokuror
from hw4 import KNB
from hw4 import Antikor
from hw4 import Akim


class President(Prokuror, KNB, Antikor, Akim):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age

    @property
    def getage(self):
        return self.__age

    @getage.setter
    def getage(self, value):
        self.__age = value
