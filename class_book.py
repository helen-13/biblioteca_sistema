
# Classe Livro
class Livro:
    def __init__(self, titulo, editora, generos, max_renovacoes=None):
        self._titulo = titulo
        self._editora = editora
        self._generos = generos
        self._autores = []
        self._exemplares = []
        self._max_renovacoes = max_renovacoes

    @property
    def titulo(self):
        return self._titulo

    @property
    def editora(self):
        return self._editora

    @property
    def generos(self):
        return self._generos

    @property
    def autores(self):
        return self._autores

    @property
    def exemplares_disponiveis(self):
        return [ex for ex in self._exemplares if ex.disponivel]

    def adicionar_autor(self, autor):
        self._autores.append(autor)

    def adicionar_exemplar(self, exemplar):
        self._exemplares.append(exemplar)

    def emprestar_exemplar(self):
        for exemplar in self._exemplares:
            if exemplar.disponivel:
                exemplar.emprestar()
                return exemplar
        return None