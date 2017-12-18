from JackTokenizer import JackTokenizer as JT
from LexicalWriter import LexicalWriter
from StatementsParser import StatementsParser as SP


class ClassParser(object):
    statements = SP()
    FIELD_STATIC = "keyword"
    VAR_NAME = "identifier"
    METHOD_NAME = "identifier"
    OPEN_BRACKET = "symbol"
    CLOSE_BRACKET = "symbol"
    PARAM = "identifier"
    COMA = "symbol"
    VAR = "keyword"

    def __init__(self, tokens, lexical):
        self._tokens = tokens
        self._lexical = lexical

    def run(self):
        self._lexical.write(self._tokens.get_token(), "keyword")
        self._tokens.next()
        self._lexical.write(self._tokens.get_token(), "identifier")
        self._tokens.next()
        self._lexical.write(self._tokens.get_token(), "symbol")
        self._tokens.next()
        self._lexical.openSub("classVarDec")
        self.run_class_var_dec(self._tokens, self._lexical)
        self._lexical.closeSub()
        self._lexical.openSub("subroutineDec")
        self.run_subroutine_dec(self._tokens, self._lexical)
        self._lexical.closeSub()
        self._lexical.write(self._tokens.get_token(), "symbol")
        self._tokens.next()

    def run_class_var_dec(self, text_tokens, lexical_writer):
        """
        run over the code and convert class member to appropriate xml tags
        :param text_tokens: given code
        :param lexical_writer: writer of xml
        :return: null
        """
        while self.run_var_dec_line(text_tokens, lexical_writer):
            continue

    def run_var_dec_line(self, text_tokens, lexical_writer):
        """
        run a specific line of code to check for class member and parse it
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is variable deceleration
        """
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

    def run_subroutine_dec(self, text_tokens, lexical_writer):
        """
        go over the text and parse methods decelerations to xml text
        :param text_tokens: give text
        :param lexical_writer: xml writer
        :return: null
        """
        while self.run_subroutine_dec_line(text_tokens, lexical_writer):
            continue

    def run_subroutine_dec_line(self, text_tokens, lexical_writer):
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
        lexical_writer.write(text_tokens.get_token())
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.METHOD_NAME)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.OPEN_BRACKET)
        text_tokens.next()
        lexical_writer.openSub("parameterList")
        self.run_param_list(text_tokens, lexical_writer)
        lexical_writer.closeSub()
        lexical_writer.openSub("subroutineBody")
        lexical_writer.write(text_tokens.get_token(), self.CLOSE_BRACKET)
        lexical_writer.closeSub()
        text_tokens.next()
        self.run_subroutine_body(text_tokens, lexical_writer)
        return True

    def run_param_list(self, text_tokens, lexical_writer):
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
            lexical_writer.write(text_tokens.get_token(), self.PARAM)
            text_tokens.next()
            if text_tokens.get_token() != ",":
                return
            lexical_writer.write(text_tokens.get_token(), self.COMA)
            text_tokens.next()

    def run_subroutine_body(self, text_tokens, lexical_writer):
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        while self.run_var_dec(text_tokens, lexical_writer):
            continue
        lexical_writer.openSub("statements")
        self.statements.run(text_tokens, lexical_writer)
        lexical_writer.closeSub()
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        return

    def run_var_dec(self, text_tokens, lexical_writer):
        """
        convert variable deceleration to xml text
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is variable deceleration line
        """
        token = text_tokens.get_token()
        if token != "var":
            return False
        lexical_writer.openSub("varDec")
        lexical_writer.write(token, self.VAR)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token())  # write variable type
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
        text_tokens.next()
        while text_tokens.get_token() == ",":
            lexical_writer.write(text_tokens.get_token(), "symbol")  # write coma
            text_tokens.next()
            lexical_writer.write(text_tokens.get_token(), self.VAR_NAME)
            text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # write semi colon
        text_tokens.next()
        lexical_writer.closeSub()
        return True


if __name__ == "__main__":
    writer = LexicalWriter()
    tokenizer = JT(r"C:\nand2tetris\projects\10\ArrayTest\main.jack")
    a = ClassParser(tokenizer, writer)
    a.run()
    writer.writeXML(r"C:\nand2tetris\projects\10\CompilerPart1\ma_man.xml")
