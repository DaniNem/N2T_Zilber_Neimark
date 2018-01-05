from Symbol import Symbol


class SymbolTable(object):
    """
    class and specific function symbol tables
    """

    def __init__(self):
        """
        default constructor
        """
        self.class_symbols = dict()
        self.subroutine_symbols = dict()
        self.class_name = ""
        self.count = {"STATIC": 0, "FIELD": 0, "ARG": 0, "VAR": 0}
        return

    def start_subroutine(self):
        """
        start a symbol table for a new sub routine
        :return: none
        """
        self.subroutine_symbols = dict()
        self.count["ARG"] = 0  # reset counts
        self.count["VAR"] = 0
        return

    def define(self, name, type_of, kind):
        """
        define a new symbol and add to table
        :param name: symbol's name
        :param type_of: symbol's jack type
        :param kind: symbol's vm stack type
        :return: none
        """
        if kind == "STATIC" or kind == "FIELD":  # check if class table or function
            #  table
            self.class_symbols[name] = Symbol(name, type_of, kind, self.count[kind])
            self.count[kind] += 1

        if kind == "ARG" or kind == "VAR":
            self.subroutine_symbols[name] = Symbol(name, type_of, kind,
                                                   self.count[kind])
            self.count[kind] += 1
        return

    def var_count(self, kind):
        """

        :param kind: kind of symbol
        :return: # of symbols with specific kind
        """
        return self.count[kind]

    def kind_of(self, name):
        """

        :param name: given symbol
        :return: kind of symbol (if does not exists then return none)
        """
        if name in self.subroutine_symbols:
            return self.subroutine_symbols[name].get_kind()
        elif name in self.class_symbols:
            return self.class_symbols[name].get_kind()
        return None

    def type_of(self, name):
        """

        :param name: given symbol
        :return: type of symbol (if does not exists then return none)
        """
        if name in self.subroutine_symbols:
            return self.subroutine_symbols[name].get_type()
        elif name in self.class_symbols:
            return self.class_symbols[name].get_type()
        return None

    def index_of(self, name):
        """

        :param name: given symbol
        :return: index of symbol (if does not exists then return none)
        """
        if name in self.subroutine_symbols:
            return self.subroutine_symbols[name].get_num()
        elif name in self.class_symbols:
            return self.class_symbols[name].get_num()
        return None

    def print(self):
        """
        print the tables
        :return:
        """
        print(self.class_symbols)
        print("------")
        print(self.subroutine_symbols)
