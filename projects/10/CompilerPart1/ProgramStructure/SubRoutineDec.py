from ParameterListPasrer import ParameterListParser as PLP
from SubRoutineBody import SubRoutineBody as SRB


class SubRoutineDec(object):
    """
    parse a given subroutine deceleration to appropriate xml text
    """
    METHOD_NAME = "identifier"
    OPEN_BRACKET = "symbol"
    CLOSE_BRACKET = "symbol"

    param_list_parser = PLP()
    body_parser = SRB()

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        go over the text and parse methods decelerations to xml text
        :param text_tokens: give text
        :param lexical_writer: xml writer
        :return: null
        """
        while self.run_line(text_tokens, lexical_writer):
            continue

    def run_line(self, text_tokens, lexical_writer):
        """
        go over a specific method deceleration and parse to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is subroutine deceleration
        """
        name = text_tokens.get_token()
        if name != "constructor" and name != "function" and name != "method":
            return False
        lexical_writer.write(name, "keyword")
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "fuck")
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.METHOD_NAME)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.OPEN_BRACKET)
        text_tokens.next()
        self.param_list_parser.run(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), self.CLOSE_BRACKET)
        text_tokens.next()
        self.body_parser.run(text_tokens, lexical_writer)
        return True
