from ProgramStructure.VarDecParser import VarDecParser as VDP
from Statements.StatementsParser import StatementsParser as SP


class SubRoutineBody(object):
    var_dec = VDP()
    statements = SP()

    def __init__(self):
        pass

    def run(self, text_tokens, lexical_writer):
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        while self.var_dec.run(text_tokens, lexical_writer):
            continue
        self.statements.run(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        return
