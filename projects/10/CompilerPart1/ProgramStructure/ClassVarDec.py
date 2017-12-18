class ClassVarDec(object):
    """
    parse class variable declarations
    """
    FIELD_STATIC = "keyword"
    VAR_NAME = "identifier"

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        run over the code and convert class member to appropriate xml tags
        :param text_tokens: given code
        :param lexical_writer: writer of xml
        :return: null
        """
        while self.run_line(text_tokens, lexical_writer):
            continue

    def run_line(self, text_tokens, lexical_writer):
        """
        run a specific line of code to check for class member and parse it
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is variable deceleration
        """
        a = text_tokens.get_token()
        if text_tokens.get_token() != "static" and text_tokens.get_token() != \
                "field":
            return False
        lexical_writer.write(text_tokens.get_token(), self.FIELD_STATIC)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token())
        text_tokens.next()

        while True:
            lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
            text_tokens.next()
            if text_tokens.get_token() != ",":
                break

        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        return True
