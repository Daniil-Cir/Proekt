import sqlite3
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from admin_panel import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection_logins = sqlite3.connect("logins.db")
        self.cur_logins = self.connection_logins.cursor()
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        self.setcombobox_sale_number()
        self.setcombobox_adminpanel_add_kategory()
        self.pushButton_adminpanel_add.clicked.connect(self.add_admin)
        self.pushButton_adminpanel_add_object.clicked.connect(self.add_object)
        self.pushButton_sale.clicked.connect(self.make_sale)

# функция для добавления администратора
    def add_admin(self):
        self.label_adminpanel_check.setText("")
        login_input = self.lineEdit_adminpanel_login.text()
        pasword_input = self.lineEdit_adminpanel_pasword.text()
        self.connection_logins = sqlite3.connect("logins.db")
        self.cur_logins = self.connection_logins.cursor()
        login_id = self.cur_logins.execute(f"SELECT id FROM logins WHERE login = '{login_input}'").fetchall()
        if login_id == []:
            self.cur_logins.execute(f"INSERT INTO logins (login, pasword, role_id) VALUES"
                                    f"('{login_input}', '{pasword_input}', {2})")
            self.connection_logins.commit()
            self.connection_logins.close()
            self.label_adminpanel_check.setText("Новый администратор добавлен")
        else:
            self.label_adminpanel_check.setText("Логин уже занят")

    # функция для добавления товара
    def add_object(self):
        self.label_add_objects_itog.setText("")
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        object_photo_name = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')
        object_name = self.lineEdit_adminpanel_add_name.text()
        object_description = self.textEdit_adminpanel_add_description.toPlainText()
        object_price = self.lineEdit_adminpanel_add_price.text()
        object_kategory = self.comboBox_adminpanel_add_kategory.currentText()
        object_kategory = self.cur_objects.execute(f"SELECT id FROM kategories WHERE kategory ="
                                                   f"'{object_kategory}'").fetchall()
        object_kategory = object_kategory[0][0]
        if object_name != '' and object_description != '' and object_price != '' and object_price.isdigit():
            object_price = int(object_price)
            object_kategory = int(object_kategory)
            t = str(object_photo_name[0]).split('/')
            self.cur_objects.execute(f"INSERT INTO objects (name, description, price, kategory_id, photo, important)"
                                     f"VALUES ('{object_name}', '{object_description}', {object_price},"
                                     f"{object_kategory}, '{str(t[len(t) - 1])}', {0})")
            self.label_add_objects_itog.setText("Объект успешно добавлен, добавьте фото объекта в папку фото")
            self.connection_objects.commit()
            self.connection_objects.close()
            self.setcombobox_sale_number()
        else:
            self.label_add_objects_itog.setText("Неверный ввод")

    def setcombobox_sale_number(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        dannye_list = []
        dannye = self.cur_objects.execute("""SELECT id FROM objects""").fetchall()
        for k in dannye:
            dannye_list.append(str(k[0]))
        del dannye_list[0]
        self.comboBox_sale_number.clear()
        self.comboBox_sale_number.addItems(dannye_list)
        self.connection_objects.close()

    def setcombobox_adminpanel_add_kategory(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        dannye_list = []
        dannye = self.cur_objects.execute("""SELECT kategory FROM kategories """).fetchall()
        for object_k in dannye:
            dannye_list.append(object_k[0])
        self.comboBox_adminpanel_add_kategory.clear()
        self.comboBox_adminpanel_add_kategory.addItems(dannye_list)
        self.connection_objects.close()

    # функция для создания скидок
    def make_sale(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        objects = self.cur_objects.execute("""SELECT id FROM objects ORDER BY important""").fetchall()
        object_list = []

        for k in range(int(self.comboBox_sale_number.currentText())):
            object_list.append(objects[k][0])
        object_list = (tuple(object_list))
        self.cur_objects.execute(f"UPDATE objects SET price = price - (price * 30 / 100)"
                                 f"WHERE id IN {object_list}").fetchall()
        self.connection_objects.commit()
        self.connection_objects.close()
        self.label_add_sale_itog.setText("Скидки успешно созданы")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())