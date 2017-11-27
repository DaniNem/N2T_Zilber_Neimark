class ConditionsOp(object):
    """
    a parser that convert vm operation command to assembly
    """
    SPACE = " "

    def is_triggered(self, line):
        """
        :param line: an vm line
        :return: true if this line refer to given operation command
        """
        if self.OPERATION in line :
            return True
        return False

    def set_params(self,file_name):
        pass
    def parse(self, line, output_ds):
        """
        convert vm operation command to assembly code
        :param output_ds: assembly commands output
        :param line: line to parse
        :return: none
        """
        JUMP = len(output_ds)
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("A=A-1")
        output_ds.append("D=M")
        output_ds.append("A=A-1")
        output_ds.append("D=M-D")
        output_ds.append("@JUMP" + str(JUMP))
        output_ds.append("D;" + self.jump_condition)
        output_ds.append("D=-1")
        output_ds.append("@END" + str(JUMP))
        output_ds.append("1;JMP")
        output_ds.append("(JUMP" + str(JUMP) + ")")
        output_ds.append("D=0")
        output_ds.append("(END" + str(JUMP) + ")")
        output_ds.append("@SP")
        output_ds.append("M=M-1")
        output_ds.append("A=M-1")
        output_ds.append("M=D")
