from src.infra.Mongo.infra import MongoInfrastructure
from src.repository.mongo.repository_mongo import MongoRepository
from datetime import datetime

class ServiceInterface:

    database = MongoInfrastructure.get_db_and_collection()
    repository = MongoRepository

    @classmethod
    def create_interface(cls):
        list_dependencies = []

        while True:
            name_system = input("Nome do sistema: ")
            option = int(input("Se o sistema tiver dependência digite 1 P/INSERIR ou 2 P/SAIR: "))

            if option == 1:
                while True:
                    dependence = input("Digite o nome da dependência ou 0 para sair: ")
                    if dependence == 0:
                        break
                    list_dependencies.append(dependence)
                    print(f"Dependências adicionadas: {[list_dependencies]}")

            if option == 2:
                pass

            create = {
                "nome_do_sistema": name_system,
                "dependencias": list_dependencies,
                "created_at": datetime.now(),
            }

            result = cls.repository.insert_one(create)
            return result

    @classmethod
    def read_all(cls):
        skip = 0
        limit = 10
        ler = cls.repository.get_all(skip, limit)
        print(ler)

    @classmethod
    def read_one(cls):
        name = input("Digite o nome do sistema: ")
        read_one = {"nome_do_sistema": name}
        ler = cls.repository.get_one(read_one)
        print(ler)

    @classmethod
    def update_one(cls):
        while True:
            option_update = input("Digite [1] para atualizar os dados ou [0] para Sair: ")
            if option_update == '0':
                break

            elif option_update == '1':
                name_system = input("Digite o nome do sistema para ser atualizado: ")
                old = {"nome_do_sistema": name_system}
                option_for_update = int(input("Escolha [1] para atualizar nome do sistema ou [2] para dependencia e [0] para SAIR: "))

                if option_for_update == 0:
                    break

                elif option_update == 1:
                    update_name = input("Digite o novo nome: ")
                    new = {"nome_do_sistema": update_name}
                    print(f"O novo nome do sistema passa a ser: '{update_name}'")

                elif option_for_update == 2:
                    dependencies_list = []
                    while True:
                        dependencies = input(
                            "Digite o nome da dependência ou [0] para SAIR: "
                        )

                        if dependencies == 0:
                            break

                        dependencies_list.append(dependencies)
                        new = {"dependencias": dependencies_list}
                        print(f"As dependencias adicinadas foram: '{dependencies_list}'")

                        cls.repository.update_data(old, new)

    @classmethod
    def delete_one(cls):
        name_system = input("Digite o nome do sistema a ser deletado: ")
        data_name = {"nome_do_sistema": name_system}
        data_db = cls.repository.delete_data(data_name)

        if data_db:
            print("Dados deletados com sucesso.")
        else:
            print("Não encontrado.")
