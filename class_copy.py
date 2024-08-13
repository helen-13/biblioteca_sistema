# Classe Exemplar
class Exemplar:
    def __init__(self, codigo):
        self._codigo = codigo
        self._disponivel = True

    @property
    def codigo(self):
        return self._codigo

    @property
    def disponivel(self):
        return self._disponivel

    def emprestar(self):
        self._disponivel = False

    def devolver(self):
        self._disponivel = True
