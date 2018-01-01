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

    def run(self, text_tokens, writer, symbol_table, lexical_writer, bypass=False):
        """
        run a parser on jack statements and convert to xml tags
        :param text_tokens: given jack file
        :param lexical_writer: xml writer
        :param bypass: given flag
        :return:
        """
        more_statements = True  # check if more statements exists
        sub_flag = False  # check need to open new sub
        term = text_tokens.get_token()
        if term == "do" or term == "if" or term == "let" or term == "while" or \
                        term == "return" or bypass:
            lexical_writer.openSub("statements")
            sub_flag = True
        while more_statements:  # run over the statements
            a = self.run_do(text_tokens, writer, symbol_table, lexical_writer)
            b = self.run_if(text_tokens, writer, symbol_table, lexical_writer)
            c = self.run_let(text_tokens, writer, symbol_table, lexical_writer)
            d = self.run_return(text_tokens, writer, symbol_table, lexical_writer)
            e = self.run_while(text_tokens, writer, symbol_table, lexical_writer)
            more_statements = a or b or c or d or e
        if sub_flag:
            lexical_writer.closeSub()
        return True

    def run_do(self, text_tokens, writer, symbol_table, lexical_writer):
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
        self.expression_parser.run_subroutine_call(text_tokens, writer, symbol_table,
                                                   lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # parse semi colon
        writer.writePop("temp", 0)
        text_tokens.next()
        lexical_writer.closeSub()
        return True

    def run_if(self, text_tokens, writer, symbol_table, lexical_writer):
        """
        parse a if line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an if line
        """
        if text_tokens.get_token() != "if":
            return False
        lexical_writer.openSub("ifStatement")
        if_true = "IF_TRUE" + str(writer.getLabelIndex())
        if_false = "IF_FALSE" + str(writer.getLabelIndex())
        if_end = "IF_END" + str(writer.getLabelIndex())
        writer.incLabelIndex()
        lexical_writer.write(text_tokens.get_token(), self.IF)
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening brackets
        text_tokens.next()
        self.expression_parser.run(text_tokens, writer, symbol_table,
                                   lexical_writer)  # parse expression
        # in brackets
        writer.writeIf(if_true)  # if goto
        writer.writeGoTo(if_false)  # goto
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing brackets
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening brackets
        text_tokens.next()
        writer.writeLabel(if_true)
        self.run(text_tokens, writer, symbol_table, lexical_writer,
                 True)  # parse statements
        # in if body
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing brackets
        text_tokens.next()
        if text_tokens.get_token() != "else":  # check if else statement exists
            lexical_writer.closeSub()
            writer.writeLabel(if_false)  # goto
            return True
        writer.writeGoTo(if_end)
        lexical_writer.write(text_tokens.get_token(), "keyword")  # opening brackets
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        writer.writeLabel(if_false)  # goto
        self.run(text_tokens, writer, symbol_table, lexical_writer,
                 True)  # parse statements
        # in else body
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing brackets
        text_tokens.next()
        lexical_writer.closeSub()
        writer.writeLabel(if_end)  # goto
        return True

    def run_let(self, text_tokens, writer, symbol_table, lexical_writer):
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
        var_name = text_tokens.get_token()
        lexical_writer.write(var_name, self.VAR_NAME)
        text_tokens.next()
        is_array = False
        if text_tokens.get_token() == "[":  # check if var_name is an array
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            self.expression_parser.run(text_tokens, writer, symbol_table,
                                       lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            writer.writePush(symbol_table.type_of(var_name), symbol_table.index_of(
                var_name))
            writer.writeAritmetic("add")
            is_array = True
        lexical_writer.write(text_tokens.get_token(), "symbol")  # get equal sign
        text_tokens.next()
        self.expression_parser.run(text_tokens, writer, symbol_table,
                                   lexical_writer)  # parse expression
        #  after equal sign
        lexical_writer.write(text_tokens.get_token(), "symbol")  # semi colon sign
        text_tokens.next()
        lexical_writer.closeSub()
        if is_array:
            writer.writePop("temp", 0)
            writer.writePop("pointer", 1)
            writer.writePush("temp", 0)
            writer.writePop("that", 0)
            return True
        writer.writePop(symbol_table.kind_of(var_name),
                        symbol_table.index_of(var_name))
        return True

    def run_return(self, text_tokens, writer, symbol_table, lexical_writer):
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
            self.expression_parser.run(text_tokens, writer, symbol_table,
                                       lexical_writer)
            # parse expression
        else:
            writer.writePush("constant", 0)
        writer.writeReturn()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # parse semi colon
        text_tokens.next()
        lexical_writer.closeSub()
        return True

    def run_while(self, text_tokens, writer, symbol_table, lexical_writer):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a let line
        """
        if text_tokens.get_token() != "while":
            return False
        lexical_writer.openSub("whileStatement")
        while_exp = "WHILE_EXP" + str(writer.getLabelIndex())
        while_end = "WHILE_END" + str(writer.getLabelIndex())
        writer.incLabelIndex()
        lexical_writer.write(text_tokens.get_token(), self.WHILE)  # parse while
        # statement
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        writer.writeLabel(while_exp)
        self.expression_parser.run(text_tokens, writer, symbol_table,
                                   lexical_writer)  # parse while
        # expression
        writer.writeAritmetic("not")
        writer.writeIf(while_end)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening
        # bracket (body)
        text_tokens.next()
        self.run(text_tokens, writer, symbol_table, lexical_writer, True)
        writer.writeGoTo(while_exp)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        #  (body)
        text_tokens.next()
        lexical_writer.closeSub()
        writer.writeLabel(while_end)
        return True
