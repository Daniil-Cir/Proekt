import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from proect_shop import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setcombobox_cofe()
        self.setcombobox_sport()
        self.setcombobox_electro()

        self.pushButton_glavnaya_top1.clicked.connect(self.like)
        self.pushButton_glavnaya_top2.clicked.connect(self.like)
        self.pushButton_glavnaya_top3.clicked.connect(self.like)

        self.pushButton_electro_like.clicked.connect(self.like1)
        self.pushButton_cofe_like.clicked.connect(self.like1)
        self.pushButton_sport_like.clicked.connect(self.like1)

        self.pushButton_electro_search.clicked.connect(self.search)
        self.pushButton_sport_search.clicked.connect(self.search)
        self.pushButton_cofe_search.clicked.connect(self.search)
        self.initUi()

    def initUi(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        pharms = self.cur_objects.execute(
            """SELECT important, name, description, photo FROM objects""").fetchall()
        pharms.sort(reverse=True)
        top1bt = pharms[0][1]
        top2bt = pharms[1][1]
        top3bt = pharms[2][1]
        top1tx = pharms[0][2]
        top2tx = pharms[1][2]
        top3tx = pharms[2][2]
        top1lb = pharms[0][3]
        top2lb = pharms[1][3]
        top3lb = pharms[2][3]
        self.top2 = QPixmap(f"photo/{top2lb}")
        # self.top2.scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label_glavnaya_top2.setPixmap(self.top2)
        self.top1 = QPixmap(f"photo/{top1lb}")
        self.label_glavnaya_top1.setPixmap(self.top1)
        self.top3 = QPixmap(f"photo/{top3lb}")
        self.label_glavnaya_top3.setPixmap(self.top3)
        self.textEdit_glavnaya_top1.setText(top1tx)
        self.textEdit_glavnaya_top2.setText(top2tx)
        self.textEdit_glavnaya_top3.setText(top3tx)

        wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (top1bt,)).fetchall()
        if wherelike[0][0] == "False":
            self.pushButton_glavnaya_top1.setText('<3')
        else:
            self.pushButton_glavnaya_top1.setText('</3')
        self.connection_objects.commit()
        wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (top2bt,)).fetchall()
        if wherelike[0][0] == "False":
            self.pushButton_glavnaya_top2.setText('<3')
        else:
            self.pushButton_glavnaya_top2.setText('</3')
        self.connection_objects.commit()
        wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (top3bt,)).fetchall()
        if wherelike[0][0] == "False":
            self.pushButton_glavnaya_top3.setText('<3')
        else:
            self.pushButton_glavnaya_top3.setText('</3')
        self.connection_objects.commit()


    def like(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        pharms = self.cur_objects.execute(
            """SELECT important, name, description, photo FROM objects""").fetchall()
        pharms.sort(reverse=True)
        top1bt = pharms[0][1]
        top2bt = pharms[1][1]
        top3bt = pharms[2][1]

        if self.sender() == self.pushButton_glavnaya_top1:
            wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (top1bt,)).fetchall()
            if wherelike[0][0] == "False":
                self.cur_objects.execute("""UPDATE objects SET important = important + 10 
                                        WHERE name = ?""", (top1bt,))
                self.cur_objects.execute("""UPDATE objects SET like = 'True' 
                                        WHERE name = ?""", (top1bt,))
                self.pushButton_glavnaya_top1.setText('</3')
            else:
                self.cur_objects.execute("""UPDATE objects SET important = important - 10 
                                                        WHERE name = ?""", (top1bt,))
                self.cur_objects.execute("""UPDATE objects SET like = 'False' 
                                                        WHERE name = ?""", (top1bt,))
                self.pushButton_glavnaya_top1.setText('<3')
            self.connection_objects.commit()
            self.connection_objects.close()

        elif self.sender() == self.pushButton_glavnaya_top2:
            wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (top2bt,)).fetchall()
            if wherelike[0][0] == "False":
                self.cur_objects.execute("""UPDATE objects SET important = important + 10 
                            WHERE name = ?""", (top2bt,))
                self.cur_objects.execute("""UPDATE objects SET like = 'True' 
                            WHERE name = ?""", (top2bt,))
                self.pushButton_glavnaya_top2.setText('</3')
            else:
                self.cur_objects.execute("""UPDATE objects SET important = important - 10 
                                            WHERE name = ?""", (top2bt,))
                self.cur_objects.execute("""UPDATE objects SET like = 'False' 
                                            WHERE name = ?""", (top2bt,))
                self.pushButton_glavnaya_top2.setText('<3')
            self.connection_objects.commit()
            self.connection_objects.close()

        elif self.sender() == self.pushButton_glavnaya_top3:
            wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (top3bt,)).fetchall()
            if wherelike[0][0] == "False":
                self.cur_objects.execute("""UPDATE objects SET important = important + 10 
                                        WHERE name = ?""", (top3bt,))
                self.cur_objects.execute("""UPDATE objects SET like = 'True' 
                                        WHERE name = ?""", (top3bt,))
                self.pushButton_glavnaya_top3.setText('</3')
            else:
                self.cur_objects.execute("""UPDATE objects SET important = important - 10 
                                                        WHERE name = ?""", (top3bt,))
                self.cur_objects.execute("""UPDATE objects SET like = 'False' 
                                                        WHERE name = ?""", (top3bt,))
                self.pushButton_glavnaya_top3.setText('<3')
            self.connection_objects.commit()
            self.connection_objects.close()
        self.initUi()

    def like1(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()

        if self.sender() == self.pushButton_electro_like:
            t = self.comboBox_electro_search.currentText()
            wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (t,)).fetchall()
            if wherelike[0][0] == "False":
                self.cur_objects.execute("""UPDATE objects SET important = important + 10 
                                                    WHERE name = ?""", (t,))
                self.cur_objects.execute("""UPDATE objects SET like = 'True' 
                                                    WHERE name = ?""", (t,))
                self.pushButton_electro_like.setText('</3')
            else:
                self.cur_objects.execute("""UPDATE objects SET important = important - 10 
                                                                    WHERE name = ?""", (t,))
                self.cur_objects.execute("""UPDATE objects SET like = 'False' 
                                                                    WHERE name = ?""", (t,))
                self.pushButton_electro_like.setText('<3')
            self.connection_objects.commit()
            self.connection_objects.close()

        elif self.sender() == self.pushButton_sport_like:
            t = self.comboBox_sport_search.currentText()
            wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (t,)).fetchall()
            if wherelike[0][0] == "False":
                self.cur_objects.execute("""UPDATE objects SET important = important + 10 
                                                                WHERE name = ?""", (t,))
                self.cur_objects.execute("""UPDATE objects SET like = 'True' 
                                                                WHERE name = ?""", (t,))
                self.pushButton_sport_like.setText('</3')
            else:
                self.cur_objects.execute("""UPDATE objects SET important = important - 10 
                                                                                WHERE name = ?""", (t,))
                self.cur_objects.execute("""UPDATE objects SET like = 'False' 
                                                                                WHERE name = ?""", (t,))
                self.pushButton_sport_like.setText('<3')
            self.connection_objects.commit()
            self.connection_objects.close()

        elif self.sender() == self.pushButton_cofe_like:
            t = self.comboBox_cofe_search.currentText()
            wherelike = self.cur_objects.execute("""SELECT like FROM objects WHERE name = ?""", (t,)).fetchall()
            if wherelike[0][0] == "False":
                self.cur_objects.execute("""UPDATE objects SET important = important + 10 
                                                                            WHERE name = ?""", (t,))
                self.cur_objects.execute("""UPDATE objects SET like = 'True' 
                                                                            WHERE name = ?""", (t,))
                self.pushButton_cofe_like.setText('</3')
            else:
                self.cur_objects.execute("""UPDATE objects SET important = important - 10 
                                                                                            WHERE name = ?""", (t,))
                self.cur_objects.execute("""UPDATE objects SET like = 'False' 
                                                                                            WHERE name = ?""", (t,))
                self.pushButton_cofe_like.setText('<3')
            self.connection_objects.commit()
            self.connection_objects.close()

    def search(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()

        if self.sender() == self.pushButton_electro_search:
            self.cur_objects.execute("""UPDATE objects SET important = important + 5 WHERE kategory_id = 
            (SELECT id FROM kategories WHERE kategory LIKE "электротехника")""")
            t = self.comboBox_electro_search.currentText()
            combo = self.cur_objects.execute("""SELECT name, description, 
            photo, price, id FROM objects WHERE name = ?""", (t,)).fetchall()
            self.lineEdit_electro_id.setText(str(combo[0][4]))
            self.lineEdit_electro_name.setText(str(combo[0][0]))
            self.textEdit_electro_description.setText(str(combo[0][1]))
            self.lineEdit_electro_price.setText(str(combo[0][3]))
            self.t = QPixmap(f"photo/{combo[0][2]}")
            self.label_electro_photo.setPixmap(self.t)
            self.connection_objects.commit()

        elif self.sender() == self.pushButton_sport_search:
            self.cur_objects.execute("""UPDATE objects SET important = important + 5 WHERE kategory_id = 
                        (SELECT id FROM kategories WHERE kategory LIKE "спорт")""")
            t = self.comboBox_sport_search.currentText()
            combo = self.cur_objects.execute("""SELECT name, description,
                        photo, price, id FROM objects WHERE name = ?""", (t,)).fetchall()
            self.lineEdit_sport_id.setText(str(combo[0][4]))
            self.lineEdit_sport_name.setText(str(combo[0][0]))
            self.textEdit_sport_description.setText(str(combo[0][1]))
            self.lineEdit_sport_price.setText(str(combo[0][3]))
            self.t = QPixmap(f"photo/{combo[0][2]}")
            self.label_sport_photo.setPixmap(self.t)
            self.connection_objects.commit()

        elif self.sender() == self.pushButton_cofe_search:
            self.cur_objects.execute("""UPDATE objects SET important = important + 5 WHERE kategory_id = 
                                    (SELECT id FROM kategories WHERE kategory LIKE "кофе")""")
            t = self.comboBox_cofe_search.currentText()
            combo = self.cur_objects.execute("""SELECT name, description,
                                    photo, price, id FROM objects WHERE name = ?""", (t,)).fetchall()
            self.lineEdit_cofe_id.setText(str(combo[0][4]))
            self.lineEdit_cofe_name.setText(str(combo[0][0]))
            self.textEdit_cofe_description.setText(str(combo[0][1]))
            self.lineEdit_cofe_price.setText(str(combo[0][3]))
            self.t = QPixmap(f"photo/{combo[0][2]}")
            self.label_cofe_photo.setPixmap(self.t)
            self.connection_objects.commit()

        self.connection_objects.close()

    def setcombobox_electro(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        r = []
        pharms = self.cur_objects.execute(
            """SELECT name FROM objects WHERE kategory_id = 
            (SELECT id FROM kategories WHERE kategory LIKE "электротехника")""").fetchall()
        for k in pharms:
            r.append(k[0])
        self.comboBox_electro_search.addItems(r)
        self.connection_objects.close()

    def setcombobox_sport(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        r = []
        pharms = self.cur_objects.execute(
            """SELECT name FROM objects WHERE kategory_id =
            (SELECT id FROM kategories WHERE kategory LIKE "спорт")""").fetchall()
        for k in pharms:
            r.append(k[0])
        self.comboBox_sport_search.addItems(r)
        self.connection_objects.close()

    def setcombobox_cofe(self):
        self.connection_objects = sqlite3.connect("shop.db")
        self.cur_objects = self.connection_objects.cursor()
        r = []
        pharms = self.cur_objects.execute(
            """SELECT name FROM objects WHERE kategory_id =
            (SELECT id FROM kategories WHERE kategory LIKE "кофе")""").fetchall()
        for k in pharms:
            r.append(k[0])
        self.comboBox_cofe_search.addItems(r)
        self.connection_objects.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())