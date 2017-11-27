class IfGoTo(object):
    IF_GOTO = "if-goto"

    def set_params(self, file_name):
        self.file_name = file_name

    def parse(self, line, output_ds):
        line_arr = line.split(" ")
        label = line_arr[1]
        output_ds.append("@SP")
        output_ds.append("M=M-1")
        output_ds.append("A=M")
        output_ds.append("D=M")
        output_ds.append("@"+label)
        output_ds.append("D;JNE")


    def is_triggered(self, line):
        """
        :param line: line of vm code
        :return: true if the line belongs to a certain memory segment
        """
        return self.IF_GOTO in line
