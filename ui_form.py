# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(921, 750)
        Widget.setMinimumSize(QSize(921, 750))
        Widget.setMaximumSize(QSize(921, 750))
        self.comboBox = QComboBox(Widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(9, 9, 100, 26))
        self.tableWidget = QTableWidget(Widget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(10, 80, 891, 291))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(1000, 16777215))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.refreshButton = QPushButton(Widget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(810, 10, 80, 26))
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 380, 891, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelMoreBefore = QLabel(self.gridLayoutWidget)
        self.labelMoreBefore.setObjectName(u"labelMoreBefore")
        self.labelMoreBefore.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreBefore, 4, 1, 1, 1)

        self.labelMoreBeforeStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreBeforeStatic.setObjectName(u"labelMoreBeforeStatic")
        self.labelMoreBeforeStatic.setMouseTracking(False)
        self.labelMoreBeforeStatic.setTabletTracking(False)
        self.labelMoreBeforeStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreBeforeStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreBeforeStatic, 4, 0, 1, 1)

        self.labelMoreAutorun = QLabel(self.gridLayoutWidget)
        self.labelMoreAutorun.setObjectName(u"labelMoreAutorun")
        self.labelMoreAutorun.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreAutorun, 3, 1, 1, 1)

        self.labelMoreNameStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreNameStatic.setObjectName(u"labelMoreNameStatic")

        self.gridLayout.addWidget(self.labelMoreNameStatic, 0, 0, 1, 1)

        self.labelMoreConflicts = QLabel(self.gridLayoutWidget)
        self.labelMoreConflicts.setObjectName(u"labelMoreConflicts")
        self.labelMoreConflicts.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreConflicts, 8, 1, 1, 1)

        self.labelMoreDescription = QLabel(self.gridLayoutWidget)
        self.labelMoreDescription.setObjectName(u"labelMoreDescription")
        self.labelMoreDescription.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreDescription, 1, 1, 1, 1)

        self.labelMoreDescriptionStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreDescriptionStatic.setObjectName(u"labelMoreDescriptionStatic")

        self.gridLayout.addWidget(self.labelMoreDescriptionStatic, 1, 0, 1, 1)

        self.labelMoreAutorunStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreAutorunStatic.setObjectName(u"labelMoreAutorunStatic")
        self.labelMoreAutorunStatic.setMouseTracking(False)
        self.labelMoreAutorunStatic.setTabletTracking(False)
        self.labelMoreAutorunStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreAutorunStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreAutorunStatic, 3, 0, 1, 1)

        self.labelMoreAfterStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreAfterStatic.setObjectName(u"labelMoreAfterStatic")
        self.labelMoreAfterStatic.setMouseTracking(False)
        self.labelMoreAfterStatic.setTabletTracking(False)
        self.labelMoreAfterStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreAfterStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreAfterStatic, 5, 0, 1, 1)

        self.labelMoreConflictsStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreConflictsStatic.setObjectName(u"labelMoreConflictsStatic")
        self.labelMoreConflictsStatic.setMouseTracking(False)
        self.labelMoreConflictsStatic.setTabletTracking(False)
        self.labelMoreConflictsStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreConflictsStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreConflictsStatic, 8, 0, 1, 1)

        self.labelMoreWants = QLabel(self.gridLayoutWidget)
        self.labelMoreWants.setObjectName(u"labelMoreWants")
        self.labelMoreWants.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreWants, 7, 1, 1, 1)

        self.labelMoreWantsStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreWantsStatic.setObjectName(u"labelMoreWantsStatic")
        self.labelMoreWantsStatic.setMouseTracking(False)
        self.labelMoreWantsStatic.setTabletTracking(False)
        self.labelMoreWantsStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreWantsStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreWantsStatic, 7, 0, 1, 1)

        self.labelMoreAfter = QLabel(self.gridLayoutWidget)
        self.labelMoreAfter.setObjectName(u"labelMoreAfter")
        self.labelMoreAfter.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreAfter, 5, 1, 1, 1)

        self.labelMoreStateStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreStateStatic.setObjectName(u"labelMoreStateStatic")
        self.labelMoreStateStatic.setMouseTracking(False)
        self.labelMoreStateStatic.setTabletTracking(False)
        self.labelMoreStateStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreStateStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreStateStatic, 2, 0, 1, 1)

        self.labelMoreName = QLabel(self.gridLayoutWidget)
        self.labelMoreName.setObjectName(u"labelMoreName")
        self.labelMoreName.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreName, 0, 1, 1, 1)

        self.labelMoreRequires = QLabel(self.gridLayoutWidget)
        self.labelMoreRequires.setObjectName(u"labelMoreRequires")
        self.labelMoreRequires.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreRequires, 6, 1, 1, 1)

        self.labelMoreRequiresStatic = QLabel(self.gridLayoutWidget)
        self.labelMoreRequiresStatic.setObjectName(u"labelMoreRequiresStatic")
        self.labelMoreRequiresStatic.setMouseTracking(False)
        self.labelMoreRequiresStatic.setTabletTracking(False)
        self.labelMoreRequiresStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMoreRequiresStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMoreRequiresStatic, 6, 0, 1, 1)

        self.labelMoreState = QLabel(self.gridLayoutWidget)
        self.labelMoreState.setObjectName(u"labelMoreState")
        self.labelMoreState.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMoreState, 2, 1, 1, 1)

        self.labelMorePathToUnitStatic = QLabel(self.gridLayoutWidget)
        self.labelMorePathToUnitStatic.setObjectName(u"labelMorePathToUnitStatic")
        self.labelMorePathToUnitStatic.setMouseTracking(False)
        self.labelMorePathToUnitStatic.setTabletTracking(False)
        self.labelMorePathToUnitStatic.setInputMethodHints(Qt.ImhNone)
        self.labelMorePathToUnitStatic.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.labelMorePathToUnitStatic, 9, 0, 1, 1)

        self.labelMorePathToUnit = QLabel(self.gridLayoutWidget)
        self.labelMorePathToUnit.setObjectName(u"labelMorePathToUnit")
        self.labelMorePathToUnit.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.labelMorePathToUnit, 9, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 6)
        self.startStopButton = QPushButton(Widget)
        self.startStopButton.setObjectName(u"startStopButton")
        self.startStopButton.setEnabled(False)
        self.startStopButton.setGeometry(QRect(260, 10, 80, 26))
        self.startStopButton.setAutoDefault(False)
        self.startStopButton.setFlat(False)
        self.enableDisableButton = QPushButton(Widget)
        self.enableDisableButton.setObjectName(u"enableDisableButton")
        self.enableDisableButton.setEnabled(False)
        self.enableDisableButton.setGeometry(QRect(380, 10, 80, 26))
        self.searchBar = QLineEdit(Widget)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(10, 50, 891, 26))

        self.retranslateUi(Widget)

        self.startStopButton.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"All", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Service", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"Mount", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"Swap", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"Socket", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Widget", u"Target", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Widget", u"Device", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Widget", u"Automount", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Widget", u"Timer", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Widget", u"Path", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Widget", u"Slice", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Widget", u"Scope", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Unit", None));
        self.refreshButton.setText(QCoreApplication.translate("Widget", u"refresh", None))
        self.labelMoreBefore.setText("")
        self.labelMoreBeforeStatic.setText(QCoreApplication.translate("Widget", u"Before", None))
        self.labelMoreAutorun.setText("")
        self.labelMoreNameStatic.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.labelMoreConflicts.setText("")
        self.labelMoreDescription.setText("")
        self.labelMoreDescriptionStatic.setText(QCoreApplication.translate("Widget", u"Description", None))
        self.labelMoreAutorunStatic.setText(QCoreApplication.translate("Widget", u"Autorun", None))
        self.labelMoreAfterStatic.setText(QCoreApplication.translate("Widget", u"After", None))
        self.labelMoreConflictsStatic.setText(QCoreApplication.translate("Widget", u"Conflicts", None))
        self.labelMoreWants.setText("")
        self.labelMoreWantsStatic.setText(QCoreApplication.translate("Widget", u"Wants", None))
        self.labelMoreAfter.setText("")
        self.labelMoreStateStatic.setText(QCoreApplication.translate("Widget", u"State", None))
        self.labelMoreName.setText("")
        self.labelMoreRequires.setText("")
        self.labelMoreRequiresStatic.setText(QCoreApplication.translate("Widget", u"Requires", None))
        self.labelMoreState.setText("")
        self.labelMorePathToUnitStatic.setText(QCoreApplication.translate("Widget", u"Path to unit", None))
        self.labelMorePathToUnit.setText("")
        self.startStopButton.setText("")
        self.enableDisableButton.setText("")
    # retranslateUi

