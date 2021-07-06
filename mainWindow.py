from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.operatorsList = ['+','-','x','/']
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
        self.eightBtn.clicked.connect(self.slotNumClicked)
        self.nineBtn = QPushButton('9')
        self.nineBtn.clicked.connect(self.slotNumClicked)

        self.fourBtn = QPushButton('4')
        self.fourBtn.clicked.connect(self.slotNumClicked)
        self.fiveBtn = QPushButton('5')
        self.fiveBtn.clicked.connect(self.slotNumClicked)
        self.sixBtn = QPushButton('6')
        self.sixBtn.clicked.connect(self.slotNumClicked)

        self.oneBtn = QPushButton('1')
        self.oneBtn.clicked.connect(self.slotNumClicked)
        self.twoBtn = QPushButton('2')
        self.twoBtn.clicked.connect(self.slotNumClicked)
        self.threeBtn = QPushButton('3')
        self.threeBtn.clicked.connect(self.slotNumClicked)

        self.zeroBtn = QPushButton('0')
        self.zeroBtn.clicked.connect(self.slotNumClicked)
        self.decBtn = QPushButton('.')
        self.decBtn.clicked.connect(self.slotNumClicked)
        self.plusBtn = QPushButton('+')
        self.plusBtn.clicked.connect(self.slotNumClicked)
        self.minusBtn = QPushButton('-')
        self.minusBtn.clicked.connect(self.slotNumClicked)
        self.multBtn = QPushButton('x')
        self.multBtn.clicked.connect(self.slotNumClicked)
        self.divBtn = QPushButton('/')
        self.divBtn.clicked.connect(self.slotNumClicked)
        self.delBtn = QPushButton('del')
        self.delBtn.clicked.connect(self.slotDelClicked)

        self.equalsBtn = QPushButton('=')
        self.equalsBtn.clicked.connect(self.slotEqualsClicked)

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
    def slotDelClicked(self):
        leTxt = self.outLE.text()
        leTxt = leTxt[:-1]
        self.outLE.setText(leTxt)
    #end slotDelClicked
    def slotEqualsClicked(self):
        eqTxt = self.outLE.text()
        operatorIndxList = []
        iKtr = 0
        for chr in eqTxt:
            if chr in self.operatorsList:
                operatorIndxList.append(iKtr)
            #end if
            iKtr += 1
        #next
        floatList = []
        eqList = []
        prevIndx = 0
        for indx in operatorIndxList:
            thisFloat = float(eqTxt[prevIndx:indx])
            floatList.append(thisFloat)
            eqList.append(thisFloat)
            eqList.append(eqTxt[indx])
            prevIndx = indx + 1
        #next
        lastFloat = float(eqTxt[indx+1:])
        eqList.append(lastFloat)

        x = eqList[0]
        func = eqList[1]
        y = eqList[2]
        if func == '+':
            out = self.add(x,y)
        elif func == '-':
            out = self.subtract(x,y)
        elif func == 'x':
            out = self.multiply(x,y)
        elif func == '/':
            out = self.divide(x,y)
        else:
            print('operation not recognized: ',func)
        #end if

        # thisFloatStr = ''
        # calcList = []
        # for chr in eqTxt:
        #     if chr not in self.operatorsList:
        #         thisFloatStr += chr
        #     else:
        #         thisFloat = float(thisFloatStr)
        #         calcList.append(thisFloat)
        #         calcList.append(chr)
        #         thisFloatStr = ''
        #     #end if
        # #next


        # x = None
        # y = None
        # func = None
        # for c in calcList:
        #     if isinstance(c, float):
        #         if x is None:
        #             x = c
        #         elif y is None:
        #             y = c
        #             if func is None:
        #                 print("improper syntax")
        #             else:
        #                 if func == '+':
        #                     x = self.add(x,y)
        #                 elif func == '-':
        #                     x = self.subtract(x,y)
        #                 elif func == 'x':
        #                     x = self.multiply(x,y)
        #                 elif func == '/':
        #                     x = self.divide(x,y)
        #                 else:
        #                     print('operation not recognized: ',func)
        #                 #end if
        #                 y = None
        #                 func = None
        #             #end if
        #         #end if
        #     elif isinstance(c,str):
        #         func = c
        #     #end if
        # #next c

        self.outLE.setText(str(out))
    #end slotEqualsClicked
    def add(self,x,y):
        return x + y
    #end add
    def subtract(self,x,y):
        return x - y
    #end subtract
    def multiply(self,x,y):
        return x * y
    #end multiply
    def divide(self,x,y):
        return x / y
    #end divide



