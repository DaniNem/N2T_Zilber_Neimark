from ExpressionParser import ExpressionParser as EP


class StatementsParser(object):
    expression_parser = EP()
    DO = "keyword"
    IF = "keyword"
    ELSE = "keyword"
    LET = "keyword"
    RETURN = "keyword"
    WHILE = "keyword"
    VAR_NAME = "identifier"

    def __init__(self):
        pass

    def run(self, text_tokens, lexical_writer):
        more_statements = True
        while more_statements:
            a = self.run_do(text_tokens, lexical_writer)
            b = self.run_if(text_tokens, lexical_writer)
            c = self.run_let(text_tokens, lexical_writer)
            d = self.run_return(text_tokens, lexical_writer)
            e = self.run_while(text_tokens, lexical_writer)
            more_statements = a or b or c or d or e
        return True

    def run_do(self, text_tokens, lexical_writer):
        """
         parse a do line from jack to xml
         :param text_tokens: given jack code
         :param lexical_writer: xml writer
         :return: true if the given line is indeed a do line
         """
        if text_tokens.get_token() != "do":
            return False
        lexical_writer.openSub("doStatement")
        lexical_writer.write(text_tokens.get_token(), self.DO)  # parse do statement
        text_tokens.next()
        self.expression_parser.run_subroutine_call(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # parse semi colon
        text_tokens.next()
        lexical_writer.closeSub()
        return True

    def run_if(self, text_tokens, lexical_writer):
        """
        parse a if line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an if line
        """
        if text_tokens.get_token() != "if":
            return False
        lexical_writer.openSub("ifStatement")
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
        self.run(text_tokens, lexical_writer)  # parse statements
        # in if body
        lexical_writer.write(text_tokens.get_token, "symbol")  # closing brackets
        text_tokens.next()
        if text_tokens.get_token() != "else":
            return True
        lexical_writer.write(text_tokens.get_token, "symbol")  # opening brackets
        text_tokens.next()
        self.run(text_tokens, lexical_writer)  # parse statements
        # in else body
        lexical_writer.write(text_tokens.get_token, "symbol")  # closing brackets
        text_tokens.next()
        lexical_writer.closeSub()
        return True

    def run_let(self, text_tokens, lexical_writer):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a let line
        """
        if text_tokens.get_token() != "let":
            return False
        lexical_writer.openSub("letStatement")
        lexical_writer.write(text_tokens.get_token(), self.LET)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
        text_tokens.next()
        if text_tokens.get_token() == "[":  # check if var_name is an array
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            self.expression_parser.run(text_tokens, lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # get equal sign
        text_tokens.next()
        self.expression_parser.run(text_tokens, lexical_writer)  # parse expression
        #  after equal sign
        lexical_writer.write(text_tokens.get_token(), "symbol")  # semi colon sign
        text_tokens.next()
        lexical_writer.closeSub()
        return True

    def run_return(self, text_tokens, lexical_writer):
        """
        parse a return line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a return line
        """
        if text_tokens.get_token() != "return":
            return False
        lexical_writer.openSub("returnStatement")
        lexical_writer.write(text_tokens.get_token(), self.RETURN)  # parse return
        # statement
        text_tokens.next()
        if text_tokens.get_token() != ";":
            self.expression_parser.run(text_tokens, lexical_writer)
            # parse expression
        lexical_writer.write(text_tokens.get_token(), "symbol")  # parse semi colon
        text_tokens.next()
        lexical_writer.closeSub()
        return True

    def run_while(self, text_tokens, lexical_writer):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a let line
        """
        if text_tokens.get_token() != "while":
            return False
        lexical_writer.openSub("whileStatement")
        lexical_writer.write(text_tokens.get_token(), self.WHILE)  # parse while
        # statement
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        self.expression_parser.run(text_tokens, lexical_writer)  # parse while
        # expression
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening
        # bracket (body)
        text_tokens.next()
        self.run(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        #  (body)
        text_tokens.next()
        lexical_writer.closeSub()
        return True
