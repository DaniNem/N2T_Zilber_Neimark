from Symbol import Symbol


class SymbolTable(object):
    count = {"STATIC": 0, "FIELD": 0, "ARG": 0, "VAR": 0}

    def __init__(self):
        self.class_symbols = dict()
        self.subroutine_symbols = dict()
        self.class_name = ""
        return

    def start_subroutine(self):
        self.subroutine_symbols = dict()
        self.count["ARG"] = 0
        self.count["VAR"] = 0
        return

    def define(self, name, type_of, kind):
        if kind == "STATIC" or kind == "FIELD":
            self.class_symbols[name] = Symbol(name, type_of, kind, self.count[kind])
            self.count[kind] += 1

        if kind == "ARG" or kind == "VAR":
            self.subroutine_symbols[name] = Symbol(name, type_of, kind,
                                                   self.count[kind])
            self.count[kind] += 1

    def var_count(self, kind):
        return self.count[kind]

    def kind_of(self, name):
        if name in self.subroutine_symbols:
            return self.subroutine_symbols[name].get_kind()
        elif name in self.class_symbols:
            return self.class_symbols[name].get_kind()
        return None

    def type_of(self, name):
        if name in self.subroutine_symbols:
            return self.subroutine_symbols[name].get_type()
        elif name in self.class_symbols:
            return self.class_symbols[name].get_type()
        return None

    def index_of(self, name):
        if name in self.subroutine_symbols:
            return self.subroutine_symbols[name].get_num()
        elif name in self.class_symbols:
            return self.class_symbols[name].get_num()
        return None

    def print(self):
        print(self.class_symbols)
        print("------")
        print(self.subroutine_symbols)

