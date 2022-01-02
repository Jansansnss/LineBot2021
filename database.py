import os
import psycopg2

DATABASE_URL = "postgres://swvvifcbkvjopu:47fd091255cea8611c4fbdb4d03850a4e7e9776f5318f0d71ec897f35e5de063@ec2-34-246-155-237.eu-west-1.compute.amazonaws.com:5432/d7rffbu2i8mqru"

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

def print_data(name):
    #DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a linebot2021-jansansnss').read()[:-1]
    conn   = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_print_query = f"""Select * from pokemon where name = {name}"""
    print(postgres_print_query)
    try:
        cursor.execute(postgres_print_query)
        conn.commit()
        data = []
        while True:
            temp = cursor.fetchone()
            if temp:
                data.append(temp)
                #print(temp)
            else:
                break
        print(data)
    except:
        print("print_data_errorororororororororororor")
        return "invalid search"
    cursor.close()
    conn.close()
    return data

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

def developer_data_mode(instruction):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_delete_query = f"""{instruction}"""
    try:
        cursor.execute(postgres_delete_query)
        conn.commit()
    except:
        print("developer_data_mode_errorororororororororororor")
    cursor.close()
    conn.close()