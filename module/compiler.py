from module.lexicalanalizer import LexicalAnalizer
from module.parser import Parser

class Compiler:
    def __init__(self):
        self.__code = ""
        self.__tokensFound = []
        self.__tree = None

    def lexicalAnalyser(self, code : str) -> tuple[list, list]:
        lexicalAnalizer = LexicalAnalizer()
        [self.__tokensFound, errors] = lexicalAnalizer.analyze(code)

        
        return (self.__tokensFound, errors)
    
    def parser(self):
        parser = Parser(self.__tokensFound)

        [self.__tree, errors] = parser.parse()

        print(errors)
        return (self.__tree, errors[0] if errors else None)
        
