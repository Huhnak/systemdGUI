# This Python file uses the following encoding: utf-8
import sys
import enum, subprocess
from typing import Union
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class UnitType(enum.Enum):
    ALL = 0
    SERVICE = 'service'
    MOUNT = 'mount'
    SWAP = 'swap'
    SOCKET = 'socket'
    TARGET = 'target'
    DEVICE = 'device'
    AUTOMOUNT = 'automount'
    TIMER = 'timer'
    PATH = 'path'
    SLICE = 'slice'
    SCOPE = 'scope'


class FileSections(enum.Enum):
    UNIT = '[Unit]'
    INSTALL = '[Install]'
    SERVICE = '[Service]'
    SOCKET = '[Socket]'
    DEVICE = '[Device]'
    MOUNT = '[Mount]'
    AUTOMOUNT = '[Automount]'
    SWAP = '[Swap]'
    TARGET = '[Target]'
    PATH = '[Path]'
    TIMER = '[Timer]'
    SLICE = '[Slice]'
    SCOPE = '[Scope]'


units = dict()
currentType = UnitType.ALL


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.enableDisableBtnConn = None
        self.startStopBtnConn = None

    def disableUnit(self, name: str):
        cmd = ["systemctl", "disable","--", name]
        subprocess.run(cmd, shell=False, stdout=subprocess.PIPE)
        onRowSelected()

    def enableUnit(self, name: str):
        cmd = ["systemctl", "enable","--" , name]
        subprocess.run(cmd, shell=False, stdout=subprocess.PIPE)
        onRowSelected()

    def startUnit(self, name: str):
        cmd = ["systemctl", "start","--" , name]
        subprocess.run(cmd, shell=False, stdout=subprocess.PIPE)
        onRowSelected()
    def stopUnit(self, name: str):
        cmd = ["systemctl", "stop","--" , name]
        subprocess.run(cmd, shell=False, stdout=subprocess.PIPE)
        onRowSelected()


def loadListOfUnits(type: UnitType = UnitType.ALL) -> dict:
    cmd = ["systemctl", "list-unit-files"] if type == UnitType.ALL else ["systemctl", "list-unit-files", f"--type={type.value}"]
    cmdOutput = str(subprocess.run(cmd, shell=False, stdout=subprocess.PIPE).stdout)
    listedOutput = " ".join(cmdOutput.split()).split("\\n")
    filtredOutput = list(map(str.strip, listedOutput))
    listOfUnits = list(map(lambda x: x.split()[0::], filtredOutput))[1:-3]
    result = dict()
    for i in listOfUnits:
        result[i[0]] = i[1:3]
    result = dict(sorted(result.items()))
    return result


def placeDataIntoTable(data: dict, tableWidget: QTableWidget):
    tableWidget.setRowCount(len(data))
    for i, item in enumerate(data):
        tableWidget.setItem(i, 0, QTableWidgetItem(item))


def getUnitPath(name: str) -> Union[str, None]:
    cmd = ["systemctl", "status", "--", name]
    cmdOut = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE)
    if cmdOut.returncode != 4:
        cmdOut = cmdOut.stdout
    else:
        return None
    try:
        return str(cmdOut).split("\\n")[1].strip().split("(")[1].split(";")[0]
    except:
        return None


def getAutoRunStatus(name: str) -> str:
    cmd = ["systemctl", "status", "--", name]
    cmdOut = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE).stdout
    result = str(cmdOut).split("\\n")[1].strip().split(';')[1].strip().split(')')[0]
    return result

def getStateStatus(name: str) -> str:
    cmd = ["systemctl", "status", "--", name]
    cmdOut = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE).stdout
    result = str(cmdOut).split("\\n")[2].strip().split()[1]
    return result

def getSectionElements(filePath: str, section: FileSections) -> Union[list, None]:
    with open(filePath) as f:
        data = f.read().strip().split('\n')
        data = list(filter(lambda x: x != '', data))
        data = list(filter(lambda x: x[0] != '#', data))
        try:
            a = data.index(section.value)
        except:
            return None
        b = len(data)
        sections = [i.value for i in FileSections]
        sections.remove(section.value)
        for item in sections:
            try:
                t = data.index(item)
                if a < t < b:
                    b = t
            except:
                continue
        return data[a + 1:b]


def getUnitDataFromFile(data: list) -> dict:
    pass


def onLoad():
    global units
    units = loadListOfUnits()
    placeDataIntoTable(units, widget.ui.tableWidget)


def onComboBoxChanged():
    global currentType, units
    strCurrentType = widget.ui.comboBox.currentText()
    currentType = UnitType.ALL if strCurrentType == "All" else UnitType(strCurrentType.lower())
    units = loadListOfUnits(currentType)
    placeDataIntoTable(units, widget.ui.tableWidget)

    onRowSelected()


def onRefreshButtonPressed():
    global currentType, units
    units = loadListOfUnits(currentType)
    placeDataIntoTable(units, widget.ui.tableWidget)


def clearMoreLabels():
    widget.ui.labelMoreAfter.setText('')
    widget.ui.labelMoreBefore.setText('')
    widget.ui.labelMoreRequires.setText('')
    widget.ui.labelMoreWants.setText('')
    widget.ui.labelMoreConflicts.setText('')
    widget.ui.labelMoreAutorun.setText('')



def onRowSelected():
    clearMoreLabels()

    # Меняю описание юнита
    selectedRow = widget.ui.tableWidget.selectedItems()
    widget.ui.labelMoreName.setText(selectedRow[0].text())
    # widget.ui.labelMoreDescription.setText(selectedRow[4].text())
    unitPath=getUnitPath(selectedRow[0].text())
    if unitPath:
        sectionElements = getSectionElements(unitPath, FileSections.UNIT)
        try:
            descriptionText = list(filter(lambda x: x.startswith('Description='), sectionElements))
            descriptionText = descriptionText[0][12::] if descriptionText else None
            widget.ui.labelMoreDescription.setText(descriptionText)
        except:
            pass
        try:
            afterText = list(filter(lambda x: x.startswith('After='), sectionElements))
            afterText = afterText[0][6::] if afterText else None
            widget.ui.labelMoreAfter.setText(afterText)
        except:
            pass
        try:
            beforeText = list(filter(lambda x: x.startswith('Before='), sectionElements))
            beforeText = beforeText[0][7::] if beforeText else None
            widget.ui.labelMoreBefore.setText(beforeText)
        except:
            pass
        try:
            requiresText = list(filter(lambda x: x.startswith('Requires='), sectionElements))
            requiresText = requiresText[0][9::] if requiresText else None
            widget.ui.labelMoreRequires.setText(requiresText)
        except:
            pass
        try:
            wantsText = list(filter(lambda x: x.startswith('Wants='), sectionElements))
            wantsText = wantsText[0][6::] if wantsText else None
            widget.ui.labelMoreWants.setText(wantsText)
        except:
            pass
        try:
            conflictsText = list(filter(lambda x: x.startswith('Conflicts='), sectionElements))
            conflictsText = conflictsText[0][10::] if conflictsText else None
            widget.ui.labelMoreConflicts.setText(conflictsText)
        except:
            pass

    # Меняю действие кнопок enable/disable
    autorunStatus = getAutoRunStatus(selectedRow[0].text())
    if autorunStatus == 'enabled':
        widget.ui.enableDisableButton.setEnabled(True)
        widget.ui.enableDisableButton.setText('disable')
        widget.ui.labelMoreAutorun.setText('enabled')

        try:widget.ui.enableDisableButton.pressed.disconnect(widget.enableDisableBtnConn)
        except: pass
        widget.enableDisableBtnConn = lambda: widget.disableUnit(selectedRow[0].text())
        widget.ui.enableDisableButton.pressed.connect(widget.enableDisableBtnConn)
    elif autorunStatus == 'disabled':
        widget.ui.enableDisableButton.setEnabled(True)
        widget.ui.enableDisableButton.setText('enable')
        widget.ui.labelMoreAutorun.setText('disabled')

        try: widget.ui.enableDisableButton.pressed.disconnect(widget.enableDisableBtnConn)
        except: pass
        widget.enableDisableBtnConn = lambda: widget.enableUnit(selectedRow[0].text())
        widget.ui.enableDisableButton.pressed.connect(widget.enableDisableBtnConn)
    else:
        widget.ui.enableDisableButton.setEnabled(False)
        widget.ui.enableDisableButton.setText('')
        try: widget.ui.enableDisableButton.pressed.disconnect(widget.enableDisableBtnConn)
        except: pass


    # Меняю действие кнопок start/stop
    activeStatus = getStateStatus(selectedRow[0].text())
    if activeStatus == 'active':
        widget.ui.startStopButton.setEnabled(True)
        widget.ui.startStopButton.setText('stop')
        widget.ui.labelMoreState.setText('active')
        try:
            widget.ui.startStopButton.pressed.disconnect(widget.startStopBtnConn)
        except:
            pass
        widget.startStopBtnConn = lambda: widget.stopUnit(selectedRow[0].text())
        widget.ui.startStopButton.pressed.connect(widget.startStopBtnConn)
    elif activeStatus == 'inactive':
        widget.ui.startStopButton.setEnabled(True)
        widget.ui.startStopButton.setText('start')
        widget.ui.labelMoreState.setText('inactive')
        try:
            widget.ui.startStopButton.pressed.disconnect(widget.startStopBtnConn)
        except:
            pass
        widget.startStopBtnConn = lambda: widget.startUnit(selectedRow[0].text())
        widget.ui.startStopButton.pressed.connect(widget.startStopBtnConn)
    else:
        widget.ui.startStopButton.setEnabled(False)
        widget.ui.startStopButton.setText('')
        widget.ui.startStopButton.pressed.disconnect(widget.startStopBtnConn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    onLoad()
    widget.ui.comboBox.currentIndexChanged.connect(onComboBoxChanged)
    widget.ui.refreshButton.pressed.connect(onRefreshButtonPressed)
    widget.ui.tableWidget.itemSelectionChanged.connect(onRowSelected)
    widget.show()

    sys.exit(app.exec())
