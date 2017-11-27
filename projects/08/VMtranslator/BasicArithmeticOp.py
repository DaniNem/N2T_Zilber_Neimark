class BasicArithmeticOp(object):
    """
    a parser that convert vm operation command to assembly
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
    def set_params(self,file_name,func_name):
        pass
    def parse(self, line,output_ds):
        """
        convert vm operation command to assembly code
        :param output_ds: assembly commands output
        :return: none
        """
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("A=A-1")
        output_ds.append("D=M")
        output_ds.append("A=A-1")
        output_ds.append("M=M" + self.op + "D")
        #output_ds.append("M=D" + self.op + "M")
        output_ds.append("@SP")
        output_ds.append("M=M-1")
