from StatementsParser import StatementsParser as SP
from SymbolTable import SymbolTable as ST

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

    def __init__(self, tokens, writer,lexical):
        """
        get text token and xml writer
        :param tokens:
        :param lexical:
        """
        self._tokens = tokens
        self._lexical = lexical
        self._writer = writer
        self._st = ST()

    def run(self):
        """
        parse jack file
        :return:
        """
        self._lexical.write(self._tokens.get_token(), "keyword")  # class keyword
        self._tokens.next()
        self._lexical.write(self._tokens.get_token(), "identifier")  # class name
        self._tokens.next()
        self._lexical.write(self._tokens.get_token(), "symbol")
        self._tokens.next()
        self.run_class_var_dec(self._tokens,self._writer,self._lexical)  # class variables
        self.run_subroutine_dec(self._tokens,self._writer ,self._lexical)  # class subroutines
        self._lexical.write(self._tokens.get_token(), "symbol")
        self._tokens.next()

    def run_class_var_dec(self, text_tokens, writer,lexical_writer):
        """
        run over the code and convert class member to appropriate xml tags
        :param text_tokens: given code
        :param lexical_writer: writer of xml
        :return: null
        """
        while self.run_var_dec_line(text_tokens,writer, lexical_writer):
            continue
        return True

    def run_var_dec_line(self, text_tokens, writer,lexical_writer):
        """
        run a specific line of code to check for class member and parse it
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is variable deceleration
        """
        var_segment = text_tokens.get_token()
        if var_segment != "static" and var_segment != \
                "field":
            return False

        self._lexical.openSub("classVarDec")
        lexical_writer.write(var_segment, self.FIELD_STATIC)  # kind
        text_tokens.next()
        var_type = text_tokens.get_token()
        lexical_writer.write(var_type)  #  type
        text_tokens.next()
        while True:  # get variable names
            var_name = text_tokens.get_token()
            lexical_writer.write(var_name, self.VAR_NAME)
            self._st.define(var_name,var_type,var_segment.upper())
            text_tokens.next()
            if text_tokens.get_token() != ",":
                break
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        self._lexical.closeSub()
        return True

    def run_subroutine_dec(self, text_tokens, writer,lexical_writer):
        """
        go over the text and parse methods decelerations to xml text
        :param text_tokens: give text
        :param lexical_writer: xml writer
        :return: null
        """
        while self.run_subroutine_dec_line(text_tokens, writer,lexical_writer):
            continue
        return True

    def run_subroutine_dec_line(self, text_tokens, writer,lexical_writer):
        """
        go over a specific method deceleration and parse to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if line is subroutine deceleration
        """
        name = text_tokens.get_token()  # subroutine type
        if name != "constructor" and name != "function" and name != "method":
            return False
        self._lexical.openSub("subroutineDec")
        lexical_writer.write(name, "keyword")
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token())
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.METHOD_NAME)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), self.OPEN_BRACKET)
        text_tokens.next()
        lexical_writer.openSub("parameterList")
        self.run_param_list(text_tokens, writer,lexical_writer)  # parameters list
        lexical_writer.closeSub()
        lexical_writer.write(text_tokens.get_token(), self.CLOSE_BRACKET)
        text_tokens.next()
        lexical_writer.openSub("subroutineBody")
        self.run_subroutine_body(text_tokens, writer,lexical_writer)  # subroutine body
        lexical_writer.closeSub()
        lexical_writer.closeSub()
        return True

    def run_param_list(self, text_tokens, writer,lexical_writer):
        """
          go over the text and parse method's parameter list to xml text
          :param text_tokens: give text
          :param lexical_writer: xml writer
          :return: null
          """
        while True:  # run over parameters until closing bracket is reached
            if text_tokens.get_token() == ")":
                return
            param_type = text_tokens.get_token()
            lexical_writer.write(param_type)
            text_tokens.next()
            param_name = text_tokens.get_token()
            lexical_writer.write(param_name, self.PARAM)
            self._st.define(param_name,param_type,"ARG")
            text_tokens.next()
            if text_tokens.get_token() != ",":
                return
            lexical_writer.write(text_tokens.get_token(), self.COMA)
            text_tokens.next()

    def run_subroutine_body(self, text_tokens, writer,lexical_writer):
        """
        parse subroutine body
        :param text_tokens: given jack tokens
        :param lexical_writer: xml writer
        :return:
        """
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        while self.run_var_dec(text_tokens, writer,lexical_writer):
            continue
        self.statements.run(text_tokens, writer,self._st,lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")
        text_tokens.next()
        return

    def run_var_dec(self, text_tokens, writer,lexical_writer):
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
        var_type =text_tokens.get_token()
        lexical_writer.write(var_type)  # write variable type
        text_tokens.next()
        var_name = text_tokens.get_token()
        lexical_writer.write(var_name, self.VAR_NAME)
        self._st.define(var_name, var_type, "VAR")
        text_tokens.next()
        while text_tokens.get_token() == ",":
            lexical_writer.write(text_tokens.get_token(), "symbol")  # write coma
            text_tokens.next()
            var_name = text_tokens.get_token()
            self._st.define(var_name,var_type,"VAR")
            lexical_writer.write(var_name, self.VAR_NAME)
            text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # write semi colon
        text_tokens.next()
        lexical_writer.closeSub()
        return True
