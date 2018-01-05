from StatementsParser import StatementsParser as SP
from SymbolTable import SymbolTable as ST


class ClassParser(object):
    """
    class parser
    """
    statements = SP()
    # FIELD_STATIC = "keyword"
    # VAR_NAME = "identifier"
    # METHOD_NAME = "identifier"
    # OPEN_BRACKET = "symbol"
    # CLOSE_BRACKET = "symbol"
    # PARAM = "identifier"
    # COMA = "symbol"
    # VAR = "keyword"

    def __init__(self, tokens, writer):
        """
        get text token and xml writer
        :param tokens:
        :param lexical:
        """
        self._tokens = tokens
        self._writer = writer
        self._st = ST()
        self._class_name = ""

    def run(self):
        """
        parse jack file
        :return: none
        """
        self._tokens.next()
        self._class_name = self._tokens.get_token()  # get class name
        self._st.class_name = self._class_name
        self._tokens.next()
        self._tokens.next()
        self.run_class_var_dec(self._tokens, self._writer)  # class variables
        self.run_subroutine_dec(self._tokens, self._writer)  # class subroutines
        self._tokens.next()

    def run_class_var_dec(self, text_tokens, writer):
        """
        run over the code and convert class member to appropriate xml tags
        :param text_tokens: given code
        :param writer: writer of vm
        :return: null
        """
        while self.run_var_dec_line(text_tokens, writer):
            continue
        return True

    def run_var_dec_line(self, text_tokens, writer):
        """
        run a specific line of code to check for class member and parse it
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if line is variable deceleration
        """
        var_segment = text_tokens.get_token()
        if var_segment != "static" and var_segment != \
                "field":
            return False
        text_tokens.next()
        var_type = text_tokens.get_token()
        text_tokens.next()
        while True:  # get variable names
            var_name = text_tokens.get_token()
            self._st.define(var_name, var_type, var_segment.upper())  # update
            # symbol table
            text_tokens.next()
            if text_tokens.get_token() != ",":
                break
            text_tokens.next()
        text_tokens.next()
        return True

    def run_subroutine_dec(self, text_tokens, writer):
        """
        go over the text and parse methods decelerations to xml text
        :param text_tokens: give text
        :param writer: vm writer
        :return: null
        """
        while self.run_subroutine_dec_line(text_tokens, writer):
            continue
        return True

    def run_subroutine_dec_line(self, text_tokens, writer):
        """
        go over a specific method deceleration and parse to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if line is subroutine deceleration
        """
        subroutine_type = text_tokens.get_token()  # subroutine type
        if subroutine_type != "constructor" and subroutine_type != "function" \
                and subroutine_type != "method":
            return False
        self._st.start_subroutine()  # start new symbol table for function
        text_tokens.next()
        text_tokens.next()
        subroutine_name = text_tokens.get_token()
        text_tokens.next()
        text_tokens.next()
        self.run_param_list(text_tokens, writer, subroutine_type)  # parameters
        # list
        text_tokens.next()
        self.run_subroutine_body(text_tokens, writer,
                                 subroutine_name, subroutine_type)  # subroutine body
        return True

    def run_param_list(self, text_tokens, writer, subroutine_type):
        """
          go over the text and parse method's parameter list to xml text
          :param text_tokens: give text
          :param writer: vm writer
          :return: null
          """
        if subroutine_type == "method":
            self._st.define("this", self._class_name, "ARG")  # add this to symbol
            # table
        while True:  # run over parameters until closing bracket is reached
            if text_tokens.get_token() == ")":
                return
            param_type = text_tokens.get_token()
            text_tokens.next()
            param_name = text_tokens.get_token()
            self._st.define(param_name, param_type, "ARG")  # define new symbols
            text_tokens.next()
            if text_tokens.get_token() != ",":
                return
            text_tokens.next()

    def run_subroutine_body(self, text_tokens, writer,
                            subroutine_name, subroutine_type):
        """
        parse subroutine body
        :param text_tokens: given jack tokens
        :param writer: vm writer
        :return:
        """
        text_tokens.next()
        while self.run_var_dec(text_tokens, writer):
            continue
        writer.writeFunction(self._class_name + '.' + subroutine_name,
                             self._st.var_count('VAR'))  # write function

        if subroutine_type == "constructor":
            writer.writePush("constant", self._st.var_count("FIELD"))
            writer.writeCall("Memory.alloc", 1)  # alloc memory for object
            writer.writePop("pointer", 0)
        elif subroutine_type == "method":  # push this
            writer.writePush("argument", 0)
            writer.writePop("pointer", 0)
        self.statements.run(text_tokens, writer, self._st)  # parse
        #  statements
        text_tokens.next()
        return

    def run_var_dec(self, text_tokens, writer):
        """
        convert variable deceleration to xml text
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if line is variable deceleration line
        """
        token = text_tokens.get_token()
        if token != "var":
            return False
        text_tokens.next()
        var_type = text_tokens.get_token()
        text_tokens.next()
        var_name = text_tokens.get_token()
        self._st.define(var_name, var_type, "VAR")  # define new symbol
        text_tokens.next()
        while text_tokens.get_token() == ",":
            text_tokens.next()
            var_name = text_tokens.get_token()
            self._st.define(var_name, var_type, "VAR")  # define new symbols
            text_tokens.next()
        text_tokens.next()
        return True
