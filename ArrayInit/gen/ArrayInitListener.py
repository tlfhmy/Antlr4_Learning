# Generated from D:/github/Antlr4_Learning/ArrayInit\ArrayInit.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArrayInitParser import ArrayInitParser
else:
    from ArrayInitParser import ArrayInitParser

# This class defines a complete listener for a parse tree produced by ArrayInitParser.
class ArrayInitListener(ParseTreeListener):

    # Enter a parse tree produced by ArrayInitParser#init.
    def enterInit(self, ctx:ArrayInitParser.InitContext):
        print('"', end="")
        pass

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx:ArrayInitParser.InitContext):
        print('"')
        pass


    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx:ArrayInitParser.ValueContext):
        print(chr(int(ctx.INT().getText())), end="")
        pass

    # Exit a parse tree produced by ArrayInitParser#value.
    def exitValue(self, ctx:ArrayInitParser.ValueContext):
        pass



del ArrayInitParser