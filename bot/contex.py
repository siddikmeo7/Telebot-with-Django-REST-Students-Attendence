from apis.secrets import PASSWORD,NAME,USER,PORT,HOST
import psycopg2
from datetime import datetime
from django.db import models

def open_connection():
    conn = psycopg2.connect(
        database=NAME,
        user=USER,
        host=HOST,
        password=PASSWORD,
        port=PORT
    )
    return conn

def close_connection(conn, cur):
    cur.close()
    conn.close()

def save_students(message):
    conn = open_connection()
    cur = conn.cursor()
    current_time = datetime.now()
    query = """
        INSERT INTO apis_users (
            telegram_id,
            username,
            f_name,
            l_name,
            created_at,
            is_active
        )
        VALUES (%s, %s, %s, %s, %s,%s)
    """
    first_name = message.chat.first_name if message.chat.first_name else None
    last_name = message.chat.last_name if message.chat.last_name else None
    cur.execute(query, (message.chat.id, message.chat.username, first_name, last_name, current_time, True))
    conn.commit()
    close_connection(conn, cur)

def save_students_come(message):
    conn = open_connection()
    cur = conn.cursor()
    current_time = datetime.now()
    query = """
        INSERT INTO apis_attendens (user_id, attended_time, come, created_at,is_active,gone)
        VALUES (
            (SELECT id FROM apis_users WHERE telegram_id = '%s'),
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """
    cur.execute(query, (message.chat.id, current_time, True, current_time, True, False))
    conn.commit()
    close_connection(conn, cur)

def save_students_notcome(message, reason):
    conn = open_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO apis_attendens (user_id, reason, missed_time, come, created_at, is_active)
        VALUES (
            (SELECT id FROM apis_users WHERE telegram_id = '%s'),
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """
    cur.execute(query, (message.chat.id, reason, datetime.now(), False, datetime.now(), True)) 
    conn.commit()
    close_connection(conn, cur)


def save_students_come2(message, username):
    conn = open_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO apis_users (telegram_id, username, f_name, l_name)
        VALUES ('%s', %s, %s, %s)
    """
    cur.execute(query, (message.chat.id, username, message.chat.first_name, message.chat.last_name))
    conn.commit()
    close_connection(conn, cur)

def get_student(id):
    conn = open_connection()
    cur = conn.cursor()
    current_year_day = datetime.now().timetuple().tm_yday
    query = """
        SELECT * FROM apis_attendens
        WHERE EXTRACT(DOY FROM attended_time) = %s
        AND user_id = (SELECT id FROM apis_users WHERE telegram_id = %s)
    """
    cur.execute(query, (current_year_day, str(id)))
    student = cur.fetchone()
    close_connection(conn, cur)
    return False if student else True

def get_student1(id):
    conn = open_connection()
    cur = conn.cursor()
    query = """
        SELECT * FROM apis_users
        WHERE telegram_id = '%s'
    """
    cur.execute(query, (id,))
    student = cur.fetchone()
    close_connection(conn, cur)
    return False if student else True




def show_who_be1(id):
    conn = open_connection()
    cur = conn.cursor()
    current_date = datetime.now()
    query = """
        SELECT * FROM apis_attendens
        WHERE come = True
        AND attended_time = %s
        AND user_id = (SELECT id FROM apis_users WHERE telegram_id = '%s')
        AND gone ISNULL
    """
    cur.execute(query, (current_date,id,))
    student = cur.fetchone()
    print(student)
    close_connection(conn, cur)
    return student


def update_out(id):
    conn = open_connection()
    cur = conn.cursor()
    query = """
        UPDATE apis_attendens
        SET timeout_time = NOW(), gone = True
        WHERE user_id = (SELECT id FROM apis_users WHERE telegram_id = '%s')
    """
    cur.execute(query, (id,))
    conn.commit()
    close_connection(conn, cur)

def update_user(id, group):
    conn = open_connection()
    cur = conn.cursor()
    query = """
        UPDATE apis_users_group
        SET groups_id = (SELECT id FROM apis_groups WHERE name_group = '%s')
        WHERE users_id = (SELECT id FROM apis_users WHERE telegram_id = '%s')
    """
    cur.execute(query, (group, id))
    conn.commit()
    close_connection(conn, cur)

def get_student2(id):
    conn = open_connection()
    cur = conn.cursor()
    query = """
        SELECT * FROM apis_users_group
        WHERE users_id = (SELECT id FROM apis_users WHERE telegram_id = '%s') 
        AND groups_id IS NULL
    """
    cur.execute(query, (id,))
    student = cur.fetchone()
    close_connection(conn, cur)
    return False if student else True


def get_groups():
    conn = open_connection()
    cur = conn.cursor()
    query = """
        SELECT * FROM apis_groups
    """
    cur.execute(query)
    student = cur.fetchall()
    close_connection(conn, cur)
    return student
