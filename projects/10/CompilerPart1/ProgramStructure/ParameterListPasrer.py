class ParameterListParser(object):
    """
    parse a given subroutine deceleration to appropriate xml text
    """
    PARAM = "identifier"
    COMA = "symbol"

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
          go over the text and parse method's parameter list to xml text
          :param text_tokens: give text
          :param lexical_writer: xml writer
          :return: null
          """
        while True:
            if text_tokens.get_token() == ")":
                return
            lexical_writer.write(text_tokens.get_token())
            text_tokens.next()
            a = text_tokens.get_token()
            lexical_writer.write(text_tokens.get_token(), self.PARAM)
            text_tokens.next()
            a = text_tokens.get_token()
            if text_tokens.get_token() != ",":
                return
            lexical_writer.write(text_tokens.get_token(), self.COMA)
            text_tokens.next()
