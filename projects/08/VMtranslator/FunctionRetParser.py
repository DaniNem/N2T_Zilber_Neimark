class FunctionRetParser(object):
    """
    convert function return statement to assembly
    """
    def __init__(self):
        """
        set initial params
        """
        self.file_name = ""
        self.ID = "return"

    def is_triggered(self, line):
        """
        check if line match the parser
        :param line: given vm line
        :return: true if matched
        """
        return line.startswith(self.ID)

    def set_params(self, file_name):
        """
        set name param
        :param file_name: given file name
        :return:
        """
        self.file_name = file_name

    def parse(self, line, output_ds):
        """
        parse vm line to assembly
        :param line: given vm line
        :param output_ds: assembly ds to add commands
        :return:
        """
        # R13 = LCL
        output_ds.append("@LCL")
        output_ds.append("D=M")
        output_ds.append("@R13")
        output_ds.append("M=D")
        # retAddr = *(frame-5)
        output_ds.append("@5")
        output_ds.append("D=D-A")
        output_ds.append("A=D")
        output_ds.append("D=M")

        output_ds.append("@R14")
        output_ds.append("M=D")
        # *ARG = result
        output_ds.append("@SP")
        output_ds.append("A=M-1")
        output_ds.append("D=M")
        output_ds.append("@ARG")
        output_ds.append("A=M")
        output_ds.append("M=D")
        # SP=ARG+1
        output_ds.append("@ARG")
        output_ds.append("D=M+1")
        output_ds.append("@SP")
        output_ds.append("M=D")
        #THAT = *(frame-1)
        output_ds.append("@R13")
        output_ds.append("M=M-1")
        output_ds.append("A=M")
        output_ds.append("D=M")
        output_ds.append("@THAT")
        output_ds.append("M=D")
        # THIS = *(frame-2)
        output_ds.append("@R13")
        output_ds.append("M=M-1")
        output_ds.append("A=M")
        output_ds.append("D=M")
        output_ds.append("@THIS")
        output_ds.append("M=D")
        # ARG = *(frame-3)
        output_ds.append("@R13")
        output_ds.append("M=M-1")
        output_ds.append("A=M")
        output_ds.append("D=M")
        output_ds.append("@ARG")
        output_ds.append("M=D")
        # LCL = *(frame-4)
        output_ds.append("@R13")
        output_ds.append("M=M-1")
        output_ds.append("A=M")
        output_ds.append("D=M")
        output_ds.append("@LCL")
        output_ds.append("M=D")

        # jump from function
        output_ds.append("@R14")
        output_ds.append("A=M")
        output_ds.append("1;JMP")

