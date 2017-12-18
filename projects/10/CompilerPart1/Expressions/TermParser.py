from Expressions.SubRoutineCallParser import SubRoutineParser as SRP


class TermParser(object):
    """
    parse jack term to xml
    """
    keyword_constant = ["true", "false", "null", "this"]
    unary_ops = ["-", "~"]
    subroutine_parser = SRP()

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, text_tokens, lexical_writer):
        """
        parse a term line from jack to xml
        :param text_tokens: given jack code
        :param lexical_writer: xml writer
        :return: true if the given line is indeed a term line
        """
        from Expressions.ExpressionParser import ExpressionParser as EP
        expression_parser = EP()

        term = text_tokens.get_token()
        text_tokens.next()
        next_token = text_tokens.get_token()
        text_tokens.prev()
        if term.isdigit():  # check is an integer
            lexical_writer.write(term, "integerConstant")
            text_tokens.next()
            return True

        elif term.startswith("\""):  # check if string
            lexical_writer.write(term, "StringConstant")
            text_tokens.next()
            return True

        elif term in self.keyword_constant:  # check if a keyword constant
            lexical_writer.write(term, "keyword")
            text_tokens.next()
            return True

        elif term in self.unary_ops:  # check if unary operand
            lexical_writer.write(term, "symbol")
            text_tokens.next()
            self.run(text_tokens, lexical_writer)
            return True

        elif term.startswith("("):  # check if an expression
            lexical_writer.write(term, "symbol")
            text_tokens.next()
            expression_parser.run(text_tokens, lexical_writer)
            lexical_writer.write(term, "symbol")
            text_tokens.next()
            return True

        elif self.subroutine_parser.run(text_tokens, lexical_writer):  #
            # check if call to subroutine
            return True

        elif next_token == "[":  # check if term is a call to array cell
            lexical_writer.write(term, "identifier")
            text_tokens.next()
            lexical_writer.write(next_token, "symbol")  # opening bracket
            text_tokens.next()
            expression_parser.run(text_tokens, lexical_writer)
            lexical_writer.write(next_token, "symbol")  # closing bracket
            text_tokens.next()
            return True

        lexical_writer.write(term, "identifier")  # term is a variable name
        text_tokens.next()
        return True
