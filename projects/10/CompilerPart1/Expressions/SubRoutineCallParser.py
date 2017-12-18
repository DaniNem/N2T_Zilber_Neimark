from Expressions.ExpressionListParser import ExpressionListParser as ELP


class SubRoutineParser(object):
    """
    parse jack subroutine call to xml
    """
    expression_list_parser = ELP()

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
            self.expression_list_parser.run(text_tokens, lexical_writer)
            lexical_writer.write(next_token, "symbol")
            text_tokens.next()
            return True
        lexical_writer.write(text_tokens.get_token(), "identifier")  # write
        what = text_tokens.get_token()
        # subroutine name
        text_tokens.next()
        lexical_writer.write(text_tokens.get_token(), "symbol")  # opening bracket
        text_tokens.next()
        self.expression_list_parser.run(text_tokens, lexical_writer)
        lexical_writer.write(next_token, "symbol")  # closing bracket
        text_tokens.next()
