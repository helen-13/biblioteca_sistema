from datetime import datetime, timedelta

# Classe Emprestimo
class Emprestimo:
    def __init__(self, usuario, exemplar, data_emprestimo):
        self._usuario = usuario
        self._exemplar = exemplar
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = None
        self._estado = "Emprestado"
        self._renovacoes = 0

    @property
    def usuario(self):
        return self._usuario

    @property
    def exemplar(self):
        return self._exemplar

    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    @property
    def data_devolucao(self):
        return self._data_devolucao

    @property
    def estado(self):
        return self._estado

    def devolver(self):
        self._data_devolucao = datetime.now()
        self._estado = "Devolvido"
        self._exemplar.devolver()

    def renovar(self, livro):
        if livro._max_renovacoes is None or self._renovacoes < livro._max_renovacoes:
            self._renovacoes += 1
            return True
        return False
