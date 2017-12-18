from Expressions.TermParser import TermParser as TP


class ExpressionParser(object):
    """
    parse jack expression to xml
    """
    term = TP()
    ops = ["+", "-", "*", "/", "&", "|", "<", ">", "="]

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse an expression from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an expression
        """
        self.term.run(text_tokens, lexical_writer)  # parse first term
        while text_tokens.get_token() in self.ops:
            lexical_writer.write(text_tokens.get_token(), "symbol")  # write operand
            text_tokens.next()
            self.term.run(text_tokens, lexical_writer)  # parse next term
        return True
