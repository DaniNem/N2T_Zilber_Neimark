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
        line_arr = line.split(self.SPACE)
        if line_arr[1] == self.CONST:
            return True
        return False

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


if __name__ == "__main__":
    line1 = "push constant 10"
    ds = []
    const = ConstantParser()
    const.parse(line1,ds)
    print(ds)
