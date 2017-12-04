class GotoParser(object):
    """
    convert go to operator to assembly
    """
    def __init__(self):
        """
        initialize arguments
        """
        self.file_name = ""
        self.ID = "goto"

    def is_triggered(self,line):
        """
        check if line match the parser
        :param line: given vm line
        :return: true if match the parser
        """
        return line.startswith(self.ID)


    def set_params(self,file_name):
        """
        set file name param
        :param file_name: given file name
        :return:
        """
        self.file_name  = file_name

    def parse(self,line,output_ds):
        """
        parse line
        :param line: given vm line
        :param output_ds: assembly ds to add commands
        :return:
        """
        t = line.split(' ')
        label = t[1]
        output_ds.append("@" + label)
        output_ds.append("1;JMP")
