from ExpressionParser import ExpressionParser as EP


class StatementsParser(object):
    """
    parse a jack statement to vm code
    """
    expression_parser = EP()
    DO = "keyword"
    IF = "keyword"
    ELSE = "keyword"
    LET = "keyword"
    RETURN = "keyword"
    WHILE = "keyword"
    VAR_NAME = "identifier"

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, writer, symbol_table, bypass=False):
        """
        run a parser on jack statements and convert to xml tags
        :param text_tokens: given jack file
        :param writer: vm writer
        :param bypass: given flag
        :return:
        """
        more_statements = True  # check if more statements exists
        while more_statements:  # run over the statements
            a = self.run_do(text_tokens, writer, symbol_table)
            b = self.run_if(text_tokens, writer, symbol_table)
            c = self.run_let(text_tokens, writer, symbol_table)
            d = self.run_return(text_tokens, writer, symbol_table)
            e = self.run_while(text_tokens, writer, symbol_table)
            more_statements = a or b or c or d or e

        return True

    def run_do(self, text_tokens, writer, symbol_table):
        """
         parse a do line from jack to xml
         :param text_tokens: given jack code
         :param writer: vm writer
         :return: true if the given line is indeed a do line
         """
        if text_tokens.get_token() != "do":
            return False
        text_tokens.next()
        self.expression_parser.run_subroutine_call(text_tokens, writer, symbol_table)
        writer.writePop("temp", 0)  # return void
        text_tokens.next()
        return True

    def run_if(self, text_tokens, writer, symbol_table):
        """
        parse a if line from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed an if line
        """
        if text_tokens.get_token() != "if":
            return False
        if_true = "IF_TRUE" + str(writer.getLabelIndex())  # create labels
        if_false = "IF_FALSE" + str(writer.getLabelIndex())
        if_end = "IF_END" + str(writer.getLabelIndex())
        writer.incLabelIndex()
        text_tokens.next()
        text_tokens.next()
        self.expression_parser.run(text_tokens, writer,
                                   symbol_table)  # parse expression
        # in brackets
        writer.writeIf(if_true)  # if goto
        writer.writeGoTo(if_false)  # goto
        text_tokens.next()
        text_tokens.next()
        writer.writeLabel(if_true)
        self.run(text_tokens, writer, symbol_table, True)  # parse statements
        # in if body
        text_tokens.next()
        if text_tokens.get_token() != "else":  # check if else statement exists
            writer.writeLabel(if_false)  # goto
            return True
        writer.writeGoTo(if_end)
        text_tokens.next()
        text_tokens.next()
        writer.writeLabel(if_false)  # goto
        self.run(text_tokens, writer, symbol_table, True)  # parse statements
        # in else body
        text_tokens.next()
        writer.writeLabel(if_end)  # goto
        return True

    def run_let(self, text_tokens, writer, symbol_table):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed a let line
        """
        if text_tokens.get_token() != "let":
            return False
        text_tokens.next()
        var_name = text_tokens.get_token()
        text_tokens.next()
        is_array = False
        if text_tokens.get_token() == "[":  # check if var_name is an array
            text_tokens.next()
            self.expression_parser.run(text_tokens, writer, symbol_table)
            text_tokens.next()
            writer.writePush(symbol_table.kind_of(var_name), symbol_table.index_of(
                var_name))
            writer.writeAritmetic("add")
            is_array = True
        text_tokens.next()
        self.expression_parser.run(text_tokens, writer,
                                   symbol_table)  # parse expression
        #  after equal sign
        text_tokens.next()
        if is_array:  # array access via vm
            writer.writePop("temp", 0)
            writer.writePop("pointer", 1)
            writer.writePush("temp", 0)
            writer.writePop("that", 0)
            return True
        writer.writePop(symbol_table.kind_of(var_name),
                        symbol_table.index_of(var_name))
        return True

    def run_return(self, text_tokens, writer, symbol_table):
        """
        parse a return line from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed a return line
        """
        if text_tokens.get_token() != "return":
            return False
        # statement
        text_tokens.next()
        if text_tokens.get_token() != ";":
            self.expression_parser.run(text_tokens, writer,
                                       symbol_table)  # parse expression
        else:
            writer.writePush("constant", 0)  # return void
        writer.writeReturn()
        text_tokens.next()
        return True

    def run_while(self, text_tokens, writer, symbol_table):
        """
        parse a let line from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed a let line
        """
        if text_tokens.get_token() != "while":
            return False
        while_exp = "WHILE_EXP" + str(writer.getLabelIndex())
        while_end = "WHILE_END" + str(writer.getLabelIndex())
        writer.incLabelIndex()
        # statement
        text_tokens.next()
        text_tokens.next()
        writer.writeLabel(while_exp)
        self.expression_parser.run(text_tokens, writer, symbol_table)  # parse while
        # expression
        writer.writeAritmetic("not")
        writer.writeIf(while_end)
        text_tokens.next()
        text_tokens.next()
        self.run(text_tokens, writer, symbol_table, True)  # parse
        # statements in while body
        writer.writeGoTo(while_exp)
        text_tokens.next()
        writer.writeLabel(while_end)
        return True
