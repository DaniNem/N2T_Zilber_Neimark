from ProgramStructure.ClassVarDec import ClassVarDec as CVD
from ProgramStructure.SubRoutineDec import SubRoutineDec as SRT
from LexicalWriter import LexicalWriter
from JackTokenizer.JackTokenizer import JackTokenizer as JT


class ClassParser(object):
    var_dec = CVD()
    sub_routine_dec = SRT()

    def __init__(self, tokens, lexical):
        self._tokens = tokens
        self._lexical = lexical

    def run(self):
        self._lexical.write(self._tokens.get_token(), "keyword")
        self._tokens.next()
        self._lexical.write(self._tokens.get_token(), "identifier")
        self._tokens.next()
        self._lexical.write(self._tokens.get_token(), "symbol")
        self._tokens.next()
        self.var_dec.run(self._tokens, self._lexical)
        self.sub_routine_dec.run(self._tokens, self._lexical)
        self._lexical.write(self._tokens.get_token(), "symbol")
        self._tokens.next()


if __name__ == "__main__":
    writer = LexicalWriter()
    tokenizer = JT(r"C:\Users\Admin\Desktop\nand2tetris\projects\09\JumpThingy\Point.jack")
    a = ClassParser(tokenizer, writer)
    a.run()
