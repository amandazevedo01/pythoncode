class Calculadora:
    def __init__(self):
        pass
    def soma(self,valor_a,valor_b):
        return valor_a + valor_b
    def subtracao(self,valor_a,valor_b):
        return valor_a - valor_b
    def multiplicacao(self,valor_a,valor_b):
        return valor_a * valor_b
    def divisao(self,valor_a,valor_b):
        return valor_a / valor_b
calculadora = Calculadora()
print(calculadora.soma(5,2))
print(calculadora.subtracao(3,2))
print(calculadora.multiplicacao(1,1))
print(calculadora.divisao(10,2))