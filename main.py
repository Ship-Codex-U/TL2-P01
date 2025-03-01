import sys
import os

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.compiler = Compiler()

        self.ui.button_compile.clicked.connect(self.codeCompile)

        self.show()

    @Slot()
    def codeCompile(self):
        resultTokens = ""

        self.ui.output_messages.clear()
        self.ui.output_result.clear()

        code = self.ui.input_code.toPlainText()

        tokensFound, lexicalErrors = self.compiler.lexicalAnalyser(code)

        if lexicalErrors:
            for i, error in enumerate(lexicalErrors):
                self.showOutputMessage(f'{str(i + 1)}) {error}', QColor(230,25,25))
        else:
            self.showOutputMessage("Lexical analysis completed with no errors", QColor("green"))      

        for token in tokensFound:
            resultTokens += "{:<{}}{}\n".format(token[0], 30, token[1])        
        self.ui.output_result.setPlainText(resultTokens)


    def showOutputMessage(self, text, color):
        cursor = self.ui.output_messages.textCursor()
        cursor.movePosition(QTextCursor.End)

        char_format = QTextCharFormat()
        char_format.setForeground(color)

        cursor.setCharFormat(char_format)
        cursor.insertText(text + "\n")

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())