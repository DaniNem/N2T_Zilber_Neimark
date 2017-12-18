from Expressions.ExpressionParser import ExpressionParser as EP


class ReturnStatementParser(object):
    """
    parse return line from jack to xml
    """
    expression_parser = EP()
    RETURN = "keyword"

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse a return line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a return line
        """
        if text_tokens.get_token() != "return":
            return False
        lexical_writer.write(text_tokens.get_token(), self.RETURN)  # parse return
        # statement
        text_tokens.next()
        if text_tokens.get_token() != ";":
            self.expression_parser.run(text_tokens, lexical_writer)
            # parse expression
        lexical_writer.write(text_tokens.get_token(), "symbol")  # parse semi colon
        text_tokens.next()
        return True
