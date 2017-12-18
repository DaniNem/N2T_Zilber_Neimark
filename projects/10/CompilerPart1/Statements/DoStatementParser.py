from Expressions.SubRoutineCallParser import SubRoutineParser as SRP


class DoStatementParser(object):
    """
    parse do line from jack to xml
    """
    subroutine_parser = SRP()
    DO = "keyword"

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
         parse a do line from jack to xml
         :param text_tokens: given jack code
         :param lexical_writer: xml writer
         :return: true if the given line is indeed a do line
         """
        if text_tokens.get_token() != "do":
            return False
        lexical_writer.write(text_tokens.get_token(), self.DO)  # parse do statement
        text_tokens.next()
        self.subroutine_parser.run(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # parse semi colon
        text_tokens.next()
        return True
