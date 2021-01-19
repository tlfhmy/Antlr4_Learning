from antlr4 import InputStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):

    def __init__(self):
        super(EvalVisitor, self).__init__()
        self.memory = {}

    def visitAssign(self, ctx:ExprParser.AssignContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    def visitPrintExpr(self, ctx:ExprParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx:ExprParser.IntContext):
        return int(ctx.INT().getText())

    def visitId(self, ctx:ExprParser.IdContext):
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        return 0

    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprParser.ADD:
            return left + right
        else:
            return left - right

    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visit(ctx.expr())

with open("t.expr") as f:
    inp = InputStream(f.read())
    lexer = ExprLexer(inp)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

    evalu = EvalVisitor()
    evalu.visit(tree)