from src.repository.mongo.repository import conection
import openpyxl


class services:
    banco = conection
    projects = list(banco.get_collection().find())
    book = openpyxl.load_workbook('sistemas2.xlsx', data_only=True)
    page = book['Rel. Interno x Interno']

    projects_dict = dict()
    mapeamento = {}

    @classmethod
    def insert_plan(cls):

        row = 4
        while add := cls.page.cell(row=row, column=1).value:
            cls.mapeamento[add.lower()] = {'linha': row, 'column': row - 2 if row < 21 else row}
            row += 1

        projects_dict = dict()
        for project in cls.projects:
            system_name = project.get("nome_do_sistema")
            projects_dict[system_name] = project.get("dependencias")

        for proj_db, dependencias in projects_dict.items():
            position_proj = cls.mapeamento.get(proj_db.lower())
            if position_proj is None:
                print('does not exist', proj_db)
                continue
            for proj_plan in dependencias:
                position_plan = cls.mapeamento.get(proj_plan.lower())
                if position_plan is None:
                    print('does not exist', proj_plan)
                    continue
                cls.page.cell(row=position_proj['linha'], column=position_plan['column']).value = 'x'
                cls.page.cell(row=position_plan['linha'], column=position_proj['column']).value = 'x'
                print('Success')
                pass

        cls.book.save('sistemas2.xlsx')
