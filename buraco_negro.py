from corpos_celestes import CorpoCeleste

class BuracoNegro(CorpoCeleste):
    def __init__(self, nome: str, tipo_buraco: str):
        super().__init__(nome, "Buraco Negro")
        self.tipo_buraco = tipo_buraco

    def absorver(self):
        return f"O buraco negro {self.nome} está absorvendo matéria."

    def atrair(self):
        return f"O buraco negro {self.nome} está atraindo objetos ao redor."

    def descrever(self):
        return (
            f"{self.nome} é um buraco negro do tipo {self.tipo_buraco}."
        )
