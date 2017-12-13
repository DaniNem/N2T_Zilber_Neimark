class VarDecParser(object):
    """
    parse variable deceleration statements
    """
    VAR = "keyword"
    VAR_NAME = "identifier"

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        convert variable deceleration to xml text
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is variable deceleration line
        """
        token = text_tokens.get_token()
        if token != "var":
            return False
        lexical_writer.write(token, self.VAR)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "fuck")  # write variable type
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
        text_tokens.next()
        while text_tokens.get_token() == ",":
            a = text_tokens.get_token()
            lexical_writer.write(text_tokens.get_token(), "symbol")  # write coma
            text_tokens.next()
            lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
            text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # write semi colon
        text_tokens.next()
        return True
