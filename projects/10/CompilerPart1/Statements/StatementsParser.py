from Statements.DoStatementParser import DoStatementParser as DSP
from Statements.IfStatementParser import IfStatementParser as ISP
from Statements.LetStatementParser import LetStatementParser as LSP
from Statements.ReturnStatementParser import ReturnStatementParser as RSP
from Statements.WhileStatementParser import WhileStatementParser as WSP


class StatementsParser(object):
    do_statement = DSP()
    if_statement = ISP()
    let_statement = LSP()
    return_statement = RSP()
    while_statement = WSP()

    def __init__(self):
        pass

    def run(self, text_tokens, lexical_writer):
        more_statements = True
        while more_statements:
            a = self.do_statement.run(text_tokens, lexical_writer)
            b = self.if_statement.run(text_tokens, lexical_writer)
            c = self.let_statement.run(text_tokens, lexical_writer)
            d = self.return_statement.run(text_tokens, lexical_writer)
            e = self.while_statement.run(text_tokens, lexical_writer)
            more_statements = a or b or c or d or e
        return True
