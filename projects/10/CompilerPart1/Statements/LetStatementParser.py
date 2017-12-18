from Expressions.ExpressionParser import ExpressionParser as EP


class LetStatementParser(object):
    LET = "keyword"
    VAR_NAME = "identifier"
    expression_parser = EP()

    def __init__(self):
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a let line
        """
        if text_tokens.get_token() != "let":
            return False
        lexical_writer.write(text_tokens.get_token(), self.LET)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
        text_tokens.next()
        if text_tokens.get_token() == "[":  # check if var_name is an array
            lexical_writer.write(text_tokens.get_token, "symbol")
            text_tokens.next()
            self.expression_parser.run(text_tokens, lexical_writer)
            lexical_writer.write(text_tokens.get_token, "symbol")
            text_tokens.next()
        lexical_writer.write(text_tokens.get_token, "symbol")  # get equal sign
        text_tokens.next()
        self.expression_parser.run(text_tokens, lexical_writer)  # parse expression
        #  after equal sign
        lexical_writer.write(text_tokens.get_token, "symbol")  # semi colon sign
        text_tokens.next()
        return True
