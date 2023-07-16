import openpyxl
import json


class Formater:
    def __init__(self) -> None:
        self.url_file = "data/СВОД 2022.xlsx"
        self.url_file_2 = "data/СВОД 2023 6 мес.xlsx"

    def format_update(self, ai):
        # Открываем файл Excel

        workbook = openpyxl.load_workbook(self.url_file)

        # Выбираем активный лист
        sheet = workbook.active

        # Создаем список для хранения данных
        data_in_column_E = []
        data_in_column_B = []

        # Проходимся в цикле по всем ячейкам в столбце
        for cell, cell_2 in zip(sheet['E'], sheet['B']):
            # Добавляем значение ячейки в список
            data_in_column_E.append(cell.value)
            data_in_column_B.append(cell_2.value)

        mass = []
        for ai_, column_B, column_E in zip(ai, data_in_column_B, data_in_column_E):
            mass.append({"price": ai_[0], "month": column_B, "class": column_E})

        # Возвращаем данные
        return mass
    
    def create_json(self, ai):
        with open("file.json", "w", encoding="UTF-8") as file:
            json.dump(self.format_update(ai), file)
    

class Result_data:
    def __init__(self) -> None:
        self.url_file = "file.json"

    def update_data(self):
        with open(self.url_file, "r", encoding='UTF-8') as file:
            content = file.read()

        print(content)


RES = Result_data()
RES.update_data()