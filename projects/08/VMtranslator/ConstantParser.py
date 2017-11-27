class ConstantParser(object):
    """
    constant memory parser
    """
    SPACE = " "
    CONST = "constant"
    PUSH = "push"

    def is_triggered(self, line):
        """
        :param line: an vm line
        :return: true if this line refer to the constant memory
        """
        return self.CONST in line
    def set_params(self,file_name):
        pass
    def parse(self, line, output_ds):
        """
        convert vm code to assembly code
        :param line: vm line
        :param output_ds: data structure containing assembly code
        :return: none
        """
        num = line.split(self.SPACE)[2]
        output_ds.append("@" + num)
        output_ds.append("D=A")
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("M=D")
        output_ds.append("@SP")
        output_ds.append("M=M+1")
