class FunctionRetParser(object):
    def __init__(self):
        """
        """
        self.file_name = ""
        self.ID = "return"

    def is_triggered(self, line):
        '''

        :return:
        '''
        return line.startswith(self.ID)

    def set_params(self, file_name):
        self.file_name = file_name

    def parse(self, line, output_ds):
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


        output_ds.append("@R14")
        output_ds.append("A=M")
        output_ds.append("1;JMP")



if __name__ == "__main__":
    pass
