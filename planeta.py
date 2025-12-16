from corpos_celestes import CorpoCeleste

class Planeta(CorpoCeleste):
    def __init__(self, nome: str, tipo_planeta: str):
        super().__init__(nome, "Planeta")
        self.tipo_planeta = tipo_planeta
        self.satelites = []

    def adicionar_satelite(self, nome_satelite: str):
        if nome_satelite not in self.satelites:
            self.satelites.append(nome_satelite)

    def remover_satelite(self, nome_satelite: str):
        if nome_satelite in self.satelites:
            self.satelites.remove(nome_satelite)

    def listar_satelites(self):
        return self.satelites

    def sofrer_impacto(self):
        return f"O planeta {self.nome} sofreu um impacto."

    def descrever(self):
        luas = ", ".join(self.satelites) if self.satelites else "nenhuma lua"
        return (
            f"{self.nome} é um planeta {self.tipo_planeta} "
            f"que possui {luas}."
        )
