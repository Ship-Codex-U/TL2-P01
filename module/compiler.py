from module.lexicalanalizer import LexicalAnalizer

class Compiler:
    def __init__(self):
        self.__code = ""

    def lexicalAnalyser(self, code : str) -> tuple[list, list]:
        lexicalAnalizer = LexicalAnalizer()
        [tokensFound, errors] = lexicalAnalizer.analyze(code)
        
        return (tokensFound, errors)
