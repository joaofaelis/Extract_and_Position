from src.service.ExcelService.Service import ServicesOpenPyXl
from src.service.Services_Interface.service import ServiceInterface
from decouple import config
import openpyxl

book = openpyxl.load_workbook(config(''), data_only=True)
while True:

    print(
        """
    [1] - Inserir novo sistema ao Banco de Dados.
    [2] - Update em sistema ou dependência já existente.
    [3] - Deletar um Sistema.
    [4] - Start em automatização no arquivo .XLS.
    [0] - EXIT.
    """
    )
    try:

        option = int(input("Digite a opção desejada: "))

        if option == 0:
            print("system shut down")
            break

        elif option == 1:
            ServiceInterface.create_interface()
            print("Sucess.")

        elif option == 2:
            ServiceInterface.update_one()

        elif option == 3:
            ServiceInterface.delete_one()

        elif option == 4:
            ServicesOpenPyXl.insert_data_plan()

    except:
        print("Option Invalid.")
        continue
