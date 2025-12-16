class CorpoCeleste:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

    def descrever(self):
        return f"{self.nome} é um corpo celeste do tipo {self.tipo}."
