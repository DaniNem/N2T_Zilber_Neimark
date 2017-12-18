from Expressions.ExpressionParser import ExpressionParser as EP


class WhileStatementParser(object):
    """
    parse jack while line to xml
    """
    WHILE = "keyword"
    expression_parser = EP()

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a let line
        """
        from Statements.StatementsParser import StatementsParser as SP
        statements_parser = SP()

        if text_tokens.get_token() != "while":
            return False
        lexical_writer.write(text_tokens.get_token(), self.WHILE)  # parse while
        # statement
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        self.expression_parser.run(text_tokens, lexical_writer)  # parse while
        # expression
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening
        # bracket (body)
        text_tokens.next()
        statements_parser.run(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        #  (body)
        text_tokens.next()
        return True
