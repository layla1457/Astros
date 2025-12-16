from estrela import Estrela
from planeta import Planeta
from buraco_negro import BuracoNegro

def menu():
    print(" ~~~ Menuzinho ~~~")
    print("<1> Listar tipos de astros")
    print("<2> Listar astros por tipo")
    print("<3> Descrever um astro")
    print("<4> Adicionar estrela")
    print("<5> Adicionar planeta")
    print("<6> Adicionar buraco negro")
    print("<0> Sair")


def main():
    astros = []

    sol = Estrela("Sol", "amarela", "anã")
    terra = Planeta("Terra", "terrestre")
    terra.adicionar_satelite("Lua")
    sagitario_a = BuracoNegro("Sagitário A*", "supermassivo")

    astros.extend([sol, terra, sagitario_a])

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Tipos de astros disponíveis:")
            print("- Estrela")
            print("- Planeta")
            print("- Buraco Negro")

        elif opcao == "2":
            tipo = input("Digite o tipo (Estrela/Planeta/Buraco Negro): ")
            print(f"Astros do tipo {tipo}:")
            for astro in astros:
                if astro.tipo.lower() == tipo.lower():
                    print(f"- {astro.nome}")

        elif opcao == "3":
            tipo = input("Digite o tipo (Estrela/Planeta/Buraco Negro): ")
            print(f"Astros do tipo {tipo}:")
            for astro in astros:
                if astro.tipo.lower() == tipo.lower():
                    print(f"- {astro.nome}")

            nome = input("Digite o nome do astro: ")
            encontrado = False
            for astro in astros:
                if astro.nome.lower() == nome.lower():
                    print("\n" + astro.descrever())
                    encontrado = True
                    break
            if not encontrado:
                print("Astro não encontrado.")

        elif opcao == "4":
            nome = input("Nome da estrela: ")
            cor = input("Cor da estrela: ")
            luminosidade = input("Tipo (ex: anã, gigante): ")
            astros.append(Estrela(nome, cor, luminosidade))
            print("Estrela adicionada com sucesso!")

        elif opcao == "5":
            nome = input("Nome do planeta: ")
            tipo = input("Tipo do planeta (terrestre/gasoso): ")
            planeta = Planeta(nome, tipo)

            while True:
                lua = input("Adicionar lua (ou ENTER para sair): ")
                if lua == "":
                    break
                planeta.adicionar_satelite(lua)

            astros.append(planeta)
            print("Planeta adicionado com sucesso!")

        elif opcao == "6":
            nome = input("Nome do buraco negro: ")
            tipo = input("Tipo (ex: supermassivo): ")
            astros.append(BuracoNegro(nome, tipo))
            print("Buraco negro adicionado com sucesso!")

        elif opcao == "0":
            print("Encerrando o programa... Tchau!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
