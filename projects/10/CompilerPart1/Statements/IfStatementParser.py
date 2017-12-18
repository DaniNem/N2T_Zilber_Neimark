from Expressions.ExpressionParser import ExpressionParser as EP


class IfStatementParser(object):
    """
    parse jack if statement to xml
    """
    IF = "keyword"
    ELSE = "keyword"
    expression_parser = EP()

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse a if line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an if line
        """
        from Statements.StatementsParser import StatementsParser as SP
        statements_parser = SP()

        if text_tokens.get_token() != "if":
            return False
        lexical_writer.write(text_tokens.get_token(), self.IF)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token, "symbol")  # opening brackets
        text_tokens.next()
        self.expression_parser.run(text_tokens, lexical_writer)  # parse expression
        # in brackets
        lexical_writer.write(text_tokens.get_token, "symbol")  # closing brackets
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token, "symbol")  # opening brackets
        text_tokens.next()
        statements_parser.run(text_tokens, lexical_writer)  # parse statements
        # in if body
        lexical_writer.write(text_tokens.get_token, "symbol")  # closing brackets
        text_tokens.next()
        if text_tokens.get_token() != "else":
            return True
        lexical_writer.write(text_tokens.get_token, "symbol")  # opening brackets
        text_tokens.next()
        self.statements_parser.run(text_tokens, lexical_writer)  # parse statements
        # in else body
        lexical_writer.write(text_tokens.get_token, "symbol")  # closing brackets
        text_tokens.next()
        return True
