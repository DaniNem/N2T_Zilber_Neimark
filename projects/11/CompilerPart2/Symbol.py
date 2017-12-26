class Symbol(object):
    def __init__(self, name, type_of, kind, num):
        self._name = name
        self._type_of = type_of
        self._kind = kind
        self._num = num
        self._table = {'STATIC':'static','FIELD':'this','ARG':'argument'
            ,'VAR':'local'}

    def get_name(self):
        return self._name

    def get_kind(self):
        return self._table[self._kind]

    def get_type(self):
        return self._type_of

    def get_num(self):
        return self._num

    def __repr__(self):
        return self._name + ", " + self._type_of + ", " + self._kind + ", " + str(self._num)
