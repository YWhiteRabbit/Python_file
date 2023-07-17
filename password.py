import sqlite3
from tkinter.simpledialog import*
import tkinter.ttk as tkk
from tkinter.messagebox import showwarning, showinfo
from tkinter import font


class Colector:
    def __init__(self, filename):
        self.filename = filename

    def create_table_colector(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute('''CREATE TABLE if not exists password_colectors(id  INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    email text NULL, 
                                                                    login text NULL,
                                                                    password text NULL,
                                                                    site text NULL)''')
        conn.commit()
        conn.close()

    def add_one_record(self, email, login, password, site):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("INSERT INTO password_colectors VALUES(NULL,?,?,?,?)", (email, login, password, site))
        conn.commit()
        conn.close()
        return 'Додано'

    def add_persons(self, k):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        for i in range(k):
            email = input('enter email:')
            login = input('enter login:')
            password = input('enter password:')
            site = input('enter the site where register:')
            curs.execute("INSERT INTO password_colectors VALUE(NULL,?,?,?,?)", (email, login, password, site))
        conn.commit()
        conn.close()

    def serch_info_for_col_site(self, sites):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT email, login, password, site FROM password_colectors WHERE site=?", (sites, ))
        result = curs.fetchall()
        conn.commit()
        conn.close()
        return result

    def serch_info_for_col_site_email(self, sites, email):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("SELECT email, login, password, site FROM password_colectors WHERE email=? AND site=?", (email, sites, ))
        result = curs.fetchall()
        conn.commit()
        conn.close()
        return result


    def update_all_info(self, old_email, new_email, new_login, new_password ):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        curs.execute("UPDATE password_colectors SET email ='new_email',"
                     " login='new_login',"
                     "password='new_password'"
                     " WHERE email = 'old_email' ")
        conn.commit()
        conn.close()

    def update_info_password(self, email_info,  new_password, site_info):
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("UPDATE password_colectors SET password=? WHERE email=? AND site=?", (new_password, email_info, site_info))
        self.conn.commit()
        self.conn.close()
        print('password')

    def update_info_login(self, email_info, new_login, site_info):
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("UPDATE password_colectors SET login=? WHERE email=? AND site=?", (new_login, email_info, site_info))
        self.conn.commit()
        self.conn.close()
        print('login')

    def return_info_in_base(self):
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("SELECT * FROM password_colectors")
        self.result = self.curs.fetchall()
        self.curs.close()
        return self.result

    def delete_info_in_base(self, email_del, site_del):
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("DELETE FROM password_colectors WHERE email=? AND site=?", (self.email_del, self.site_del, ))
        self.conn.commit()
        self.conn.close()
        return 'Інформацію видалено'

class WindowsColector(Colector):
    def __init__(self, root, filename):
        ''' combobox-ибираємо дію, label-текст, що програма робить,

        button-запускаємо програму, entry-вводимо іноформацію
        додаткове поде для введення нової інформації '''
        self.filename = filename
        self.fr1 = Frame(root, borderwidth=0, height=50, width=20, relief=SOLID)
        self.fr2 = Frame(root, borderwidth=1, height=50, width=20, relief=SOLID)
        self.fr4 = Frame(root, borderwidth=1, height=50, width=20, relief=GROOVE)
        self.fr5 = Frame(root, borderwidth=1, height=50, width=20, relief=GROOVE)
        self.font1 = font.Font(family="Roman", size=9, weight="normal", slant="roman", underline=False, overstrike=False)

        self.lb1 = Label(self.fr1, text='Ознайомитись з поточною інформацією:', font=self.font1)
        self.lb2 = Label(self.fr1, text='Введіть назву сайту', font=self.font1)
        self.lb9 = Label(self.fr4, text='Результат пошуку:', font=self.font1)
        self.var1 = IntVar()
        self.chek1 = Checkbutton(self.fr1, text='Переглянути інформацію', font=self.font1, variable=self.var1)
        self.ent = Entry(self.fr1)
        self.var2 = StringVar(value=0)
        self.lb8 = Label(self.fr2, text='Виберіть дію:', font=self.font1)
        self.rad1 = Radiobutton(self.fr2, text='Змінити', font=self.font1, variable=self.var2, value=1)
        self.rad2 = Radiobutton(self.fr2, text='Додати', font=self.font1, variable=self.var2, value=2)
        self.rad3 = Radiobutton(self.fr2, text='Видалити', font=self.font1, variable=self.var2, value=3)
        self.btn1 = Button(self.fr1, text='Виконати', font=self.font1, command=self.button_1)
        self.btn2 = Button(root, text='Про програму', font=self.font1, command=self.info_about_program)
        self.btn3 = Button(self.fr2, text='Вибрати', font=self.font1, command=self.button_2)
        self.fr1.grid(row=1, column=1)
        self.fr2.grid(row=3, column=1)
        self.fr4.grid(row=4, column=1, columnspan=4, sticky=EW, padx=5, pady=5)
        self.btn1.config(command=self.button_1)
        self.chek1.grid(row=2, column=3)
        self.lb1.grid(row=1, column=3)
        self.lb2.grid(row=1, column=4)
        self.ent.grid(row=2, column=4)
        self.btn1.grid(row=4, column=4)
        self.btn2.grid(row=0, column=0, ipadx=6, ipady=2, padx=4, pady=4, sticky=NSEW)
        self.btn3.grid(row=3, column=5, ipadx=6, ipady=2, padx=4, pady=4, sticky=NSEW)
        self.lb8.grid(row=0, column=3)
        self.lb9.grid(row=0, column=1)
        self.rad1.grid(row=2, column=1)
        self.rad2.grid(row=2, column=2)
        self.rad3.grid(row=2, column=3)

    def button_1(self):
        self.ent_site_text_1 = self.ent.get()
        self.var_1=self.var1.get()
        if self.ent_site_text_1 and self.var1==1:
            self.cerch = self.create_table_colector()
            self.v = self.serch_info_for_col_site(self.ent_site_text_1)
            self.result_text(self.v, self.fr4)
        elif self.var1.get()==1 and not self.ent_site_text_1:
            self.all_info=self.return_info_in_base()
            self.result_text(self.all_info, self.fr4)

    def result_text(self, arr=None, fram=None):
        j = 1
        for i in arr:
            self.strings = Label(fram, text=i).grid(row=j, column=2)
            j += 1
        return self.strings


    def open_warning(self):
        self.w=showwarning(title='Відсутня інформація', message='Даної інформації немає в системі.')

    def open_info(self):
        self.w=showinfo(title='Відсутність даних', message='Перевірте, що ввели інформацію.')

    def button_2(self):
        '''зберегти зміни інформації'''
        self.value=self.var2.get()
        if self.value=='1':
            self.new_win_update()
        if self.value=='2':
            self.new_win_add_info()
        if self.value=='3':
            self.new_win_delete()


    def new_win_add_info(self):
        self.win_add=Tk()
        self.win_add.title('Додати інформацію')
        self.win_add.geometry('350x300')
        self.win_add.resizable(False, False)

        self.lb_1 = Label(self.win_add, text='Додати інформацію:')
        self.lb_2 = Label(self.win_add, text='Заповніть інформацію в полях')
        self.lb_site = Label(self.win_add, text='Сайт:')
        self.lb_email = Label(self.win_add, text='Електрона пошта:')
        self.lb_login = Label(self.win_add, text='Логін:')
        self.lb_password = Label(self.win_add, text='Пароль:')
        self.ent_site_add = Entry(self.win_add)
        self.ent_email_add = Entry(self.win_add)
        self.ent_login_add = Entry(self.win_add)
        self.ent_site_add = Entry(self.win_add)
        self.ent_pass_add = Entry(self.win_add)
        self.fr_add = Frame(self.win_add)

        self.btn_add = Button(self.win_add, text='Зберегти', command=self.choice_2)

        self.lb_1.grid(row=0, column=1)
        self.lb_2.grid(row=1, column=1)
        self.lb_site.grid(row=2, column=0)
        self.lb_email.grid(row=3, column=0)
        self.lb_login.grid(row=4, column=0)
        self.lb_password.grid(row=5, column=0)
        self.ent_site_add.grid(row=2, column=1)
        self.ent_email_add.grid(row=3, column=1)
        self.ent_login_add.grid(row=4, column=1)
        self.ent_pass_add.grid(row=5, column=1)
        self.btn_add.grid(row=6, column=1)
        self.fr_add.grid(row=7, column=1)


        self.win_add.mainloop()

    def choice_2(self):
        '''додати нову інформацію'''
        self.email=self.ent_em.get()
        self.login=self.ent_log.get()
        self.password=self.ent_pass.get()
        self.site=self.ent_site.get()
        if self.email and self.login and self.password and self.site:
            self.res1=self.add_one_record(self.email, self.login, self.password, self.site)
        else:
            self.open_info()

    def new_win_delete(self):
        self.new_win=Tk()
        self.new_win.title('Видалити інформацію')
        self.new_win.geometry('350x300')
        self.new_win.resizable(False, False)
        self.fr_del = Frame(self.new_win, borderwidth=1, height=35, width=25, relief=GROOVE)
        self.d_lb1 = Label(self.new_win, text='Видалення даних')
        self.d_lb2 = Label(self.new_win, text='Введіть сайт:')
        self.d_lb3 = Label(self.new_win, text='Введіть пошту:')
        self.d_lb4 = Label(self.fr_del, text='Попередній огляд інформації')
        self.btn_del_1 = Button(self.new_win, text='Застосувати', command=self.return_info_del)
        self.btn_del_2 = Button(self.new_win, text='Видалити інформацію', command=self.return_delet)
        self.del_ent1 = Entry(self.new_win)
        self.del_ent2 = Entry(self.new_win)
        self.fr_del.grid(row=3, column=1, columnspan=2, sticky=EW, padx=5, pady=5)
        self.d_lb1.grid(row=0, column=1)
        self.d_lb2.grid(row=1, column=0)
        self.d_lb3.grid(row=2, column=0)
        self.d_lb4.grid(row=0, column=1)
        self.del_ent1.grid(row=1, column=1)
        self.del_ent2.grid(row=2, column=1)
        self.btn_del_1.grid(row=4, column=1, ipadx=4, ipady=2, padx=2, pady=2, sticky=NSEW)
        self.btn_del_2.grid(row=5, column=1, ipadx=4, ipady=2, padx=2, pady=2, sticky=NSEW)

        self.new_win.mainloop()


    def return_info_del(self):
        self.email_serch_del=self.del_ent2.get()
        self.site_serch_del=self.del_ent1.get()
        if self.email_serch_del and self.site_serch_del:
            self.res_info = self.serch_info_for_col_site_email(self.site_serch_del, self.email_serch_del)
            self.res = Label(self.fr_del, text=self.res_info).grid(row=1, column=0)


    def return_delet(self):
        self.email_del = self.del_ent2.get()
        self.site_del = self.del_ent1.get()
        if self.email_del and self.site_del:
            self.dele_in_base = self.delete_info_in_base(self.email_del, self.site_del)
            self.del_message = Label(self.fr_del, text=self.dele_in_base).grid(row=2, column=0)


    def new_win_update(self, ttk=None):
        self.win = Tk()
        self.win.title('Змінити інформацію')
        self.win.geometry('350x300')
        self.win.resizable(False, False)
        self.fr_upd = Frame(self.win, borderwidth=1, height=35, width=25, relief=GROOVE)
        self.n_lb1 = Label(self.win, text='Змінити інформацію')
        self.n_lb2 = Label(self.win, text='Введіть наступну інформацію:')
        self.n_lb3 = Label(self.win, text='Сайт:')
        self.n_lb4 = Label(self.win, text='Електронну адресу:')
        self.n_lb5 = Label(self.win, text='Ввід нової інформації')
        self.n_lb6 = Label(self.win, text='Введіть інформацію:')
        self.n_lb7 = Label(self.win, text='Виберіть, що зміити:')
        self.info_act = ['Логін', 'Пароль']
        self.var_4 = IntVar(value=self.info_act[0])
        self.n_com = tkk.Combobox(self.win, textvariable=self.var_4, values=self.info_act, height=len(self.info_act))
        self.ent_1_site = Entry(self.win)
        self.ent_2_email = Entry(self.win)
        self.ent_3 = Entry(self.win)
        self.win_btn1 = Button(self.win, text='Змінити', command=self.update_info)
        self.n_lb1.grid(row=0, column=1)
        self.n_lb2.grid(row=1, column=1)
        self.n_lb3.grid(row=2, column=0)
        self.n_lb4.grid(row=3, column=0)
        self.n_lb5.grid(row=4, column=1)
        self.n_lb6.grid(row=6, column=0)
        self.n_lb7.grid(row=5, column=0)
        self.n_com.grid(row=5, column=1)
        self.ent_1_site.grid(row=2, column=1)
        self.ent_2_email.grid(row=3, column=1)
        self.ent_3.grid(row=6, column=1)
        self.win_btn1.grid(row=7, column=1, ipadx=6, ipady=2, padx=4, pady=4, sticky=NSEW)
        self.fr_upd.grid(row=8, column=1)
        #self.n_lb.grid(row=, column=)

        self.win.mainloop()

    def update_info(self):
        self.act_com = self.n_com.get()
        self.site_return_update = self.ent_1_site.get()
        self.old_email_return_update = self.ent_2_email.get()
        self.info_upd = self.ent_3.get()
        print(self.act_com)
        if self.act_com=='Логін' and self.site_return_update and self.info_upd:
            self.update_info_login(self.old_email_return_update, self.info_upd, self.site_return_update)
        if self.act_com=='Пароль' and self.info_upd and self.old_email_return_update:
            self.update_info_password(self.old_email_return_update, self.info_upd, self.site_return_update)

    def info_about_program(self):
        self.win_info=Tk()
        self.win_info.geometry('550x300')
        self.win_info.title('Інформація про програму')

        self.info_lbq_0 = Label(self.win_info, text='Збирач паролів')
        self.info_lbq_1 = Label(self.win_info, text='Дана програма збирає ваші дані в локальну базу даних, яка є окремим файлом.')
        self.info_lbq_2 = Label(self.win_info, text='Видаливши цей файл "password_colector.db" ви втратите файл разом зі збереженими даними.')

        self.info_lbq_0.grid(row=0, column=0)
        self.info_lbq_1.grid(row=1, column=0)
        self.info_lbq_2.grid(row=3, column=0)

        self.win_info.mainloop()



filenames = 'password_colector.db'
rb = Colector(filenames)
toot = Tk()
toot.title('Збирач паролів')
toot.geometry('700x350')
toot.resizable(False, False)
colector = WindowsColector(toot, filenames)

toot.mainloop()

