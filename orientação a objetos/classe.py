class Carro:
    def __init__(self, marca, modelo, ano, proprietario):
        self.__marca= marca
        self.__modelo= modelo
        self.__ano= ano
        self.__proprietario= proprietario

    @property
    def info(self):
        return print('marca: {} \n modelo: {} \n ano: {} \n proprietário: {}'.format(self.__marca, self.__modelo, self.__ano, self.__proprietario))
    
    @info.setter
    def info(self, modelo):
        self.__modelo= modelo

    @staticmethod
    def ola():
        return print("bom dia companheiro")