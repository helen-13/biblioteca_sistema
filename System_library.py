# Importando bibliotecas
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []
        self._emprestimos = []

    def adicionar_livro(self, livro):
        self._livros.append(livro)

    def adicionar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def realizar_emprestimo(self, usuario, livro):
        exemplar = livro.emprestar_exemplar()
        if exemplar:
            emprestimo = Emprestimo(usuario, exemplar, datetime.now())
            self._emprestimos.append(emprestimo)
            usuario.adicionar_emprestimo(emprestimo)
            return emprestimo
        return None

    def devolver_livro(self, emprestimo):
        emprestimo.devolver()

    def renovar_emprestimo(self, emprestimo, livro):
        return emprestimo.renovar(livro)

    def listar_emprestimos(self):
        return self._emprestimos
