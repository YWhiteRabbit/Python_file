import sqlite3
from tkinter import ttk
import tkinter.ttk as tkk
from tkinter.simpledialog import*


class Colector:
    def __init__(self, filename):
        self.filename = filename

    def create_table_colector(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''CREATE TABLE if not exists password_colector(id  INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    email text NULL, 
                                                                    login text NULL,
                                                                    password text NULL,
                                                                    site text NULL)''')
        conn.commit()
        conn.close()

    def add_one_record(self, email, login, password, site):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO password_colector VALUES(NULL,?,?,?,?)", (email, login, password, site))
        result = curs.fetchall()
        conn.commit()
        conn.close()
        return f"email:{result[0]} login:{result[1]} password:{result[2]} site:{result[3]}"


    def add_persons(self, k):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        for i in range(k):
            email = input('enter email:')
            login = input('enter login:')
            password = input('enter password:')
            site = input('enter the site where register:')
            curs.execute("INSERT INTO password_colector VALUE(NULL,?,?,?,?)", (email, login, password, site))
        conn.commit()
        conn.close()

    def serch_info_for_col_site(self, sites):
        position=[]
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("SELECT email, login, password, site FROM password_colector WHERE site=?", (sites, ))
        p=self.curs.fetchall()
        position.append(p)
        self.conn.commit()
        self.conn.close()
        for line in position:
            return line


    def update_all_info(self):
        old_email = input('enter old email:')
        new_email = input('enter your new email:')
        new_login = input('enter your new login:')
        new_password = input('enter your new password:')
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("UPDATE password_colector SET email ='new_email',"
                     " login='new_login',"
                     "password='new_password'"
                     " WHERE email = 'old_email' ")
        conn.commit()
        conn.close()

    def update_info(self):
        print('Виберіть, що змінюватимете: 1-login, 2-password')
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        site = input('enter site from info update:')
        n=int(input('n:'))
        if n==1:
            curs.execute("UPDATE password_colector SET login ='new_login' WHERE site = 'site_info' ")
            conn.commit()
            conn.close()
        elif n==2:
            curs.execute("UPDATE password_colector SET password ='new_password' WHERE site = 'site_info' ")
            conn.commit()
            conn.close()

    def return_info_in_base(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT * FROM password_colector")
        #result = curs.fetchall()
        curs.close()
        return str(f"email:{curs[0]} login: {curs[1]} password: {curs[2]} site: {curs[3]}")

    def delete(self, del_site, del_email):
        conn=sqlite3.connect(self.filename)
        curs=conn.cursor()
        curs.execute('''DELETE FROM password_colector WHERE (SELECT email, login, password, site FROM password_colector WHERE site=?, email=?", (del_site, del_email, ) )''')
        curs.close()
        return 'Видалено'


#робота з вікном

class WindowsColector(Colector):
    def __init__(self, root, filename):
        '''combobox-ибираємо дію, label-текст, що програма робить,

        button-запускаємо програму, entry-вводимо іноформацію
        додаткове поде для введення нової інформації'''
        self.filename = filename
        self.lb1 = Label(root, text='Виберіть дію серед запропонованих варіантів')
        self.lb2 = Label(root, text='Введіть назву сайту')
        self.lb3 = Label(root, text='Введіть інформацію для подальших дій:')
        self.lb4 = Label(root, text='Електронну пошту:')
        self.lb5 = Label(root, text='Логін:')
        self.lb6 = Label(root, text='Пароль')
        self.lb7 = Label(root, text='Сайт')
        self.action = ['Перегляд інформації', 'Додати', 'Видалити', 'Змінити', 'Вся інформація']
        self.check = StringVar(value=self.action[0])
        self.com = tkk.Combobox(root, textvariable=self.check, values=self.action, height=len(self.action))
        self.ent = Entry()
        self.ent_em = Entry()
        self.ent_log = Entry()
        self.ent_pass = Entry()
        self.ent_site = Entry()
        self.btn1 = Button(root, text='Виконати')
        self.btn2 = Button(root, text='Про програму')
        self.btn3 = Button(root, text='Зберегти зміни')
        self.btn1.config(command=self.button_1)
        self.btn3.config(command=self.button_2)
        self.lb1.grid(row=1, column=2)
        self.lb2.grid(row=1, column=3)
        self.ent.grid(row=2, column=3)
        self.com.grid(row=2, column=2)
        self.btn1.grid(row=4, column=3)
        self.btn2.grid(row=0, column=0)
        self.btn3.grid(row=9, column=4)
        self.lb3.grid(row=6, column=2)
        self.lb4.grid(row=7, column=1)
        self.lb5.grid(row=7, column=2)
        self.lb6.grid(row=7, column=3)
        self.lb7.grid(row=7, column=4)
        self.ent_em.grid(row=8, column=1)
        self.ent_log.grid(row=8, column=2)
        self.ent_pass.grid(row=8, column=3)
        self.ent_site.grid(row=8, column=4)



    def button_1(self):
        self.check1 = self.check.get()
        self.enter_site = self.ent.get()
        self.create_table=self.create_table_colector()
        if self.check1=='Перегляд інформації' and self.enter_site:
            self.result_serch = self.get_text(self.serch_info_for_col_site(self.enter_site))
            #self.lb1_serch = Label(text=self.result_serch).grid(row=10, column=2)
            #self.lb1.grid(row=10, column=2)
        if self.check1=='Змінити':
            self.update=self.update_info_win()

    def get_text(self, arr):
        j=10
        for i in arr:
            p=Label(text=i).grid(row=j, column=2)
            j+=1
        return p



    def button_2(self):
        self.check1 = self.check.get()
        self.enter_email=self.ent_em.get()
        self.enter_login = self.ent_log.get()
        self.enter_password = self.ent_pass.get()
        self.enter_site=self.ent_site.get()
        if self.check1=='Додати' and self.enter_email and self.enter_login and self.enter_password and self.enter_site:
            self.add = self.add_one_record(self.enter_email, self.enter_login, self.enter_password, self.enter_site)
            self.result2 = Label(text='Додано').grid(row=10, column=3)


    def choice_2(self, site):
        pass

    def choice_3(self):
        pass

    def choice_4(self):
        pass

    def choice_5(self):
        pass

    def update_info_win(self):
        '''Створенння нового вікна для зміни даних'''
        self.new_win=Tk()
        self.new_win.title('Змінити інформацію')
        self.new_win.geometry('500x300+500+300')

        self.frame_1= Frame()
        self.lb_up_1= Label(self.new_win, text='Змінити інформацію')
        self.lb_up_2= Label(self.new_win, text='Введіть сайт')
        self.lb_up_3= Label(self.frame_1, text='Вивести наявну інформацію по цьому сайту')
        self.ent_up_site = Entry(self.new_win)
        self.ent_up_new_em= Entry(self.new_win)
        self.ent_up_new_log= Entry(self.new_win)
        self.ent_up_new_pass= Entry(self.new_win)
        self.btn_up_1= Button(self.new_win, text='Змінити')
        self.btn_up_2= Button(self.new_win, text='Вивести')

        self.frame_1.grid()
        self.lb_up_1.grid(row=0, column=2)
        self.lb_up_2.grid(row=2, column=1)
        self.lb_up_3.grid(row=1, column=2)
        self.ent_up_site.grid(row=1, column=1)
        self.ent_up_new_em.grid(row=3, column=0)
        self.ent_up_new_log.grid(row=3, column=1)
        self.ent_up_new_pass.grid(row=3, column=2)
        self.btn1.grid(row=1, column=2)
        self.btn2.grid(row=2, column=2)
        self.btn3.grid(row=3, column=1)


        self.new_win.mainloop()


filenames = 'password.db'
rb = Colector(filenames)

toot = Tk()
toot.title('Збирач паролів')
toot.geometry('800x400+300+250')
toot.resizable(True, False)
colector = WindowsColector(toot, filenames)
toot.mainloop()




