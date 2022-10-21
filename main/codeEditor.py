from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPlainTextEdit, QFileDialog, QDialog, QMessageBox
from compilerWin import Ui_compilerWin
from dialog import Ui_Dialog
from PySide6.QtCore import Slot
from platform import platform, system 
import sys
import os
import subprocess

# ToDo
# Error Message Extraction                              Done
# Save Indigator Implimentation                         Done
# Not Save Message Generation ( Dialogue Box)           Done
# Modify For Windows                                    
# Font Control
# System Font Control
# Line Number Field Implementation
# Menu Activation


class ErrorLog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.setStandardButtons(self.ui.buttonBox.StandardButton.Ok)

    # def closeWin(self):
    #     self.close()


class LineNumberField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumWidth(40)


class EditorField(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberField = LineNumberField(self)


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = MyUI()
        self.errorLogWin = ErrorLog()
        self.ui = Ui_compilerWin()
        self.ui.setupUi(self)
        self.ui.tabWidget.removeTab(1)
        self.ui.tabWidget.removeTab(0)
        self.openedFileList = []
        self.openedFileSaveList = []

        # Button Connection
        self.ui.newBtn.clicked.connect(self.createNewFile)
        self.ui.openBtn.clicked.connect(self.openFile)
        self.ui.saveBtn.clicked.connect(self.saveFile)
        self.ui.compileBtn.clicked.connect(self.compileFile)
        self.ui.executeBtn.clicked.connect(self.executeFile)
        self.ui.errorLogBtn.clicked.connect(self.errorLogOpen)
        self.ui.tabWidget.tabCloseRequested.connect(self.tabCloseBtn)

    def errorLogOpen(self):
        self.errorLogWin.show()

    def tabCloseBtn(self, index):

        if self.openedFileSaveList[index]:
            self.ui.tabWidget.removeTab(index)
            del self.openedFileList[index]
            del self.openedFileSaveList[index]
        else:
            m = QMessageBox.question(
                self, "File Not Save",
                "This File is not saved.\n Do you Want to save it ?",
                buttons=QMessageBox.StandardButtons(
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel),
                defaultButton=QMessageBox.StandardButton.Cancel)
            if m == QMessageBox.StandardButton.Yes:
                self.saveFile(index)
            elif m == QMessageBox.StandardButton.No:
                self.ui.tabWidget.removeTab(index)
                del self.openedFileList[index]
                del self.openedFileSaveList[index]

    def createNewFile(self):
        widget = EditorField()
        self.ui.tabWidget.addTab(
            widget, f"untitled{self.ui.tabWidget.count()-len(self.openedFileList)}")
        self.openedFileList.append(None)
        self.openedFileSaveList.append(False)

    # For only testing 
    # test_dir = os.
    def openFile(self):
        basedir =os.getcwd()
        os.path.join(basedir , 'testdir')
        filePath = QFileDialog.getOpenFileName(
            self, 'open file',os.path.join(basedir , 'testdir'))[0]

        if filePath != '':
            filename = os.path.basename(filePath)
            f = open(filePath, "r")
            content = f.read()
            widget = EditorField()
            widget.setPlainText(content)
            self.ui.tabWidget.addTab(widget, filename)
            self.openedFileList.append(filePath)
            self.openedFileSaveList.append(True)

    def saveFile(self, currentIndex=None):
        # if self.is_not_save(self):

        # Save
        if currentIndex != None:
            currentIndex = self.ui.tabWidget.currentIndex()
        if currentIndex == -1:
            return

        content = self.ui.tabWidget.currentWidget().toPlainText()
        print(content)
        filePath = self.openedFileList[currentIndex]
        if not self.openedFileSaveList[currentIndex]:
            print(filePath)
            if bool(filePath):
                f = open(filePath, "w")
                f.write(content)
                print(currentIndex)
                f.close()
            else:
                filePath = QFileDialog.getSaveFileName(
                    self, "Save F:xile", "/home/jana/untitled.png", "Text files (*.*)")[0]
                print(filePath)
                f = open(filePath, 'w')
                f.write(content)
                f.close()
                filename = os.path.basename(filePath)
                # currentIndex = self.ui.tabWidget.currentIndex()
                self.ui.tabWidget.setTabText(currentIndex, filename)
                self.openedFileList[currentIndex] = filePath
                self.openedFileSaveList[currentIndex] = True
                print(currentIndex, "From Save")
        # For Now else 
        else :
            if bool(filePath):
                f = open(filePath, "w")
                f.write(content)
                print(currentIndex)
                f.close()

    def is_not_save(self):
        return True

    def compileFile(self):
        lang_to_extension = {'Python': 'py',
                             'C': 'c', 'C++': 'cpp', 'Java': 'java'}
        currentFileIndex = self.ui.tabWidget.currentIndex()
        lang = self.ui.selectBtn.currentText()
        try:
            if self.openedFileSaveList[currentFileIndex]:
                path = self.openedFileList[currentFileIndex]
                name, extension = os.path.splitext(path)
                extension = extension[1:]
                if extension == lang_to_extension[lang]:
                    if extension == 'py':
                        m = QMessageBox.information(
                            self, 'Compiletion Stoped', f"Python does not required any compilation. ")
                    elif extension == 'java':
                        # os.system(f"javac {path}")
                        error = subprocess.run(['javac', path],
                                               stderr=subprocess.PIPE).stderr
                        if error:
                            # print("Open Dialog Box to Show error")
                            self.errorLogWin.ui.label.setText(
                                str(error.decode('utf-8')))
                    elif extension == 'c':
                        # os.system(f" {path} -o {name}.out ")
                        if (system() == 'Windows'):
                            error = subprocess.run(['gcc', path, '-o', name+'.exe'],
                                                stderr=subprocess.PIPE).stderr
                        else:
                            error = subprocess.run(['gcc', path, '-o', name+'.out'],
                                                stderr=subprocess.PIPE).stderr
                        if error:
                            # print("Open Dialog Box to Show error")
                            self.errorLogWin.ui.label.setText(
                                str(error.decode('utf-8')))
                    elif extension == 'cpp':
                        # os.system(f"g++ {path} -o {name}.out ")
                        error = subprocess.run(['g++', path, '-o', name+'.out'],
                                               stderr=subprocess.PIPE).stderr
                        if error:
                            # print("Open Dialog Box to Show error")
                            self.errorLogWin.ui.label.setText(
                                str(error.decode('utf-8')))
                else:
                    QMessageBox.information(
                        self, 'Compiletion Stoped', f"selected Language is {lang}.\nplease check the file extension")
            else:
                QMessageBox.information(
                    self, 'Compiletion Stoped', f"Please Save the file before Compile.")
        except:
            pass

    def executeFile(self):
        lang_to_extension = {'Python': 'py',
                             'C': 'c', 'C++': 'cpp', 'Java': 'java'}
        currentFileIndex = self.ui.tabWidget.currentIndex()
        lang = self.ui.selectBtn.currentText()
        try:
            if self.openedFileSaveList[currentFileIndex]:
                path = self.openedFileList[currentFileIndex]
                name, extension = os.path.splitext(path)
                dir_name = os.path.dirname(path)
                absolute_name = os.path.basename(name)                
                extension = extension[1:]
                if system() == 'Windows':
                    if extension == lang_to_extension[lang]:
                        if extension == 'py':
                            os.system(f'start powershell -Command "python {path};cat"')
                            # subprocess.call(f'start /wait python {path}; read x', shell=True)
                        elif extension == 'java':
                            # subprocess.call(f'start /wait javac {path}; read x', shell=True)
                            os.system(f'start powershell -Command "cd {dir_name};java {absolute_name};cat"')
                        elif extension == 'c' or extension == 'cpp':
                            # subprocess.call(f'start /wait  {path}; read x', shell=True)
                            os.system(f'start powershell -Command "{name}.exe;cat"')

                    else:
                        QMessageBox.information(
                            self, 'Compiletion Stoped', f"selected Language is {lang}.\nplease check the file extension")
                else :
                    if extension == lang_to_extension[lang]:
                        if extension == 'py':

                            subprocess.call(
                                ['xterm', '-e', f'python {path};read z'])
                            # subprocess.call(['xterm', '-e', f'python {path};read z'])
                        elif extension == 'java':
                            subprocess.call(
                                ['xterm', '-e', f'cd {dir_name};java {name};read z'])
                            # subprocess.call(['xterm', '-e', f'java {name};read z'])
                        elif extension == 'c' or extension == 'cpp':
                            subprocess.call(['xterm', '-e', f"{name}.out; read z"])
                            # subprocess.call(['xterm', '-e', f"{name}.out; read z"])

                    else:
                        QMessageBox.information(
                            self, 'Compiletion Stoped', f"selected Language is {lang}.\nplease check the file extension")
            else:
                QMessageBox.information(
                    self, 'Compiletion Stoped', f"Please Save the file before Compile.")
        except:
            pass


def main():
    app = QApplication(sys.argv)

    # win = QMessageBox()
    win = CodeEditor()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
