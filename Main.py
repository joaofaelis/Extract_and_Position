from src.service.ExcelService.Service import services
from src.service.service import Service
import openpyxl

book = openpyxl.load_workbook('sistemas2.xlsx', data_only=True)
while True:

    print(
        """
    [1] - Inserir Sistema ao MONGODB.
    [2] - Update.
    [3] - Delete.
    [4] - Start Excel Service.
    [0] - EXIT.
    """
    )
    try:

        option = int(input("Digite a opção desejada: "))

        if option == 0:
            print("system shut down")
            break

        elif option == 1:
            Service.create_data()
            print("Sucess.")

        elif option == 2:
            Service.update_one()

        elif option == 3:
            Service.delete_onee()

        elif option == 4:
            services.insert_plan()

    except:
        print("Option Invalid.")
        continue
