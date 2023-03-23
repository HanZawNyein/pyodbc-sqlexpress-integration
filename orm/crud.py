import os
import logging
import pyodbc
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class Crud:
    DRIVER = os.getenv('DRIVER')
    SERVER = os.getenv("SERVER")
    PORT = os.getenv("PORT")
    DATABASE = os.getenv("DATABASE")
    UID = os.getenv("UID")
    PWD = os.getenv("password")

    def __init__(self) -> None:
        __connection_str = f'DRIVER={{{self.DRIVER}}};SERVER={self.SERVER},{self.PORT};DATABASE={self.DATABASE};UID={self.UID};PWD={self.PWD}'
        logging.warning(__connection_str)
        cnxn = pyodbc.connect(__connection_str)
        self.cursor = cnxn.cursor()

    def get_cursor(self):
        return self.cursor

    def get_table_columns(self, table_name):
        query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' ORDER BY ORDINAL_POSITION"
        return [table[0] for table in self.execute(query=query)]

    def get_all_tables(self):
        query = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='{os.getenv('DATABASE')}'"
        return [table[0] for table in self.execute(query=query)]

    def read_table(self, table_name: str, *, columns: list[str] | None = None):
        query = f"SELECT * FROM {table_name}"
        if columns is not None:
            query = query.replace("*", ','.join(columns))
        # query += f"From {table_name}"
        # print()
        data = self.execute(query=query)
        columns = self.get_table_columns(table_name=table_name)
        # self.data_crawler(table_name=table_name, data=data)
        # return data
        return sorted(self.data_crawler(table_name=table_name, data=data, columns=columns), key=lambda x: x['Id'])

    def execute(self, query: str) -> list[str]:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def data_crawler(self, table_name, data, *, columns):
        result = list()
        # columns = self.get_table_columns(table_name=table_name)
        for single_record in data:
            result_single = dict()
            for index, record in enumerate(single_record):
                result_single[columns[index]] = record
            result.append(result_single)
            # print(result_single)
            # print(result)
            # print(columns)
        return result

    def insert(self, table_name, values):
        # query = f"INSERT INTO {table_name} {tuple(values.keys())} VALUES {tuple(values.values())};"
        query = f"INSERT INTO {table_name} VALUES {tuple(values.values())};"
        self.cursor.execute(query)

    def update(self, table_name, values, *, Id):
        # query = f"UPDATE {table_name} SET column1 = value1, column2 = value2, ... WHERE condition;"
        update_data = list()
        for key, value in values.items():
            if isinstance(value, int):
                _ = f"{key}={value}"
            else:
                _ = f"{key}='{value}'"
            update_data.append(_)
        query = f"UPDATE {table_name} SET {','.join(update_data)} WHERE Id={Id};"
        self.cursor.execute(query)

    def delete(self, table_name, *, Id):
        # query =f"DELETE FROM table_name WHERE condition;"
        query = f"DELETE FROM {table_name} WHERE Id={Id};"
        self.cursor.execute(query)


if __name__ == "__main__":
    crud = Crud()
    all_tables = crud.get_all_tables()
    # for table in all_tables:
    # print("*"*10)
    table_columns = crud.get_table_columns(table_name=all_tables[0])
    # table_columns = ['Id','OrderNo']
    # data = crud.read_table(table_name=all_tables[0], columns=table_columns)
    print(crud.read_table(table_name=all_tables[0], columns=table_columns))
    # print(table_columns)

    # crud.insert(all_tables[0], {
    #     'OrderNo': 'O00011',
    #     'Customer_Id': 2,
    #     'Order_Date': '2023-03-13',
    #     'Received_Date': '2023-03-15'
    # })

    # crud.update(table_name=all_tables[0], values={
    #             'OrderNo': 'O00012', 'Customer_Id': 2}, Id=21)


    # crud.delete(table_name=all_tables[0],Id=21)
    # print(crud.read_table(table_name=all_tables[0], columns=table_columns))
