class OneOperandArithmetic(object):
    """
    a parser that convert vm addition command to assembly
    """
    SPACE = " "

    def is_triggered(self, line):
        """
        :param line: an vm line
        :return: true if this line refer to given operation command
        """
        if line.split(self.SPACE)[0] == self.OPERATION:
            return True
        return False

    def parse(self, output_ds):
        """
        convert vm operation command to assembly code
        :param output_ds: assembly commands output
        :return: none
        """
        output_ds.append("@SP")
        output_ds.append("@A=M")
        output_ds.append("A=A-1")
        output_ds.append("D=M")
        output_ds.append(self.op + "M")
