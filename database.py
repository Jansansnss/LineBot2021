#import os
import psycopg2

def insert_data(table_name,table_columns,records):
    #DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a linebot2021-jansansnss').read()[:-1]
    conn   = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    #records = ('Jason', 60, 180, '2021-08-26')
    #table_columns = '(name, weight, height, date)'
    
    postgres_insert_query = f"""INSERT INTO {table_name} {table_columns} VALUES {records}"""
    print(postgres_insert_query)
    try:
        cursor.execute(postgres_insert_query)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into database")
    except:
        print("insert_data_errorororororororororororor")
    cursor.close()
    conn.close()
    return

def print_data(table_name,table_columns):
    #DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a linebot2021-jansansnss').read()[:-1]
    conn   = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_print_query = f"""Select {table_columns} from {table_name}"""
    print(postgres_print_query)
    try:
        cursor.execute(postgres_print_query)
        conn.commit()
        data = []
        while True:
            temp = cursor.fetchone()
            if temp:
                data.append(temp)
                print(temp)
            else:
                break
        print(data)
    except:
        print("print_data_errorororororororororororor")
    cursor.close()
    conn.close()
    return

def update_data(table_name,table_columns,origin_data,new_data):
    #DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a linebot2021-jansansnss').read()[:-1]
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_update_query = f"""UPDATE {table_name} set {table_columns} = %s WHERE {table_columns} = %s"""
    try:
        print(postgres_update_query)
        cursor.execute(postgres_update_query,(new_data,origin_data))
        conn.commit()
    except:
        print("print_data_errorororororororororororor")
    cursor.close()
    conn.close()
    return

def delete_data(table_name,user_id):
    #DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a linebot2021-jansansnss').read()[:-1]
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_delete_query = f"""DELETE FROM {table_name} WHERE user_id = {user_id}"""
    try:
        cursor.execute(postgres_delete_query)
        conn.commit()
    except:
        print("delete_data_errorororororororororororor")
    cursor.close()
    conn.close()