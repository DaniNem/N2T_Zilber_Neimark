

class FunctionCallParser(object):
    def __init__(self):
        """
        """
        self.file_name = ""
        self.ID = "call"

    def is_triggered(self,line):
        '''

        :return:
        '''
        return line.startswith(self.ID)


    def set_params(self,file_name):
        self.file_name  = file_name

    def parse(self,line,output_ds):
        t = line.split(' ')
        function = t[1]
        nArgs = t[2]
        retLabel = self.file_name + ".retLabel" + str(len(output_ds))
        #pushing the retLabel
        output_ds.append("@" + retLabel)
        output_ds.append("D=A")
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("M=D")
        # SP ++
        output_ds.append("@SP")
        output_ds.append("M=M+1")
        #push LCL
        output_ds.append("@LCL")
        output_ds.append("D=M")
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("M=D")
        # SP ++
        output_ds.append("@SP")
        output_ds.append("M=M+1")
        #push ARG
        output_ds.append("@ARG")
        output_ds.append("D=M")
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("M=D")
        # SP ++
        output_ds.append("@SP")
        output_ds.append("M=M+1")
        #push THIS
        output_ds.append("@THIS")
        output_ds.append("D=M")
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("M=D")
        # SP ++
        output_ds.append("@SP")
        output_ds.append("M=M+1")
        #push THAT
        output_ds.append("@THAT")
        output_ds.append("D=M")
        output_ds.append("@SP")
        output_ds.append("A=M")
        output_ds.append("M=D")
        # SP ++
        output_ds.append("@SP")
        output_ds.append("M=M+1")

        #SET ARG ADDRESS
        output_ds.append("@SP")
        output_ds.append("D=M")
        output_ds.append("@"+nArgs)
        output_ds.append("D=D-A")
        output_ds.append("@5")
        output_ds.append("D=D-A")
        output_ds.append("@ARG")
        output_ds.append("M=D")

        #SET LCL ADDRESS
        output_ds.append("@SP")
        output_ds.append("D=M")
        output_ds.append("@LCL")
        output_ds.append("M=D")

        #set goto
        output_ds.append("@"+function)
        output_ds.append("1;JMP")

        output_ds.append("("+retLabel+")")


if __name__ == "__main__":
    pass