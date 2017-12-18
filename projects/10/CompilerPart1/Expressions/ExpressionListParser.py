class ExpressionListParser(object):
    """
    parse jack expression list to xml
    """

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse an expression list from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an expression list
        """
        from Expressions.ExpressionParser import ExpressionParser as EP
        expression_parser = EP()

        if text_tokens.get_token() == ")":
            return True
        expression_parser.run(text_tokens, lexical_writer)
        while text_tokens.get_token() == ",":
            expression_parser.run(text_tokens, lexical_writer)
            text_tokens.next()
        return True
