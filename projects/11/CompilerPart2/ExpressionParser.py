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

    def run(self, text_tokens, writer, symbol_table):
        """
        parse an expression from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed an expression
        """
        self.run_term(text_tokens, writer, symbol_table)  # parse first term
        while text_tokens.get_token() in self.ops:

            symbol = text_tokens.get_token()
            text_tokens.next()
            self.run_term(text_tokens, writer, symbol_table)  # parse next term
            if self.ops[symbol][0] == "Aritmetic":
                writer.writeAritmetic(self.ops[symbol][1])
            else:
                writer.writeCall(self.ops[symbol][1], 2)
        return True

    def run_term(self, text_tokens, writer, symbol_table):
        """
        parse a term line from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed a term line
        """

        term = text_tokens.get_token()
        text_tokens.next()
        next_token = text_tokens.get_token()
        text_tokens.prev()
        if term.isdigit():  # check is an integer
            writer.writePush("constant", term)
            text_tokens.next()
            return True

        elif term.startswith("\""):  # check if string
            term = term[1:len(term) - 1]
            writer.writePush("constant", len(term))
            writer.writeCall("String.new", "1")

            for ch in term:
                writer.writePush("constant", ord(ch))
                writer.writeCall("String.appendChar", "2")
            text_tokens.next()
            return True

        elif term in self.keyword_constant:  # check if a keyword constant
            if term == 'true':
                writer.writePush("constant", 0)
                writer.writeAritmetic("not")
            elif term == 'false':
                writer.writePush("constant", 0)
            elif term == 'null':
                writer.writePush("constant", 0)
            elif term == 'this':
                writer.writePush("pointer", 0)
            text_tokens.next()
            return True

        elif term in self.unary_ops:  # check if unary operand
            text_tokens.next()
            self.run_term(text_tokens, writer, symbol_table)
            if term == '~':
                writer.writeAritmetic('not')
            else:
                writer.writeAritmetic('neg')
            return True

        elif term.startswith("("):  # check if an expression
            text_tokens.next()
            self.run(text_tokens, writer, symbol_table)
            text_tokens.next()
            return True

        elif self.run_subroutine_call(text_tokens, writer, symbol_table):
            # check if call to subroutine
            return True

        elif next_token == "[":  # check if term is a call to array cell
            text_tokens.next()
            text_tokens.next()
            self.run(text_tokens, writer, symbol_table)
            writer.writePush(symbol_table.kind_of(term), symbol_table.index_of(term))
            writer.writeAritmetic("add")
            writer.writePop("pointer", 1)
            writer.writePush("that", 0)
            text_tokens.next()
            return True
        writer.writePush(symbol_table.kind_of(term), symbol_table.index_of(term))
        text_tokens.next()
        return True

    def run_subroutine_call(self, text_tokens, writer, symbol_table):
        """
        parse a term line from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed a term line
        """
        current_token = text_tokens.get_token()
        text_tokens.next()
        next_token = text_tokens.get_token()
        if next_token != "(" and next_token != ".":
            text_tokens.prev()
            return False
        text_tokens.next()
        if next_token == "(":
            counter = self.run_expression_list(text_tokens, writer, symbol_table,
                                               True)
            writer.writeCall(symbol_table.class_name + "." + current_token,
                             counter)
            text_tokens.next()
            return True
        subroutine_name = text_tokens.get_token()
        if symbol_table.index_of(current_token) != None:
            writer.writePush(symbol_table.kind_of(current_token),
                             symbol_table.index_of(current_token))

        text_tokens.next()
        text_tokens.next()
        counter = self.run_expression_list(text_tokens, writer, symbol_table, False)
        if symbol_table.index_of(current_token) != None:
            counter += 1
            writer.writeCall(symbol_table.type_of(current_token) + "." +
                             subroutine_name, counter)
        else:
            writer.writeCall(current_token + "." + subroutine_name, counter)
        text_tokens.next()
        return True

    def run_expression_list(self, text_tokens, writer, symbol_table, is_method):
        """
        parse an expression list from jack to xml
        :param text_tokens: given jack code
        :param writer: vm writer
        :return: true if the given line is indeed an expression list
        """
        counter = 0
        if is_method:
            counter += 1
            writer.writePush("pointer", 0)
        if text_tokens.get_token() == ")":
            return counter
        self.run(text_tokens, writer, symbol_table)
        counter += 1
        while text_tokens.get_token() == ",":
            counter += 1
            text_tokens.next()
            self.run(text_tokens, writer, symbol_table)
        return counter
