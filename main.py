import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from modau import Ui_MoDau
from thongtinnguoidung import Ui_ThongTinNguoiDung
from lenkehoach import Ui_LenKeHoach
from khamphamon import Ui_Form
from chucnang import Ui_ChucNang
from lichsu import Ui_LichSu
import pandas as pd
import itertools
import datetime
from babel.dates import format_date, format_datetime
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MoDau()
        self.uic.setupUi(self)
        self.main_win_2 = QWidget()
        self.uic2 = Ui_ThongTinNguoiDung()
        self.uic2.setupUi(self.main_win_2)
        self.main_win_3 = QWidget()
        self.uic3 = Ui_LenKeHoach()
        self.uic3.setupUi(self.main_win_3)
        self.main_win_4 = QWidget()
        self.uic4 = Ui_ChucNang()
        self.uic4.setupUi(self.main_win_4)
        self.main_win_5 = QWidget()
        self.uic5 = Ui_Form()
        self.uic5.setupUi(self.main_win_5)
        self.main_win_6 = QWidget()
        self.uic6 = Ui_LichSu()
        self.uic6.setupUi(self.main_win_6)
        self.uic.btnNext.clicked.connect(lambda: self.next())
        self.uic2.btnNext.clicked.connect(lambda: self.nextThongTinNguoiDung())
        self.uic3.btnLenKeHoach.clicked.connect(lambda: self.handleLenKeHoach())
        self.uic4.btnThongTinNguoiDung.clicked.connect(lambda: self.showThongTinNguoiDung())
        self.uic4.btnKhamPhaMon.clicked.connect(lambda: self.khamPhaMon())
        self.initTable()
        self.uic5.pushButton.clicked.connect(lambda: self.khamPhaMonChucNang())
        self.uic4.btnLenKeHoach.clicked.connect(lambda: self.showLenKeHoach())
        self.uic3.btnNext.clicked.connect(lambda: self.nextLenKeHoach())
        self.uic5.tableWidget.itemClicked.connect(self.handleCellClicked)
        self.uic4.btnLichSu.clicked.connect(lambda: self.showLichSu())
        self.uic6.pushButton.clicked.connect(lambda: self.nextLichSu())
        self.loadLichSu()
        self.calbmr()
        self.uic2.spinBoxTuoi.valueChanged.connect(lambda: self.calbmr())
        self.uic2.spinBoxChieuCao.valueChanged.connect(lambda: self.calbmr())
        self.uic2.spinBoxCanNang.valueChanged.connect(lambda: self.calbmr())
        self.uic2.comboBoxGioiTinh.currentIndexChanged.connect(lambda: self.calbmr())
        self.uic6.btnXoaLichSu.clicked.connect(lambda: self.xoaLichSu())
        self.uic6.tableWidget.cellClicked.connect(lambda: self.handleCellClickedLichSu())
    def handleCellClickedLichSu(self):
        row = self.uic6.tableWidget.currentRow()
        column = self.uic6.tableWidget.currentColumn()
        monan = self.uic6.tableWidget.item(row, column).text()
        print(monan)
        url = ""
        for i in range(self.uic5.tableWidget.rowCount()):
            if monan == self.uic5.tableWidget.item(i, 1).text():
                url = self.uic5.tableWidget.item(i, 7).text()
        QDesktopServices.openUrl(QUrl(url))
        print(url)
    def xoaLichSu(self):
        # Clear the content of the "lichsu.txt" file
        with open("lichsu.txt", "w", encoding="utf-8") as file:
            file.write("")

        # Optionally, you can also clear the content of the table widget
        self.uic6.tableWidget.clearContents()
        self.uic6.tableWidget.setRowCount(0)
    def nextThongTinNguoiDung(self):
        self.main_win_2.close()
        self.main_win_4.show()
    def loadLichSu(self):
        with open("lichsu.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        self.uic6.tableWidget.setRowCount(len(lines))
        for row, line in enumerate(lines):
            data = line.strip()
            lst = data.split(";")
            for i in range(len(lst)):
                self.uic6.tableWidget.setItem(row, i, QTableWidgetItem(lst[i]))

    def showLichSu(self):
        self.main_win_4.close()
        self.main_win_6.show()
    def nextLichSu(self):
        self.main_win_6.close()
        self.main_win_4.show()
    def nextLenKeHoach(self):
        self.main_win_4.show()
        self.main_win_3.close()
    def showLenKeHoach(self):
        self.main_win_4.close()
        self.main_win_3.show()
    def khamPhaMonChucNang(self):
        self.main_win_4.show()
        self.main_win_5.close()
    def initTable(self):
        df = pd.read_excel('monan.xlsx', usecols=range(8))
        self.uic5.tableWidget.setRowCount(df.shape[0])
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.uic5.tableWidget.setItem(i, j, item)
    def handleCellClicked(self):
            url = self.uic5.tableWidget.item(self.uic5.tableWidget.currentRow(), 7).text()
            QDesktopServices.openUrl(QUrl(url))
    def khamPhaMon(self):
        self.main_win_5.show()
        self.main_win_4.close()
    def showThongTinNguoiDung(self):
        self.main_win_4.close()
        self.main_win_2.show()
    def handleLenKeHoach(self):
        self.uic3.txtThucDon.clear()
        df = pd.read_excel('monan.xlsx', usecols=range(8))
        data_list = df.values.tolist()
        lstDam = []
        if self.uic3.checkBoxThitHeo.isChecked():
            lstDam.append(self.uic3.checkBoxThitHeo.text())
        if self.uic3.checkBoxThitBo.isChecked():
            lstDam.append(self.uic3.checkBoxThitBo.text())
        if self.uic3.checkBoxThitGaVit.isChecked():
            lstDam.append(self.uic3.checkBoxThitGaVit.text())
        if self.uic3.checkBoxCa.isChecked():
            lstDam.append(self.uic3.checkBoxCa.text())
        if self.uic3.checkBoxTrung.isChecked():
            lstDam.append(self.uic3.checkBoxTrung.text())
        if self.uic3.checkBoxHaiSanTomMuc.isChecked():
            lstDam.append(self.uic3.checkBoxHaiSanTomMuc.text())
        if self.uic3.checkBoxDamThucVatTauHuSuonChay.isChecked():
            lstDam.append(self.uic3.checkBoxDamThucVatTauHuSuonChay.text())
        lstTinhBot = []
        if self.uic3.checkBoxComXoi.isChecked():
            lstTinhBot.append(self.uic3.checkBoxComXoi.text())
        if self.uic3.checkBoxBunHuTieuMien.isChecked():
            lstTinhBot.append(self.uic3.checkBoxBunHuTieuMien.text())
        if self.uic3.checkBoxBanhMi.isChecked():
            lstTinhBot.append(self.uic3.checkBoxBanhMi.text())
        if self.uic3.checkBoxMi.isChecked():
            lstTinhBot.append(self.uic3.checkBoxMi.text())
        if self.uic3.checkBoxChao.isChecked():
            lstTinhBot.append(self.uic3.checkBoxChao.text())
        if self.uic3.checkBoxNui.isChecked():
            lstTinhBot.append(self.uic3.checkBoxNui.text())
        if self.uic3.checkBoxBanhPho.isChecked():
            lstTinhBot.append(self.uic3.checkBoxBanhPho.text())
        lstChatXo = []
        if self.uic3.checkBoxDuaLeoCaChua.isChecked():
            lstChatXo.append(self.uic3.checkBoxDuaLeoCaChua.text())
        if self.uic3.checkBoxCaRotKhoaiTay.isChecked():
            lstChatXo.append(self.uic3.checkBoxCaRotKhoaiTay.text())
        if self.uic3.checkBoxRauCai.isChecked():
            lstChatXo.append(self.uic3.checkBoxRauCai.text())
        if self.uic3.checkBoxDau.isChecked():
            lstChatXo.append(self.uic3.checkBoxDau.text())
        if self.uic3.checkBoxHanhTay.isChecked():
            lstChatXo.append(self.uic3.checkBoxHanhTay.text())
        if self.uic3.checkBoxBi.isChecked():
            lstChatXo.append(self.uic3.checkBoxBi.text())
        if self.uic3.checkBoxNam.isChecked():
            lstChatXo.append(self.uic3.checkBoxNam.text())
        if self.uic3.checkBoxKhomDuaThom.isChecked():
            lstChatXo.append(self.uic3.checkBoxKhomDuaThom.text())
        lstDam.append("x")
        lstTinhBot.append("x")
        lstChatXo.append("x")
        lstThucDon = []
        lstThoiGianCheBien = []
        if self.uic3.radioNhoHon15p.isChecked():
            lstThoiGianCheBien = ["<15p"]
        elif self.uic3.radioNhoHon30p.isChecked():
            lstThoiGianCheBien = ["<15p", "<30p"]
        elif self.uic3.radioNhoHon45p.isChecked():
            lstThoiGianCheBien = ["<15p", "<30p","<45p"]
        elif self.uic3.radioLonHon45p.isChecked():
            lstThoiGianCheBien = [">45p"]
        for i in data_list:
            if i[2] in lstDam and i[3] in lstTinhBot and i[4] in lstChatXo and i[5] in lstThoiGianCheBien:
                lstThucDon.append(i)
        print(self.bmr)
        if self.bmr < 1600:
            breakfast_meal = None
            lunch_meal = None
            dinner_meal = None
            total_calories = float('inf')
            closest_difference = float('inf')
            for combination in itertools.combinations(lstThucDon, 3):
                current_calories = sum(meal[6] for meal in combination)
                current_difference = abs(current_calories - self.bmr)
                if current_difference < closest_difference:
                    closest_difference = current_difference
                    breakfast_meal, lunch_meal, dinner_meal = combination
            if breakfast_meal is None or lunch_meal is None or dinner_meal is None:
                QMessageBox.warning(self, 'Thông báo', 'Không đủ món ăn')
                return
            self.uic3.txtThucDon.setText("Sáng: " + breakfast_meal[1] + "\nTrưa: " + lunch_meal[1] + "\nChiều: " +dinner_meal[1])

        if self.bmr < 2500 and self.bmr > 1600:
            breakfast_meal = None
            lunch_meal = None
            dinner_meal = None
            evening_meal = None
            closest_difference = float('inf')
            for combination in itertools.combinations(lstThucDon, 4):
                current_calories = sum(meal[6] for meal in combination)
                current_difference = abs(current_calories - self.bmr)
                if current_difference < closest_difference:
                    closest_difference = current_difference
                    breakfast_meal, lunch_meal, dinner_meal, evening_meal = combination
            if breakfast_meal is None or lunch_meal is None or dinner_meal is None or evening_meal is None:
                QMessageBox.warning(self, 'Thông báo', 'Không đủ món ăn')
                return
            self.uic3.txtThucDon.setText("Sáng: " + breakfast_meal[1] + "\nTrưa: " + lunch_meal[1] + "\nChiều: " +dinner_meal[1] + "\nTối: " + evening_meal[1])
        
        if self.bmr >= 2500:
            print("Hello")
            breakfast_meal = None
            lunch_meal = None
            dinner_meal = None
            evening_meal = None
            midnight_meal = None
            total_calories = float('inf')
            closest_difference = float('inf')
            for combination in itertools.combinations(lstThucDon, 5):
                current_calories = sum(meal[6] for meal in combination)
                current_difference = abs(current_calories - self.bmr)
                if current_difference < closest_difference:
                    closest_difference = current_difference
                    breakfast_meal, lunch_meal, dinner_meal, evening_meal, midnight_meal = combination
            if breakfast_meal is None or lunch_meal is None or dinner_meal is None or evening_meal is None or midnight_meal is None:
                QMessageBox.warning(self, 'Thông báo', 'Không đủ món ăn')
                return
            self.uic3.txtThucDon.setText("Sáng: " + breakfast_meal[1] + "\nTrưa: " + lunch_meal[1] + "\nChiều: " +dinner_meal[1] + "\nTối: " + evening_meal[1] + "\nKhuya: " + midnight_meal[1])
        

        text = self.uic3.txtThucDon.toPlainText()
        elements = text.split("\n")
        formatted_text = ";".join(elements)

        # Lấy thông tin ngày tháng hiện tại
        current_date = datetime.datetime.now()

        # Dịch định dạng ngày tháng sang tiếng Việt
        date_string = format_date(current_date, format='full', locale='vi_VN')

        # Thêm thông tin ngày tháng vào trước nội dung
        formatted_text_with_date = f"{date_string};{formatted_text}\n"

        with open("lichsu.txt", "a", encoding="utf-8") as file:
            file.write(formatted_text_with_date.replace("Sáng: ", "").replace("Trưa: ", "").replace("Chiều: ", "").replace("Tối: ", "").replace("Khuya: ", ""))

        self.loadLichSu()

    def next(self):
        self.main_win_2.show()
        main_win.close()
    def calbmr(self):
        if self.uic2.comboBoxGioiTinh.currentText() == "Nam":
            self.bmr = 66 +(13.7 * int(self.uic2.spinBoxCanNang.text())) + (5 * (int(self.uic2.spinBoxChieuCao.text()))) - (6.8 * int(self.uic2.spinBoxTuoi.text()))
        else:
            self.bmr = 665 +(9.6 * int(self.uic2.spinBoxCanNang.text())) + (5 * (int(self.uic2.spinBoxChieuCao.text()))) - (6.8 * int(self.uic2.spinBoxTuoi.text()))
        self.uic2.labelTongLuongCalo.setText(str(int(self.bmr)))

        
if __name__ == "__main__":            
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()
    sys.exit(app.exec())