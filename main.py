import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Click the Button'

        # Initialize variables
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 800
        self.counter = 0
        self.clickingPower = 1
        self.autoClickingPower = 1
        self.autoClickers = 0
        self.autoAutoClickers = 0
        self.clicksPerSecond = 0

        # Initialize the prices
        self.curPrice = 10 + (self.autoClickers * 5)
        self.curPrice2 = 20 + (self.autoAutoClickers * 10)
        self.curPrice3 = 50 * (self.clickingPower ** 2)
        self.curPrice4 = 100 * (self.autoClickingPower ** 2)

        # Initialize the timer
        self.timer = QTimer()

        # Initialize the Labels
        self.clicksLabel = QLabel('You have clicked ' + str(self.counter) + ' times.', self)
        self.autoClicksLabel = QLabel('You have ' + str(self.autoClickers) + ' AutoClickers', self)
        self.autoAutoClicksLabel = QLabel('You have ' + str(self.autoAutoClickers) + ' AutoAutoClickers', self)
        self.clicksPerSecondLabel = QLabel('CPS: ' + str(self.clicksPerSecond), self)

        # Initialize Buttons
        self.mainButton = QPushButton(self)
        self.autoClickerButton = QPushButton(self)
        self.autoAutoClickerButton = QPushButton(self)
        self.clickingPowerButton = QPushButton(self)
        self.autoClickingPowerButton = QPushButton(self)
        
        # Initialize the UI
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
 
        # The button to buy clicking power upgrade
        self.clickingPowerButton.move(300, 200)
        self.clickingPowerButton.adjustSize()
        self.clickingPowerButton.clicked.connect(self.upgrade_clicking)

        # The button to buy autoClicking power upgrade
        self.autoClickingPowerButton.move(375, 250)
        self.autoClickingPowerButton.adjustSize()
        self.autoClickingPowerButton.clicked.connect(self.upgrade_auto_clicking)

        # Label showing clicks per second
        self.clicksPerSecondLabel.move(350, 50)
        self.clicksPerSecondLabel.adjustSize()

        # Label showing clicks
        self.clicksLabel.move(200, 50)
        self.clicksLabel.adjustSize()

        # Label showing auto clickers
        self.autoClicksLabel.move(200, 100)
        self.autoClicksLabel.adjustSize()

        # Label showing auto auto clickers
        self.autoAutoClicksLabel.move(200, 150)
        self.autoAutoClicksLabel.adjustSize()

        # Label showing Clicker Button
        self.mainButton.setText('Clicking Power: ' + str(self.clickingPower))
        self.mainButton.adjustSize()

        # Label showing Buying Autoclicker Button
        self.autoClickerButton.setText('AutoClickers: ' + str(self.curPrice) + ' Clicks required')
        self.autoClickerButton.adjustSize()

        # Label showing Buying Autoclicker Button
        self.autoAutoClickerButton.setText('AutoAutoClickers: ' + str(self.curPrice2) + ' AutoClickers required')
        self.autoAutoClickerButton.adjustSize()

        # Label showing Clicker Upgrade Button
        self.clickingPowerButton.setText('Upgrade clicking power: ' + str(self.curPrice3) + ' clicks required')
        self.clickingPowerButton.adjustSize()

        # Label showing Autoclicker Upgrade Button
        self.autoClickingPowerButton.setText('Upgrade auto clicking power: ' + str(self.curPrice4) + ' clicks required')
        self.autoClickingPowerButton.adjustSize()

        # Timer setup
        self.timer.timeout.connect(self.increment_clicks)
        self.timer.start(1000)

        # Submit the UI
        self.show()
		
    @pyqtSlot()
    def on_click(self):
        self.counter += self.clickingPower
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
            self.counter = 0

            self.update_labels()

    @pyqtSlot()
    def upgrade_clicking(self):
        if self.curPrice3 <= self.counter:
            self.clickingPower += 1
            self.counter -= self.curPrice3

            self.update_labels()

    @pyqtSlot()
    def upgrade_auto_clicking(self):
        if self.curPrice4 <= self.counter:
            self.autoClickingPower += 1
            self.counter -= self.curPrice4
            self.update_labels()

    def increment_clicks(self):
        self.counter += (1 * self.autoClickers)
        self.autoClickers += (1 * self.autoAutoClickers)
        self.clicksPerSecond = self.autoClickers
        self.update_labels()

    def update_labels(self):
        # Update clicks label
        self.clicksLabel.setText('You have clicked ' + str(self.counter) + ' times.')
        self.clicksLabel.adjustSize()

        # Update auto clicks label
        self.autoClicksLabel.setText('You have ' + str(self.autoClickers) + ' AutoClickers')
        self.autoClicksLabel.adjustSize()

        # Update auto auto clicks label
        self.autoAutoClicksLabel.setText('You have ' + str(self.autoAutoClickers) + ' AutoAutoClickers')
        self.autoAutoClicksLabel.adjustSize()

        # Update clicks per second label
        self.clicksPerSecondLabel.setText('CPS: ' + str(self.clicksPerSecond * self.autoClickingPower))
        self.clicksPerSecondLabel.adjustSize()

        # Update AutoClicker Button
        self.mainButton.setText('Clicking Power: ' + str(self.clickingPower))
        self.mainButton.adjustSize()

        # Update AutoClicker Button
        self.autoClickerButton.setText('AutoClickers: ' + str(self.curPrice) + ' Clicks required')
        self.autoClickerButton.adjustSize()

        # Update AutoAutoClicker Button
        self.autoAutoClickerButton.setText('AutoAutoClickers: ' + str(self.curPrice2) + ' AutoClickers required')
        self.autoAutoClickerButton.adjustSize()

        # Update Clicking Power Button
        self.clickingPowerButton.setText('Upgrade clicking power: ' + str(self.curPrice3) + ' clicks required')
        self.clickingPowerButton.adjustSize()

        # Update AutoClicking Power Button
        self.autoClickingPowerButton.setText('Upgrade auto clicking power: ' + str(self.curPrice4) + ' clicks required')
        self.autoClickingPowerButton.adjustSize()

        # Update Prices
        self.curPrice = 10 + (self.autoClickers * 5)
        self.curPrice2 = 20 + (self.autoAutoClickers * 10)
        self.curPrice3 = 50 * (self.clickingPower ** 2)
        self.curPrice4 = 100 * (self.autoClickingPower ** 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())
