import sqlite3

class Person:
    def __init__(self, filename):
        self.filename = filename

    def create_person(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("""CREATE TABLE if not exists system_log (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                name_system text NOT NULL, 
                                                                email text NOT NULL, 
                                                                password text NOT NULL)""")
        n = int(input('the number of people to create:'))
        for i in range(n):
            name_system = input('enter name_system:')
            email = input('enter your email:')
            password = input('enter your parol:')
            curs.execute("INSERT INTO system_log VALUES(NULL,?,?,?)", (name_system, email, password))
        conn.commit()
        conn.close()

    def add_person(self):
        '''додати нового користувача до бд'''
        name_system = input('enter name_system:')
        email = input('enter your email:')
        parol = input('enter your login:')
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO system_log VALUES(NULL,?,?,?)", (name_system, email, parol))
        conn.commit()
        conn.close()

    def update_person_password(self):
        old_email = input('enter old email:')
        new_password = input('enter your new password:')
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("UPDATE system_log SET password=? WHERE email=?", (new_password, old_email))
        conn.commit()
        conn.close()

    def updatet_email_person(self):
        old_email = input('enter old email:')
        new_email = input('enter your new email:')
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''UPDATE system_log SET email ='new_email' WHERE email = 'old_email' ''')
        conn.commit()
        conn.close()

    def delete_person(self):
        your_email = input('enter your email for delete:')
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''DELETE FROM system_log WERE system, email = your_email, parol''')
        conn.commit()
        conn.close()

    def return_info_in_base(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''SELECT * FROM system_log''')
        result = curs.fetchall()
        curs.close()
        print(result)

filename = 'register_person.db'

rb = Person(filename)

while True:
    k = int(input('k:'))
    if k==1:
        print('Запис до бази даних кількох користувачів')
        rb.create_person()
    elif k==2:
        print('Додавання до бази даних нового користувача')
        rb.add_person()
    elif k==3:
        print('Зміна паролю')
        rb.update_person_password()
    elif k==4:
        print('Зміна електронної адреси')
        rb.updatet_email_person()
    elif k==5:
        print('Видалити користувача')
        rb.delete_person()
    elif k==6:
        print('Всі дані з бази даних')
        rb.return_info_in_base()
    elif k==7:
        break