from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    #end __init__
    def setupUI(self):
        self.setWindowTitle('PyCalc')

        #
        #  Make Widgets
        #
        self.outLE = QLineEdit()

        self.sevenBtn = QPushButton('7')
        self.sevenBtn.clicked.connect(self.slotNumClicked)
        self.eightBtn = QPushButton('8')
        self.nineBtn = QPushButton('9')

        self.fourBtn = QPushButton('4')
        self.fiveBtn = QPushButton('5')
        self.sixBtn = QPushButton('6')

        self.oneBtn = QPushButton('1')
        self.twoBtn = QPushButton('2')
        self.threeBtn = QPushButton('3')

        self.zeroBtn = QPushButton('0')
        self.decBtn = QPushButton('.')
        self.plusBtn = QPushButton('+')
        self.minusBtn = QPushButton('-')
        self.multBtn = QPushButton('x')
        self.divBtn = QPushButton('/')
        self.delBtn = QPushButton('del')

        self.equalsBtn = QPushButton('=')

        #
        #  Layout
        #
        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        mainLayout.addWidget(self.outLE, 0,0,1,4)

        mainLayout.addWidget(self.sevenBtn, 1,0,1,1)
        mainLayout.addWidget(self.eightBtn, 1,1,1,1)
        mainLayout.addWidget(self.nineBtn, 1,2,1,1)
        mainLayout.addWidget(self.plusBtn, 1,3,1,1)

        mainLayout.addWidget(self.fourBtn, 2,0,1,1)
        mainLayout.addWidget(self.fiveBtn, 2,1,1,1)
        mainLayout.addWidget(self.sixBtn, 2,2,1,1)
        mainLayout.addWidget(self.minusBtn, 2,3,1,1)

        mainLayout.addWidget(self.oneBtn, 3,0,1,1)
        mainLayout.addWidget(self.twoBtn, 3,1,1,1)
        mainLayout.addWidget(self.threeBtn, 3,2,1,1)
        mainLayout.addWidget(self.multBtn, 3,3,1,1)

        mainLayout.addWidget(self.zeroBtn, 4,0,1,1)
        mainLayout.addWidget(self.decBtn, 4,1,1,1)
        mainLayout.addWidget(self.delBtn, 4,2,1,1)
        mainLayout.addWidget(self.divBtn, 4,3,1,1)

        mainLayout.addWidget(self.equalsBtn, 5,0,1,4)
    #end setupUI
    def slotNumClicked(self):
        if isinstance(self.sender(), QPushButton):
            num = self.sender().text()
            leTxt = self.outLE.text()
            leTxt += num
            self.outLE.setText(leTxt)
        #end if
    #end slotNumClicked



