import sqlite3
from tkinter.simpledialog import*
from tkinter.messagebox import showwarning, showinfo
import customtkinter, tkinter
from CTkTable import *

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

    def serch_info_for_col_site(self, sites):
        a=[]
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("SELECT id, email, login, password, site FROM password_colectors WHERE site=?", (sites, ))
        self.result = self.curs.fetchall()
        self.conn.commit()
        self.conn.close()
        for line in self.result:
            a.append(line)
        return a

    def serch_info_for_col_site_email(self, sites, email):
        a=[]
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("SELECT email, login, password, site FROM password_colectors WHERE email=? AND site=?", (email, sites, ))
        self.result = self.curs.fetchall()
        self.conn.commit()
        self.conn.close()
        for line in self.result:
            a.append(line)
        return a


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
        a=[]
        self.conn = sqlite3.connect(self.filename)
        self.curs = self.conn.cursor()
        self.curs.execute("SELECT * FROM password_colectors")
        self.result = self.curs.fetchall()
        self.curs.close()
        for line in self.result:
            a.append(line)
        return a

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
        self.fr1 = customtkinter.CTkFrame(root)
        self.fr2 = customtkinter.CTkFrame(root)
        self.fr4 = customtkinter.CTkFrame(root)
        self.fr5 = customtkinter.CTkFrame(root)
        #self.font1 = CTkFont(family="Roman", size=9, weight="normal", slant="roman", underline=False, overstrike=False)

        self.lb1 = customtkinter.CTkLabel(self.fr1, text='Ознайомитись з поточною інформацією:')
        self.lb2 = customtkinter.CTkLabel(self.fr1, text='Введіть назву сайту:')
        self.lb9 = customtkinter.CTkLabel(self.fr4, text='Результат пошуку:')
        self.var1 = IntVar()
        self.chek1 = customtkinter.CTkCheckBox(self.fr1, text='Переглянути інформацію', variable=self.var1)
        self.ent = customtkinter.CTkEntry(self.fr1)
        self.var2 = StringVar(value=0)
        self.lb8 = customtkinter.CTkLabel(self.fr2, text='Виберіть дію:')
        self.rad1=customtkinter.CTkRadioButton(self.fr2, text='Змінити', variable=self.var2, value=1)
        self.rad2=customtkinter.CTkRadioButton(self.fr2, text='Додати', variable=self.var2, value=2)
        self.rad3=customtkinter.CTkRadioButton(self.fr2, text='Видалити', variable=self.var2, value=3)
        self.btn1 = customtkinter.CTkButton(self.fr1, text='Виконати', command=self.button_1)
        self.btn2 = customtkinter.CTkButton(root, text='Про програму', command=self.info_about_program)
        self.btn3 = customtkinter.CTkButton(self.fr2, text='Вибрати', command=self.button_2)
        self.btn4 = customtkinter.CTkButton(root, text='Очистити інформацію')
        self.fr2.grid(row=4, column=1, columnspan=4, sticky=EW, padx=5, pady=5)
        self.fr4.grid(row=5, column=0, columnspan=4, sticky=EW, padx=5, pady=5)
        self.fr1.grid(row=1, column=1)
        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=2, column=0)
        self.chek1.grid(row=1, column=1)
        self.ent.grid(row=2, column=1)
        self.btn1.grid(row=3, column=0)
        self.btn2.grid(row=0, column=0, ipadx=2, ipady=2, padx=2, pady=4)
        self.btn3.grid(row=2, column=5, ipadx=6, ipady=2, padx=4, pady=4, sticky=NSEW)
        self.btn4.grid(row=1, column=0)
        self.lb8.grid(row=0, column=3)
        self.lb9.pack()
        self.rad1.grid(row=2, column=1)
        self.rad2.grid(row=2, column=2)
        self.rad3.grid(row=2, column=3)

    def button_1(self):
        self.cerch = self.create_table_colector()
        self.ent_site_text_1 = self.ent.get()
        self.var_1=self.var1.get()
        if self.var_1==1 and self.ent_site_text_1:
            self.v = self.serch_info_for_col_site(self.ent_site_text_1)
            self.res_table_one=self.result_text(self.v)
        elif self.var1.get()==1 and not self.ent_site_text_1:
            self.all_info=self.return_info_in_base()
            self.table = self.result_text(self.all_info)


    def result_text(self, arr=None):
        self.table = CTkTable(master=self.fr4, row=len(arr), column=5, values=arr)
        self.table.pack(expand=True, fill="both", padx=20, pady=20)

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
        self.win_add=customtkinter.CTk()
        self.win_add.title('Додати інформацію')
        self.win_add.geometry('350x300+350+200')
        self.win_add.resizable(False, False)

        self.lb_1 = customtkinter.CTkLabel(self.win_add, text='Додати інформацію:')
        self.lb_2 = customtkinter.CTkLabel(self.win_add, text='Заповніть інформацію в полях')
        self.lb_site = customtkinter.CTkLabel(self.win_add, text='Сайт:')
        self.lb_email = customtkinter.CTkLabel(self.win_add, text='Електрона пошта:')
        self.lb_login = customtkinter.CTkLabel(self.win_add, text='Логін:')
        self.lb_password = customtkinter.CTkLabel(self.win_add, text='Пароль:')
        self.ent_site_add = customtkinter.CTkEntry(self.win_add)
        self.ent_email_add = customtkinter.CTkEntry(self.win_add)
        self.ent_login_add = customtkinter.CTkEntry(self.win_add)
        self.ent_site_add = customtkinter.CTkEntry(self.win_add)
        self.ent_pass_add = customtkinter.CTkEntry(self.win_add)
        self.fr_add = customtkinter.CTkFrame(self.win_add)

        self.btn_add = customtkinter.CTkButton(self.win_add, text='Зберегти', command=self.choice_2)

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
        self.new_win = customtkinter.CTk()
        self.new_win.title('Видалити інформацію')
        self.new_win.geometry('700x300+350+200')
        self.new_win.resizable(True, False)
        self.fr_del = customtkinter.CTkFrame(self.new_win)
        self.d_lb1 = customtkinter.CTkLabel(self.new_win, text='Видалення даних')
        self.d_lb2 = customtkinter.CTkLabel(self.new_win, text='Введіть сайт:')
        self.d_lb3 = customtkinter.CTkLabel(self.new_win, text='Введіть пошту:')
        self.d_lb4 = customtkinter.CTkLabel(self.fr_del, text='Попередній огляд інформації')
        self.btn_del_1 = customtkinter.CTkButton(self.new_win, text='Застосувати', command=self.return_info_del)
        self.btn_del_2 = customtkinter.CTkButton(self.new_win, text='Видалити інформацію', command=self.return_delet)
        self.del_ent1 = customtkinter.CTkEntry(self.new_win)
        self.del_ent2 = customtkinter.CTkEntry(self.new_win)
        self.fr_del.grid(row=5, column=1, columnspan=2, sticky=EW, padx=5, pady=5)
        self.d_lb1.grid(row=0, column=1)
        self.d_lb2.grid(row=1, column=0)
        self.d_lb3.grid(row=2, column=0)
        self.d_lb4.pack()
        self.del_ent1.grid(row=1, column=1)
        self.del_ent2.grid(row=2, column=1)
        self.btn_del_1.grid(row=3, column=1, ipadx=4, ipady=2, padx=2, pady=2, sticky=NSEW)
        self.btn_del_2.grid(row=4, column=1, ipadx=4, ipady=2, padx=2, pady=2, sticky=NSEW)

        self.new_win.mainloop()


    def return_info_del(self):
        self.email_serch_del=self.del_ent2.get()
        self.site_serch_del=self.del_ent1.get()
        if self.email_serch_del and self.site_serch_del:
            self.res_info = self.serch_info_for_col_site_email(self.site_serch_del, self.email_serch_del)
            self.table2 = CTkTable(master=self.fr_del, row=len(self.res_info), column=4, values=self.res_info)
            self.table2.pack(expand=True, fill="both", padx=1, pady=1)

    def return_delet(self):
        self.email_del = self.del_ent2.get()
        self.site_del = self.del_ent1.get()
        if self.email_del and self.site_del:
            self.dele_in_base = self.delete_info_in_base(self.email_del, self.site_del)
            self.del_message = customtkinter.CTkLabel(self.fr_del, text=self.dele_in_base).grid(row=2, column=0)


    def new_win_update(self):
        self.win = customtkinter.CTk()
        self.win.title('Змінити інформацію')
        self.win.geometry('350x300+350+200')
        self.win.resizable(False, False)
        self.fr_upd = customtkinter.CTkFrame(self.win)
        self.n_lb1 = customtkinter.CTkLabel(self.win, text='Змінити інформацію')
        self.n_lb2 = customtkinter.CTkLabel(self.win, text='Введіть наступну інформацію:')
        self.n_lb3 = customtkinter.CTkLabel(self.win, text='Сайт:')
        self.n_lb4 = customtkinter.CTkLabel(self.win, text='Електронну адресу:')
        self.n_lb5 = customtkinter.CTkLabel(self.win, text='Ввід нової інформації')
        self.n_lb6 = customtkinter.CTkLabel(self.win, text='Введіть інформацію:')
        self.n_lb7 = customtkinter.CTkLabel(self.win, text='Виберіть, що зміити:')
        self.info_act = ['Логін', 'Пароль']
        self.var_4 = IntVar(value=self.info_act[0])
        self.n_com = customtkinter.CTkComboBox(self.win, values=self.info_act, variable=self.var_4)
        self.ent_1_site = customtkinter.CTkEntry(self.win)
        self.ent_2_email = customtkinter.CTkEntry(self.win)
        self.ent_3 = customtkinter.CTkEntry(self.win)
        self.win_btn1 = customtkinter.CTkButton(self.win, text='Змінити', command=self.update_info)
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
        self.win_info=customtkinter.CTk()
        self.win_info.geometry('600x200+350+200')
        self.win_info.title('Інформація про програму')

        self.info_lbq_0 = customtkinter.CTkLabel(self.win_info, text='Збирач паролів')
        self.info_lbq_1 = customtkinter.CTkLabel(self.win_info, text='Дана програма збирає ваші дані в локальну базу даних, яка є окремим файлом.')
        self.info_lbq_2 = customtkinter.CTkLabel(self.win_info, text='Видаливши файл "password_colector.db" ви втратите файл разом зі збереженими даними.')

        self.info_lbq_0.grid(row=0, column=0)
        self.info_lbq_1.grid(row=1, column=0)
        self.info_lbq_2.grid(row=3, column=0)

        self.win_info.mainloop()



filenames = 'password_colector.db'
rb = Colector(filenames)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
toot = customtkinter.CTk()
toot.title('Збирач паролів')
toot.geometry('800x500+350+200')
toot.resizable(False, True)
colector = WindowsColector(toot, filenames)

toot.mainloop()




