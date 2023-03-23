from orm import crud

all_tables = crud. all_tables = crud.get_all_tables()
print(f"[+] ALl Tables .... {all_tables}")
for table in all_tables:
    print("*"*10, '\n')
    table_columns = crud.get_table_columns(table_name=table)
    # table_columns = ['Id','OrderNo']
    print(f"[+] {table} of Columns {table_columns}\n")
    # data = crud.read_table(table_name=table, columns=table_columns)
    # print(data)
    # print(table_columns)

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
