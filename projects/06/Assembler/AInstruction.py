class AInstruction:
    """
    an a instruction converting class
    """
    AT = "@"  # a instruction sign

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, lines, symbols):
        """
        go over the lines and convert them to binary form
        :param lines: file lines
        :param symbols: symbols dictionary
        """
        for i in range(len(lines)):  # go over the lines and and replace
            # the appropriate lines to binary form
            if lines[i].startswith(self.AT):  # check if a instruction
                jump = lines[i].strip(self.AT)
                self.__convert_to_bin(lines, jump, i)

    def __convert_to_bin(self, lines, name, line_num):
        """
        :param lines: file lines
        :param name: name of register
        :param line_num: appropriate line number
        """
        if name.isdigit():  # check that line is int
            reg = str(bin(int(name)))[2:]  # convert to binary form
            lines[line_num] = "0" + "0" * (15 - len(reg)) + reg
