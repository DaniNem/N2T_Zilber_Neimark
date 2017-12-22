class ExpressionParser(object):
    """
    parse jack expression to xml
    """
    ops = ["+", "-", "*", "/", "&", "|", "<", ">", "="]
    keyword_constant = ["true", "false", "null", "this"]
    unary_ops = ["-", "~"]

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse an expression from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an expression
        """
        lexical_writer.openSub("expression")
        lexical_writer.openSub("term")
        self.run_term(text_tokens, lexical_writer)  # parse first term
        lexical_writer.closeSub()
        while text_tokens.get_token() in self.ops:
            lexical_writer.write(text_tokens.get_token(), "symbol")  # write operand
            text_tokens.next()
            lexical_writer.openSub("term")
            self.run_term(text_tokens, lexical_writer)  # parse next term
            lexical_writer.closeSub()
        lexical_writer.closeSub()
        return True

    def run_term(self, text_tokens, lexical_writer):
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
            text_tokens.next()
            return True

        elif term.startswith("\""):  # check if string
            term = term[1:len(term) - 1]
            lexical_writer.write(term, "stringConstant")
            text_tokens.next()
            return True

        elif term in self.keyword_constant:  # check if a keyword constant
            lexical_writer.write(term, "keyword")
            text_tokens.next()
            return True

        elif term in self.unary_ops:  # check if unary operand
            lexical_writer.write(term, "symbol")
            text_tokens.next()
            lexical_writer.openSub("term")
            self.run_term(text_tokens, lexical_writer)
            lexical_writer.closeSub()
            return True

        elif term.startswith("("):  # check if an expression
            lexical_writer.write(term, "symbol")
            text_tokens.next()
            self.run(text_tokens, lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            return True

        elif self.run_subroutine_call(text_tokens, lexical_writer):  #
            # check if call to subroutine
            return True

        elif next_token == "[":  # check if term is a call to array cell
            lexical_writer.write(term, "identifier")
            text_tokens.next()
            lexical_writer.write(next_token, "symbol")  # opening bracket
            text_tokens.next()
            self.run(text_tokens, lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")  # closing
            # bracket
            text_tokens.next()
            return True

        lexical_writer.write(term, "identifier")  # term is a variable name
        text_tokens.next()
        return True

    def run_subroutine_call(self, text_tokens, lexical_writer):
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
            self.run_expression_list(text_tokens, lexical_writer)
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            return True
        lexical_writer.write(text_tokens.get_token(), "identifier")  # write
        # subroutine name
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        self.run_expression_list(text_tokens, lexical_writer)
        lexical_writer.write(text_tokens.get_token(), "symbol")  # closing bracket
        text_tokens.next()
        return True

    def run_expression_list(self, text_tokens, lexical_writer):
        """
        parse an expression list from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed an expression list
        """
        lexical_writer.openSub("expressionList")
        if text_tokens.get_token() == ")":
            lexical_writer.closeSub()
            return True
        self.run(text_tokens, lexical_writer)
        while text_tokens.get_token() == ",":
            lexical_writer.write(text_tokens.get_token(), "symbol")
            text_tokens.next()
            self.run(text_tokens, lexical_writer)
        lexical_writer.closeSub()
        return True
