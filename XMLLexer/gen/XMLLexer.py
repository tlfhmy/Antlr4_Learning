# Generated from D:/github/Antlr4_Learning/XMLLexer\XMLLexer.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("b\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3\'\n\3\f\3")
        buf.write("\16\3*\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\6\4\64\n\4")
        buf.write("\r\4\16\4\65\3\4\3\4\3\5\6\5;\n\5\r\5\16\5<\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\7\tL\n\t\f")
        buf.write("\t\16\tO\13\t\3\t\3\t\3\n\3\n\3\n\7\nV\n\n\f\n\16\nY\13")
        buf.write("\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\4(M\2\16\4\3\6")
        buf.write("\4\b\5\n\6\f\7\16\b\20\t\22\n\24\13\26\f\30\2\32\2\4\2")
        buf.write("\3\7\3\2c|\4\2((>>\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\62")
        buf.write(";\2d\2\4\3\2\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n\3\2\2\2\3")
        buf.write("\f\3\2\2\2\3\16\3\2\2\2\3\20\3\2\2\2\3\22\3\2\2\2\3\24")
        buf.write("\3\2\2\2\3\26\3\2\2\2\4\34\3\2\2\2\6 \3\2\2\2\b\61\3\2")
        buf.write("\2\2\n:\3\2\2\2\f>\3\2\2\2\16B\3\2\2\2\20G\3\2\2\2\22")
        buf.write("I\3\2\2\2\24R\3\2\2\2\26Z\3\2\2\2\30^\3\2\2\2\32`\3\2")
        buf.write("\2\2\34\35\7>\2\2\35\36\3\2\2\2\36\37\b\2\2\2\37\5\3\2")
        buf.write("\2\2 !\7>\2\2!\"\7#\2\2\"#\7/\2\2#$\7/\2\2$(\3\2\2\2%")
        buf.write("\'\13\2\2\2&%\3\2\2\2\'*\3\2\2\2()\3\2\2\2(&\3\2\2\2)")
        buf.write("+\3\2\2\2*(\3\2\2\2+,\7/\2\2,-\7/\2\2-.\7@\2\2./\3\2\2")
        buf.write("\2/\60\b\3\3\2\60\7\3\2\2\2\61\63\7(\2\2\62\64\t\2\2\2")
        buf.write("\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2")
        buf.write("\2\66\67\3\2\2\2\678\7=\2\28\t\3\2\2\29;\n\3\2\2:9\3\2")
        buf.write("\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\13\3\2\2\2>?\7@\2")
        buf.write("\2?@\3\2\2\2@A\b\6\4\2A\r\3\2\2\2BC\7\61\2\2CD\7@\2\2")
        buf.write("DE\3\2\2\2EF\b\7\4\2F\17\3\2\2\2GH\7?\2\2H\21\3\2\2\2")
        buf.write("IM\7$\2\2JL\13\2\2\2KJ\3\2\2\2LO\3\2\2\2MN\3\2\2\2MK\3")
        buf.write("\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7$\2\2Q\23\3\2\2\2RW\5\30")
        buf.write("\f\2SV\5\30\f\2TV\5\32\r\2US\3\2\2\2UT\3\2\2\2VY\3\2\2")
        buf.write("\2WU\3\2\2\2WX\3\2\2\2X\25\3\2\2\2YW\3\2\2\2Z[\t\4\2\2")
        buf.write("[\\\3\2\2\2\\]\b\13\3\2]\27\3\2\2\2^_\t\5\2\2_\31\3\2")
        buf.write("\2\2`a\t\6\2\2a\33\3\2\2\2\n\2\3(\65<MUW\5\7\3\2\b\2\2")
        buf.write("\6\2\2")
        return buf.getvalue()


class XMLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INSIDE = 1

    OPEN = 1
    COMMENT = 2
    EntityRef = 3
    TEXT = 4
    CLOSE = 5
    SLASH_CLOSE = 6
    EQUALS = 7
    STRING = 8
    SlashName = 9
    S = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "INSIDE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'/>'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "OPEN", "COMMENT", "EntityRef", "TEXT", "CLOSE", "SLASH_CLOSE", 
            "EQUALS", "STRING", "SlashName", "S" ]

    ruleNames = [ "OPEN", "COMMENT", "EntityRef", "TEXT", "CLOSE", "SLASH_CLOSE", 
                  "EQUALS", "STRING", "SlashName", "S", "ALPHA", "DIGIT" ]

    grammarFileName = "XMLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


