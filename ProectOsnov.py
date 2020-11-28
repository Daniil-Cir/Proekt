import sqlite3
import os
import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from Dialog_Register import Ui_Dialog as Dialog_login
from Dialog_mode import Ui_Dialog as Dialog_mod

# Класс диалогового окна для админов
class Dialog_modes(QDialog, Dialog_mod):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton_admin.clicked.connect(self.Button_admin_skript)
        self.pushButton_entrance.clicked.connect(self.Button_entrance_skript)

# Открытие программы с магазином
    def Button_entrance_skript(self):
        self.close()
        os.system('python shop.py')

# Открытие программы с панелью админа
    def Button_admin_skript(self):
        self.close()
        os.system('python admin_panel_skript.py')

# Класс сартового диалогового окна
class Dialog_logins(QDialog, Dialog_login):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton_enter.clicked.connect(self.Button_enter_skript)
        self.pushButton_register.clicked.connect(self.Button_register_skript)

# функция для регистрации
    def Button_register_skript(self):
        login_input = self.lineEdit_login.text()
        pasword_input = self.lineEdit_pasword.text()
        con = sqlite3.connect("logins.db")
        cur = con.cursor()
        login_id = cur.execute(f"SELECT id FROM logins WHERE login = '{login_input}'").fetchall()
        if login_id == []:
            cur.execute(f"INSERT INTO logins (login, pasword, role_id) VALUES"
                        f"('{login_input}', '{pasword_input}', {1})")
            con.commit()
            con.close()
            self.close()
            os.system('python shop.py')

        else:
            self.label_check.setText("Логин уже занят")

    # функция для входа
    def Button_enter_skript(self):
        login_input = self.lineEdit_login.text()
        pasword_input = self.lineEdit_pasword.text()
        con = sqlite3.connect("logins.db")
        cur = con.cursor()
        login_id = cur.execute(f"SELECT id FROM logins WHERE login = '{login_input}'").fetchall()
        pasword_id = cur.execute(f"SELECT id FROM logins WHERE pasword = '{pasword_input}'").fetchall()
        login_list = []
        for i in login_id:
            login_list.append((int(i[0])))
        pasword_list = []
        for i in pasword_id:
            pasword_list.append((int(i[0])))
        if len(login_list) != 0 and len(pasword_list) != 0:
            for i in range(len(login_list)):
                for j in range(len(pasword_list)):
                    if login_list[i] == pasword_list[j]:
                        role_id = cur.execute(f"SELECT role_id FROM logins WHERE id = {login_list[i]}").fetchall()
                        role_id_int = int(role_id[0][0])
                        role = cur.execute(f"SELECT role FROM roles WHERE id = {role_id_int}").fetchall()
                        role = role[0][0]
                        # сравнивание роли пользователя
                        if role == "admin":
                            con.close()
                            self.close()
                            dialog_mode = Dialog_modes()
                            dialog_mode.show()
                            dialog_mode.exec()
                        else:
                            con.close()
                            self.close()
                            os.system('python shop.py')
        else:
            self.label_check.setText("Неверный логин или пароль")


class MyWidget():
    def __init__(self):
        super().__init__()
        self.mainwindow = self
        dialog_login = Dialog_logins()
        dialog_login.show()
        dialog_login.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()