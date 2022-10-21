# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compilerWin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_compilerWin(object):
    def setupUi(self, compilerWin):
        if not compilerWin.objectName():
            compilerWin.setObjectName(u"compilerWin")
        compilerWin.resize(1019, 640)
        compilerWin.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(220,220, 255);\n"
"	color:black;\n"
"}\n"
"\n"
"QMainWindow{\n"
"	background-color:rgb(50, 0, 90);\n"
"}\n"
"QTabWidget{\n"
"	background-color:rgb(85, 0, 127);\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"QMenuBar{\n"
"	background-color:rgb(50, 0, 90);\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"/**/\n"
"QMenuBar::item {\n"
"			padding:2px 7%;\n"
"           \n"
" }\n"
"\n"
" QMenuBar::item::selected {\n"
" background-color: rgb(50,30,100);\n"
"}\n"
"\n"
"QMenu {\n"
"	background-color: rgb(120, 40, 160);\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid #000;           \n"
"}\n"
"\n"
"QMenu::item::selected {\n"
"	 background-color: rgb(10,20,100);\n"
" }\n"
"/***/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"	background-color:rgb(50, 0, 90);\n"
"	color:white;\n"
"	padding:2%;\n"
"}\n"
"QStatusBar{\n"
"	background-color:rgb(85, 0, 127);\n"
"\n"
"}\n"
"/*\n"
"QTabWidget QWidget {\n"
"	background-color:rgb(240,240 , 255);\n"
"\n"
"}*/\n"
"\n"
"QTabBar  {\n"
""
                        " 	background-color:rgb(70, 40, 130);\n"
"	color:white;\n"
"	padding:0;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background :rgb(55, 0, 110);\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	background-color:rgb(240,240 , 255);\n"
"}\n"
"")
        compilerWin.setTabShape(QTabWidget.Rounded)
        self.actionNew = QAction(compilerWin)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOprn = QAction(compilerWin)
        self.actionOprn.setObjectName(u"actionOprn")
        self.actionSave = QAction(compilerWin)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(compilerWin)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionUndo = QAction(compilerWin)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(compilerWin)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(compilerWin)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(compilerWin)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPest = QAction(compilerWin)
        self.actionPest.setObjectName(u"actionPest")
        self.actionCompile = QAction(compilerWin)
        self.actionCompile.setObjectName(u"actionCompile")
        self.actionExecute = QAction(compilerWin)
        self.actionExecute.setObjectName(u"actionExecute")
        self.actionAbou_Us = QAction(compilerWin)
        self.actionAbou_Us.setObjectName(u"actionAbou_Us")
        self.actionSystem_Font = QAction(compilerWin)
        self.actionSystem_Font.setObjectName(u"actionSystem_Font")
        self.actionColoy = QAction(compilerWin)
        self.actionColoy.setObjectName(u"actionColoy")
        self.actionExit = QAction(compilerWin)
        self.actionExit.setObjectName(u"actionExit")
        self.actionFont = QAction(compilerWin)
        self.actionFont.setObjectName(u"actionFont")
        self.actionDebug = QAction(compilerWin)
        self.actionDebug.setObjectName(u"actionDebug")
        self.actionContuct_Us = QAction(compilerWin)
        self.actionContuct_Us.setObjectName(u"actionContuct_Us")
        self.actionSetings = QAction(compilerWin)
        self.actionSetings.setObjectName(u"actionSetings")
        self.centralwidget = QWidget(compilerWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setLocale(QLocale(QLocale.Erzya, QLocale.Russia))
        self.tabWidget.setInputMethodHints(Qt.ImhNone)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        icon = QIcon()
        iconThemeName = u"text-html"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.newBtn = QPushButton(self.centralwidget)
        self.newBtn.setObjectName(u"newBtn")

        self.verticalLayout_2.addWidget(self.newBtn)

        self.openBtn = QPushButton(self.centralwidget)
        self.openBtn.setObjectName(u"openBtn")

        self.verticalLayout_2.addWidget(self.openBtn)

        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")

        self.verticalLayout_2.addWidget(self.saveBtn)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.selectBtn = QComboBox(self.centralwidget)
        self.selectBtn.addItem("")
        self.selectBtn.addItem("")
        self.selectBtn.addItem("")
        self.selectBtn.addItem("")
        self.selectBtn.setObjectName(u"selectBtn")

        self.verticalLayout_2.addWidget(self.selectBtn)

        self.compileBtn = QPushButton(self.centralwidget)
        self.compileBtn.setObjectName(u"compileBtn")

        self.verticalLayout_2.addWidget(self.compileBtn)

        self.executeBtn = QPushButton(self.centralwidget)
        self.executeBtn.setObjectName(u"executeBtn")

        self.verticalLayout_2.addWidget(self.executeBtn)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.errorLogBtn = QPushButton(self.centralwidget)
        self.errorLogBtn.setObjectName(u"errorLogBtn")

        self.verticalLayout_2.addWidget(self.errorLogBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        compilerWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(compilerWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1019, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSetings = QMenu(self.menubar)
        self.menuSetings.setObjectName(u"menuSetings")
        compilerWin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(compilerWin)
        self.statusbar.setObjectName(u"statusbar")
        compilerWin.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSetings.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOprn)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPest)
        self.menuEdit.addAction(self.actionFont)
        self.menuRun.addAction(self.actionCompile)
        self.menuRun.addAction(self.actionExecute)
        self.menuRun.addAction(self.actionDebug)
        self.menuHelp.addAction(self.actionAbou_Us)
        self.menuHelp.addAction(self.actionContuct_Us)
        self.menuSetings.addAction(self.actionSystem_Font)
        self.menuSetings.addAction(self.actionColoy)
        self.menuSetings.addAction(self.actionSetings)

        self.retranslateUi(compilerWin)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(compilerWin)
    # setupUi

    def retranslateUi(self, compilerWin):
        compilerWin.setWindowTitle(QCoreApplication.translate("compilerWin", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("compilerWin", u"New", None))
        self.actionOprn.setText(QCoreApplication.translate("compilerWin", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("compilerWin", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("compilerWin", u"Save As", None))
        self.actionUndo.setText(QCoreApplication.translate("compilerWin", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("compilerWin", u"Redo", None))
        self.actionCut.setText(QCoreApplication.translate("compilerWin", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("compilerWin", u"Copy", None))
        self.actionPest.setText(QCoreApplication.translate("compilerWin", u"Pest", None))
        self.actionCompile.setText(QCoreApplication.translate("compilerWin", u"Compile", None))
        self.actionExecute.setText(QCoreApplication.translate("compilerWin", u"Execute", None))
        self.actionAbou_Us.setText(QCoreApplication.translate("compilerWin", u"Abou Us", None))
        self.actionSystem_Font.setText(QCoreApplication.translate("compilerWin", u"System Font", None))
        self.actionColoy.setText(QCoreApplication.translate("compilerWin", u"Color", None))
        self.actionExit.setText(QCoreApplication.translate("compilerWin", u"Exit", None))
        self.actionFont.setText(QCoreApplication.translate("compilerWin", u"Font", None))
        self.actionDebug.setText(QCoreApplication.translate("compilerWin", u"Debug", None))
        self.actionContuct_Us.setText(QCoreApplication.translate("compilerWin", u"Contuct Us", None))
        self.actionSetings.setText(QCoreApplication.translate("compilerWin", u"Setings", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("compilerWin", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("compilerWin", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("compilerWin", u"File", None))
        self.newBtn.setText(QCoreApplication.translate("compilerWin", u"New", None))
        self.openBtn.setText(QCoreApplication.translate("compilerWin", u"Open", None))
        self.saveBtn.setText(QCoreApplication.translate("compilerWin", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("compilerWin", u"Compiler", None))
        self.selectBtn.setItemText(0, QCoreApplication.translate("compilerWin", u"Java", None))
        self.selectBtn.setItemText(1, QCoreApplication.translate("compilerWin", u"C", None))
        self.selectBtn.setItemText(2, QCoreApplication.translate("compilerWin", u"C++", None))
        self.selectBtn.setItemText(3, QCoreApplication.translate("compilerWin", u"Python", None))

        self.compileBtn.setText(QCoreApplication.translate("compilerWin", u"Compile", None))
        self.executeBtn.setText(QCoreApplication.translate("compilerWin", u"Execute", None))
        self.label_3.setText(QCoreApplication.translate("compilerWin", u"Debug", None))
        self.errorLogBtn.setText(QCoreApplication.translate("compilerWin", u"Error Log", None))
        self.menuFile.setTitle(QCoreApplication.translate("compilerWin", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("compilerWin", u"Edit", None))
        self.menuRun.setTitle(QCoreApplication.translate("compilerWin", u"Run", None))
        self.menuHelp.setTitle(QCoreApplication.translate("compilerWin", u"Help", None))
        self.menuSetings.setTitle(QCoreApplication.translate("compilerWin", u"System", None))
    # retranslateUi

