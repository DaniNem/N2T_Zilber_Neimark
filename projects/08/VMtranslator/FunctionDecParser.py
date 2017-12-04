class FunctionDecParser(object):
    """
    convert function deceleration statement to assembly
    """

    def __init__(self):
        """
        set initial params
        """
        self.file_name = ""
        self.ID = "function"

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
        t = line.split(' ')
        function = "(" + t[1] + ")"
        nVars = t[2]
        output_ds.append(function)
        for i in range(int(nVars)):  # set function arguments to 0
            output_ds.append("@SP")
            output_ds.append("A=M")
            output_ds.append("M=0")
            output_ds.append("@SP")
            output_ds.append("M=M+1")
