from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import datetime

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = 'Click the Button'
		self.left = 10
		self.top = 10
		self.width = 800
		self.height = 800
		self.counter = 0
		self.autoClickers = 0
		self.autoAutoClickers = 0
		self.curPrice = 10 + (self.autoClickers * 5)
		self.curPrice2 = 20 + (self.autoClickers * 10)
		self.timer = QTimer()
		self.label1 = QLabel('You have clicked ' + str(self.counter) + ' times.', self)
		self.label2 = QLabel('You have ' + str(self.autoClickers) + ' Auto Clickers', self)
		self.label3 = QLabel('You have ' + str(self.autoAutoClickers) + ' Auto Auto Clickers', self)
		self.mainButton = QPushButton('Button', self)
		self.autoClickerButton = QPushButton('AutoClickers', self)
		self.autoAutoClickerButton = QPushButton('AutoClickers', self)
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		# The main clicking button
		self.mainButton.move(200, 200)
		self.mainButton.adjustSize()
		self.mainButton.clicked.connect(self.on_click)

		# The button to buy autoClickers
		self.autoClickerButton.move(200, 250)
		self.autoClickerButton.adjustSize()
		self.autoClickerButton.clicked.connect(self.buy_auto_clicker)

		# The button to buy autoAutoClickers
		self.autoAutoClickerButton.move(200, 300)
		self.autoAutoClickerButton.adjustSize()
		self.autoAutoClickerButton.clicked.connect(self.buy_auto_auto_clicker)
 
 		# Label showing clicks
		self.label1.move(200, 50)
		self.label1.adjustSize()

		# Label showing auto clickers
		self.label2.move(200, 100)
		self.label2.adjustSize()

		# Label showing auto auto clickers
		self.label3.move(200, 150)
		self.label3.adjustSize()

		# Label showing Buying Autoclicker Button
		self.autoClickerButton.setText('AutoClickers: ' + str(self.curPrice) + ' Clicks required')
		self.autoClickerButton.adjustSize()

		# Label showing Buying Autoclicker Button
		self.autoAutoClickerButton.setText('AutoAutoClickers: ' + str(self.curPrice2) + ' Auto Clickers required')
		self.autoAutoClickerButton.adjustSize()

		# Timer setup
		self.timer.timeout.connect(self.increment_clicks)
		self.timer.start(1000)

		# Submit the UI
		self.show()
		
	@pyqtSlot()
	def on_click(self):
		self.counter += 1
		self.update_labels()

	@pyqtSlot()
	def buy_auto_clicker(self):
		if self.curPrice <= self.counter:
			self.autoClickers += 1
			self.counter -= self.curPrice
			
			self.update_labels()

	@pyqtSlot()
	def buy_auto_auto_clicker(self):
		if self.curPrice2 <= self.autoClickers:
			self.autoAutoClickers += 1
			self.autoClickers -= self.curPrice2
		
			self.update_labels()

	def increment_clicks(self):
		self.counter += (1 * self.autoClickers)
		self.autoClickers += (1 * self.autoAutoClickers)
		self.update_labels()

	def update_labels(self):
		# Update Label 1
		self.label1.setText('You have clicked ' + str(self.counter) + ' times.')
		self.label1.adjustSize()

		# Update Label 2
		self.label2.setText('You have ' + str(self.autoClickers) + ' Auto Clickers')
		self.label2.adjustSize()

		# Update Label 3
		self.label3.setText('You have ' + str(self.autoAutoClickers) + ' Auto Auto Clickers')
		self.label3.adjustSize()

		# Update AutoClicker Button
		self.autoClickerButton.setText('AutoClickers: ' + str(self.curPrice) + ' Clicks required')
		self.autoClickerButton.adjustSize()

		# Update AutoAutoClicker Button
		self.autoAutoClickerButton.setText('AutoAutoClickers: ' + str(self.curPrice2) + ' Auto Clickers required')
		self.autoAutoClickerButton.adjustSize()

		# Update Prices
		self.curPrice = 10 + (self.autoClickers * 5)
		self.curPrice2 = 20 + (self.autoAutoClickers * 10)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()

	sys.exit(app.exec_())