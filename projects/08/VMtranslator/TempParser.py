from PushPopParser import PushPopParser


class TempParser(PushPopParser):
    """
        convert a pop and pop operations of temp memory from vm language
        to assembly
    """

    def __init__(self):
        """
            set initial parameters
        """
        self.map = ["R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"]
        self.ID = "temp"

    def __parse_pop(self, num, output_ds):
        """
        translate pop operation to assembly
        :param num: number of register
        :param output_ds: post translating code
        :return: null
        """

        # go to last stuck arg
        output_ds.append("@SP")
        output_ds.append("A=M-1")
        # remember the value in D
        output_ds.append("D=M")
        output_ds.append("@" + self.map[int(num)])
        # update the memorey
        output_ds.append("M=D")
        # update the sp pos
        output_ds.append("@SP")
        output_ds.append("M=M-1")

    def __parse_push(self, num, output_ds):
        """
        translate push operation to assembly
        :param num: number of appropriate register
        :param output_ds: post translation code
        :return: null
        """
        output_ds.append("@" + self.map[int(num)])
        # Remember this value in D
        output_ds.append("D=M")
        # go to the stuck last pos
        output_ds.append("@SP")
        output_ds.append("A=M")
        # update the stuck
        output_ds.append("M=D")
        # update the suck pointer
        output_ds.append("@SP")
        output_ds.append("M=M+1")

    def parse(self, line, output_ds):
        """
        translate a given push/pop command to assembly
        :param line: a given line of code
        :param output_ds: post translation code
        :return: null
        """
        t = line.split(' ')
        if t[0] == "pop":
            self.__parse_pop(t[2], output_ds)
        else:
            self.__parse_push(t[2], output_ds)
