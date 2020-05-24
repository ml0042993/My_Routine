import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
from Core.Proxy.verification_proxy import Verification
from Core.Spider import Spiders_Chi,Spiders_Eur,Spiders_Jap
# from PyQt5.QtGui import
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI
	##==========自定义功能函数==========
	def run_proxy(self):
		Verification().run_proxy()
	def run_spider(self):
		Spiders_Jap.Get_Jap().run_japsite()
		Spiders_Eur.Get_Eur().run_eursite()
		Spiders_Chi.Get_Chi().run_chisite()
	##==========事件处理函数===========
	def on_refresh_Button_clicked(self):

		self.run_proxy()
	def on_Init_Button_clicked(self):
		self.run_spider()
	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())