from corpos_celestes import CorpoCeleste

class Estrela(CorpoCeleste):
    def __init__(self, nome: str, cor: str, luminosidade: str):
        super().__init__(nome, "Estrela")
        self.cor = cor
        self.luminosidade = luminosidade

    def brilhar(self):
        return f"A estrela {self.nome} está brilhando."

    def fundir_elementos(self):
        return f"A estrela {self.nome} está realizando fusão nuclear."

    def descrever(self):
        return (
            f"O {self.nome} é uma estrela {self.cor} "
            f"do tipo {self.luminosidade}."
        )

