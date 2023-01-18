from src.repository.mongo.repository import conection
from datetime import datetime

class Service:
    repository = conection

    @classmethod
    def create_data(cls):
        lista_dependencia = []

        while True:
            nome_do_sistema = input("Nome do sistema: ")
            option = int(input("Se o sistema tiver dependência digite 1 P/INSERIR ou 2 P/SAIR: "))

            if option == 1:
                while True:
                    dependencia = input("Digite o nome da dependência ou 0 para sair: ")
                    if dependencia == 0:
                        break
                    lista_dependencia.append(dependencia)
                    print(f"Dependências adicionadas: {[lista_dependencia]}")

            if option == 2:
                pass

            create = {
                "nome_do_sistema": nome_do_sistema,
                "dependencias": lista_dependencia,
                "created_at": datetime.now(),
            }

            resultado = cls.repository.insert_one(create)
            return resultado

    @classmethod
    def read_all(cls):
        skip = 0
        limit = 10
        ler = cls.repository.get_all_coletor(skip, limit)
        print(ler)

    @classmethod
    def read_one(cls):
        nome = input("Digite o nome do sistema: ")
        lendo_um = {"nome_do_sistema": nome}
        ler = cls.repository.get_coletor(lendo_um)
        print(ler)

    @classmethod
    def update_one(cls):
        while True:
            option_update = input("Digite [1] para atualizar os dados ou [0] para Sair: ")
            if option_update == '0':
                break

            elif option_update == '1':
                nome_sistema = input("Digite o nome do sistema para ser atualizado: ")
                old = {"nome_do_sistema": nome_sistema}
                opcao_for_update = int(input("Escolha [1] para atualizar nome do sistema ou [2] para dependencia e [0] para SAIR: "))

                if opcao_for_update == 0:
                    break

                elif opcao_for_update == 1:
                    atualizacao_nome = input("Digite o novo nome: ")
                    new = {"nome_do_sistema": atualizacao_nome}
                    print(f"O novo nome do sistema passa a ser {atualizacao_nome}")

                elif opcao_for_update == 2:
                    depencias_lista = []
                    while True:
                        depencia_sistema = input(
                            "Digite o nome da dependência ou [0] para SAIR: "
                        )

                        if depencia_sistema == 0:
                            break

                        depencias_lista.append(depencia_sistema)
                        new = {"dependencias": depencias_lista}
                        print(f"As dependencias adicinadas foram {depencias_lista}")

        cls.repository.update(old, new)

    @classmethod
    def delete_onee(cls):
        nome_sistema = input("Digite o nome do sistema a ser deletado: ")
        data = {"nome_do_sistema": nome_sistema}
        dt = cls.repository.delete_coletor(data)

        if dt:
            print("Dados deletados com sucesso.")
        else:
            print("Não encontrado.")
