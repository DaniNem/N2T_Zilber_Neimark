class FunctionDecParser(object):

    def __init__(self):
        """
        """
        self.file_name = ""
        self.ID = "function"

    def is_triggered(self, line):
        '''

        :return:
        '''
        return line.startswith(self.ID)

    def set_params(self, file_name):
        self.file_name = file_name

    def parse(self, line, output_ds):
        t = line.split(' ')
        function = "(" + t[1] + ")"
        nVars = t[2]
        output_ds.append(function)
        for i in range(int(nVars)):
            output_ds.append("@SP")
            output_ds.append("A=M")
            output_ds.append("M=0")
            output_ds.append("@SP")
            output_ds.append("M=M+1")




if __name__ == "__main__":
    pass