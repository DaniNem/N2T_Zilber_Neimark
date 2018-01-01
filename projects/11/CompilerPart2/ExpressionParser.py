class ExpressionParser(object):
    """
    parse jack expression to xml
    """
    ops = {"+": ("Aritmetic", "add"), "-": ("Aritmetic", "sub"),
           "*": ("Call", "Math.multiply"), "/": ("Call", "Math.divide")
        , "&": ("Aritmetic", "and"), "|": ("Aritmetic", "or"),
           "<": ("Aritmetic", "lt"), ">": ("Aritmetic", "gt"),
           "=": ("Aritmetic", "eq")}
    keyword_constant = ["true", "false", "null", "this"]
    unary_ops = ["-", "~"]

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, writer, symbol_table, lexical_writer):
        """
        parse an expression from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an expression
        """
        lexical_writer.openSub("expression")
        lexical_writer.openSub("term")
        self.run_term(text_tokens, writer, symbol_table,
                      lexical_writer)  # parse first term
        lexical_writer.closeSub()
        while text_tokens.get_token() in self.ops:
            lexical_writer.write(text_tokens.get_token(), "symbol")  # write operand
            symbol = text_tokens.get_token()
            text_tokens.next()
            lexical_writer.openSub("term")
            self.run_term(text_tokens, writer, symbol_table,
                          lexical_writer)  # parse next term
            if self.ops[symbol][0] == "Aritmetic":
                writer.writeAritmetic(self.ops[symbol][1])
            else:
                writer.writeCall(self.ops[symbol][1], 2)
            lexical_writer.closeSub()
        lexical_writer.closeSub()
        return True

    def run_term(self, text_tokens, writer, symbol_table, lexical_writer):
        """
        parse a term line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a term line
        """

        term = text_tokens.get_token()
        text_tokens.next()
        next_token = text_tokens.get_token()
        text_tokens.prev()
        if term.isdigit():  # check is an integer
            lexical_writer.write(term, "integerConstant")
            writer.writePush("constant", term)
            text_tokens.next()
            return True

        elif term.startswith("\""):  # check if string
            term = term[1:len(term) - 1]
            writer.writePush("constant", len(term))
            lexical_writer.write(term, "stringConstant")
            writer.writeCall("String.new", "1")

            for ch in term:
                writer.writePush("constant", ord(ch))
                writer.writeCall("String.appendChar", "2")
            text_tokens.next()
            return True

        elif term in self.keyword_constant:  # check if a keyword constant
            if term == 'true':
                writer.writePush("constant", 1)
                writer.writeAritmetic("not")
            elif term == 'false':
                writer.writePush("constant", 0)
            elif term == 'null':
                writer.writePush("constant", 0)
            elif term == 'this':
                writer.writePush("pointer", 0)
            else:
                raise (11)
            lexical_writer.write(term, "keyword")

            text_tokens.next()
            return True

        elif term in self.unary_ops:  # check if unary operand
            lexical_writer.write(term, "symbol")
            text_tokens.next()

            lexical_writer.openSub("term")
            self.run_term(text_tokens, writer, symbol_table, lexical_writer)
            if term == '~':
                writer.writeAritmetic('not')
            else:
                writer.writeAritmetic('neg')
            lexical_writer.closeSub()
            return True

        elif term.startswith("("):  # check if an expression
            lexical_writer.write(term, "symbol")
            text_tokens.next()
            self.run(text_tokens, writer, symbol_table, lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            return True

        elif self.run_subroutine_call(text_tokens, writer, symbol_table,
                                      lexical_writer):
            # check if call to subroutine
            # TODO run!!!
            return True

        elif next_token == "[":  # check if term is a call to array cell
            # TODO run!!!
            lexical_writer.write(term, "identifier")
            text_tokens.next()
            lexical_writer.write(next_token, "symbol")  # opening bracket
            text_tokens.next()
            self.run(text_tokens, writer, symbol_table, lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")  # closing
            # bracket
            text_tokens.next()
            return True

        lexical_writer.write(term, "identifier")  # term is a variable name
        writer.writePush(symbol_table.kind_of(term), symbol_table.index_of(term))
        text_tokens.next()
        return True

    def run_subroutine_call(self, text_tokens, writer, symbol_table, lexical_writer):
        """
        parse a term line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a term line
        """
        current_token = text_tokens.get_token()
        text_tokens.next()
        next_token = text_tokens.get_token()
        if next_token != "(" and next_token != ".":
            text_tokens.prev()
            return False
        lexical_writer.write(current_token, "identifier")  # write
        # subroutine/class/variable name to xml file
        lexical_writer.write(next_token, "symbol")  # writer ( or . to xml file
        text_tokens.next()
        if next_token == "(":
            counter = self.run_expression_list(text_tokens, writer, symbol_table,
                                               lexical_writer, True)
            writer.writeCall(symbol_table.kind_of("this") + "." + current_token,
                             counter)
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            return True
        lexical_writer.write(text_tokens.get_token(), "identifier")  # write
        # subroutine name
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        counter = self.run_expression_list(text_tokens, writer, symbol_table,
                                           lexical_writer, False)
        writer.writerCall(current_token, counter)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        text_tokens.next()
        return True

    def run_expression_list(self, text_tokens, writer, symbol_table,
                            lexical_writer, flag):
        """
        parse an expression list from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an expression list
        """
        lexical_writer.openSub("expressionList")
        counter = 0
        if flag:
            counter += 1
            writer.writePush("pointer", 0)
        if text_tokens.get_token() == ")":
            lexical_writer.closeSub()
            return counter
        self.run(text_tokens, writer, symbol_table, lexical_writer)
        counter += 1
        while text_tokens.get_token() == ",":
            counter += 1
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            self.run(text_tokens, writer, symbol_table, lexical_writer)
        lexical_writer.closeSub()
        return counter
