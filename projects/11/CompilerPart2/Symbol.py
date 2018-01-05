class Symbol(object):
    """
    define a symbol
    """

    def __init__(self, name, type_of, kind, num):
        """
        constructor set value to symbol
        :param name: symbol name
        :param type_of: symbol jack type
        :param kind: stack type
        :param num: number of appropriate kind in appropriate symbol table
        """
        self._name = name
        self._type_of = type_of
        self._kind = kind
        self._num = num
        self._table = {'STATIC': 'static', 'FIELD': 'this', 'ARG': 'argument'
            , 'VAR': 'local'}

    def get_name(self):
        """

        :return: symbol's name
        """
        return self._name

    def get_kind(self):
        """

        :return: symbol's jack type
        """
        return self._table[self._kind]

    def get_type(self):
        """

        :return: symbol's appropriate stack type
        """
        return self._type_of

    def get_num(self):
        """

        :return: number of appropriate kind in appropriate symbol table
        """
        return self._num

    def __repr__(self):
        """

        :return: string representation o symbol
        """
        return self._name + ", " + self._type_of + ", " + self._kind + ", " + str(
            self._num)
