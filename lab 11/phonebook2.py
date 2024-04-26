import csv
import psycopg2
import re

conn = psycopg2.connect(dbname = "postgres",
                        user = "postgres",
                        host = 'localhost',
                        password = "1234",
                        port = 5432)

cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS phonebook2(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    surname VARCHAR(20),
                    phone VARCHAR(11))
            ''')

def exist(item):
    cur.execute('SELECT * FROM phonebook2 WHERE name = %s AND surname = %s AND phone = %s', (item[0], item[1], item[2]))
    row = cur.fetchone() # row=none if not exist
    return True if row else False

def menu():
    print('''
        1 - show all users
        2 - upload data from csv
        3 - add user from console
        4 - update phone number
        5 - sort by name
        6 - sort by surname
        7 - search user
        8 - delete user
        9 - insert by list
            ''')
    num = input("enter number: ")
    if num == '1':
        show()
    elif num == '2':
        upload()
    elif num == '3':
        add()
    elif num == '4':
        update()
    elif num == '5':
        sortbyname()
    elif num == '6':
        sortbysurname()
    elif num == '7':
        search()
    elif num == '8':
        delete()
    elif num == '9':
        insertbylist()

def show():
    cur.execute('SELECT * FROM phonebook2')
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    if input("\n0 - return to menu: ") == '0':
        menu()

def upload():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for item in reader:    
            if not exist(item):
                cur.execute('INSERT INTO phonebook2(name, surname, phone) VALUES (%s, %s, %s)', (item[0], item[1], item[2]))
                print(f"new user: {item}")
        conn.commit()

        if input("\n0 - return to menu: ") == '0':
            menu()

def add():
    print("enter data for new user by this order -> name, surname, phone):")
    new_user = list(map(str, input().split()))  

    if not exist(new_user):
        cur.execute('INSERT INTO phonebook2 (name, surname, phone) VALUES (%s, %s, %s)', new_user)
        print("added new user")
        conn.commit()
    elif exist(new_user):
        cur.execute('UPDATE phonebook2 SET phone = %s WHERE surname = %s AND name = %s', (new_user[2], new_user[1], new_user[0]))
        print(f"updated phone number for {new_user[0]}")
    else:
        print("this user already exists")

    if input("\n0 - return to menu: ") == '0':
        menu()

def update():
    print("enter name and new phone number:")
    new_phone = tuple(map(str, input().split()))
    cur.execute('SELECT name FROM phonebook2 WHERE name = %s', (new_phone[0], ))

    if cur.fetchone():
        cur.execute('UPDATE phonebook2 SET phone = %s WHERE name = %s', (new_phone[1], new_phone[0]))                   
        print(f"updated phone number for {new_phone[0]}")
        conn.commit()
    else:
        print(f"user - {new_phone[0]} does not exist")

    if input("\n0 - return to menu: ") == '0':
        menu()

def sortbyname():
    cur.execute('SELECT * FROM phonebook2 ORDER BY name')
    rows = cur.fetchall()
    print("sorted by name: ")
    for row in rows:
        print(row)
    conn.commit()

    if input("\n0 - return to menu: ") == '0':
        menu()

def sortbysurname():
    cur.execute('SELECT * FROM phonebook2 ORDER BY surname')
    rows = cur.fetchall()
    print("sorted by surname: ")
    for row in rows:
        print(row)
    conn.commit()

    if input("\n0 - return to menu: ") == '0':
        menu()

def search():
    mypattern = input("enter pattern of name/surname/phone to find users: ")
    mode = input("search by name/surname/phone? ")
    if mode == "name":
        cur.execute('SELECT * FROM phonebook2 WHERE name ILIKE %s', (f'%{mypattern}%', ))
    elif mode == "surname":
        cur.execute('SELECT * FROM phonebook2 WHERE surname ILIKE %s', (f'%{mypattern}%', ))
    elif mode == "phone":
        cur.execute('SELECT * FROM phonebook2 WHERE phone LIKE %s', (f'%{mypattern}%', ))

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print(f"'{mypattern}' not found")

    if input("\n0 - return to menu: ") == '0':
        menu()
    
def delete():
    mode = input("delete by name/phone: ")

    if mode == "name":
        name = input("enter name to delete: ")
        cur.execute(f"SELECT name FROM phonebook2 WHERE name = '{name}'")
        if cur.fetchone():
            cur.execute(f"DELETE FROM phonebook2 WHERE name = '{name}'")
            print(f"user - {name} deleted")
            conn.commit()
    elif mode == "phone":
        phone = input("enter phone to delete: ")
        cur.execute(f"SELECT phone FROM phonebook2 WHERE phone = '{phone}'")
        if cur.fetchone():
            cur.execute(f"DELETE FROM phonebook2 WHERE phone = '{phone}'")
            print(f"user with phone - {phone} deleted")
            conn.commit()
    else:
        print(f"user does not exist")

    if input("\n0 - return to menu: ") == '0':
        menu()

def insert(data):
    if not exist(data):
        cur.execute('INSERT INTO phonebook2 (name, surname, phone) VALUES (%s, %s, %s)', data)
        print("added new user")
        conn.commit()
    else:
        print("this user already exists")

def insertbylist():
    incorrect_data = []
    while True:
        mode = input("want to add user? yes/no: ")
        if mode == "no":
            break
        elif mode == "yes":
            print("enter data for new user by this order -> name, surname, phone):")
            new_user = list(map(str, input().split()))  

            if len(new_user) != 3:
                incorrect_data.append(new_user)
                continue
            elif not re.match(r'^7[0-9]{10}$', new_user[2]):
                incorrect_data.append(new_user)
                print('4')
                continue
            elif not re.match(r"^[A-Z][a-z]*$", new_user[0]) or not re.match(r"^[A-Z][a-z]*$", new_user[1]):
                incorrect_data.append(new_user)
                continue
            else:
                insert(new_user)

    if len(incorrect_data) == 0:
        return
    
    print("\nThis data were not added due to incorrect format: ")
    for i in incorrect_data:
         print(i)

    if input("\n0 - return to menu: ") == '0':
        menu()



menu()    

conn.commit()
cur.close()
conn.close()