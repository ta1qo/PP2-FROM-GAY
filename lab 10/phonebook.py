import csv
import psycopg2

conn = psycopg2.connect(dbname = "postgres",
                        user = "postgres",
                        host = 'localhost',
                        password = "1234",
                        port = 5432)

cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS phonebook(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    surname VARCHAR(20),
                    phone VARCHAR(11))
            ''')

def exist(item):
    cur.execute('SELECT * FROM phonebook WHERE name = %s AND surname = %s AND phone = %s', (item[0], item[1], item[2]))
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

def show():
    cur.execute('SELECT * FROM phonebook')
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
                cur.execute('INSERT INTO phonebook(name, surname, phone) VALUES (%s, %s, %s)', (item[0], item[1], item[2]))
                print(f"new user: {item}")
        conn.commit()
        if input("\n0 - return to menu: ") == '0':
            menu()

def add():
    print("enter data for new user by this order -> name, surname, phone):")
    new_user = list(map(str, input().split()))  
    if not exist(new_user):
        cur.execute('INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)', new_user)
        print("added new user")
        conn.commit()
    else:
        print("this user already exists")
    if input("\n0 - return to menu: ") == '0':
        menu()

def update():
    print("enter name and new phone number:")
    new_phone = tuple(map(str, input().split()))
    cur.execute('SELECT * FROM phonebook WHERE name = %s', (new_phone[0], ))
    if cur.fetchone():
        cur.execute('UPDATE phonebook SET phone = %s WHERE name = %s', new_phone)                   
        print(f"updated phone number for {new_phone[0]}")
        conn.commit()
    else:
        print(f"user - {new_phone[0]} does not exist")
    if input("\n0 - return to menu: ") == '0':
        menu()

def sortbyname():
    cur.execute('SELECT * FROM phonebook ORDER BY name')
    rows = cur.fetchall()
    print("sorted by name: ")
    for row in rows:
        print(row)
    conn.commit()
    if input("\n0 - return to menu: ") == '0':
        menu()

def sortbysurname():
    cur.execute('SELECT * FROM phonebook ORDER BY surname')
    rows = cur.fetchall()
    print("sorted by surname: ")
    for row in rows:
        print(row)
    conn.commit()
    if input("\n0 - return to menu: ") == '0':
        menu()

def search():
    mystring = input("enter name/surname to find user: ")
    cur.execute('SELECT * FROM phonebook WHERE name = %s OR surname = %s', (mystring, mystring))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
        conn.commit()
    else:
        print(f"user - {mystring} does not exist")
    if input("\n0 - return to menu: ") == '0':
        menu()
    
def delete():
    name = input("enter name to delete: ")
    cur.execute(f"SELECT * FROM phonebook WHERE name = '{name}'")
    if cur.fetchone():
        cur.execute(f"DELETE FROM phonebook WHERE name = '{name}'")
        print(f"user - {name} deleted")
        conn.commit()
    else:
        print(f"user - {name} does not exist")
    if input("\n0 - return to menu: ") == '0':
        menu()


menu()    

conn.commit()
cur.close()
conn.close()