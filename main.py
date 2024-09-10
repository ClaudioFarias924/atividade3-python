class aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    
    def get_nome(self):
        return self.__nome

    
    def set_nome(self, nome):
        self.__nome = nome


    def get_nota1(self):
        return self.__nota1

    
    def set_nota1(self, nota1):
        self.__nota1 = nota1


    def get_nota2(self):
        return self.__nota2

    
    def set_nota2(self, nota2):
        self.__nota2 = nota2


    def calcular_media (self):
        return (self.__nota1 + self.__nota2) / 2
    

aluno1 = aluno("Cláudio", 8.5, 9.3)
print(f"Nome: {aluno1.get_nome()}")
print(f"Nota1: {aluno1.get_nota1()}")
print(f"Nota2: {aluno1.get_nota2()}")
print(f"Média: {aluno1.calcular_media():.2f}")

aluno2 = aluno("Mariana", 8.5, 6.5)
print(f"\nNome: {aluno2.get_nome()}")
print(f"Nota1: {aluno2.get_nota1()}")
print(f"Nota2: {aluno2.get_nota2()}")
print(f"Média: {aluno2.calcular_media():.2f}")