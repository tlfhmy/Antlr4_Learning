from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
import ArrayInitLexer
import ArrayInitParser
import ArrayInitListener

input_1 = InputStream(input("Please enter: "))

lexer = ArrayInitLexer.ArrayInitLexer(input_1)

tokens = CommonTokenStream(lexer)

parser = ArrayInitParser.ArrayInitParser(tokens)

tree = parser.init()

walker = ParseTreeWalker()
walker.walk(ArrayInitListener.ArrayInitListener(),tree)

print(tree.toStringTree(recog=parser))