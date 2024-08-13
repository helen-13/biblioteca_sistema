from abc import ABC, abstractmethod

# Classe abstrata para Pessoa
class Pessoa(ABC):
    def __init__(self, nome, telefone, nacionalidade):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @abstractmethod
    def descricao(self):
        pass

# Classe Autor que herda de Pessoa
class Autor(Pessoa):
    def descricao(self):
        return f"Autor: {self.nome}, Nacionalidade: {self.nacionalidade}"

# Classe Usuario que herda de Pessoa
class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)
        self._emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def descricao(self):
        return f"Usu\u00e1rio: {self.nome}, Telefone: {self.telefone}"
