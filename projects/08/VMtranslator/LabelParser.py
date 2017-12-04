class LabelParser(object):
    """
    parse label command to assembly
    """

    def __init__(self):
        """
        set initial parmas
        """
        self.file_name = ""
        self.ID = "label"

    def is_triggered(self, line):
        """
        check if line match the parser
        :param line: given line
        :return: true if matched
        """
        return line.startswith(self.ID)

    def set_params(self, file_name):
        """
        set param
        :param file_name: given file name
        :return:
        """
        self.file_name = file_name

    def parse(self, line, output_ds):
        """
        parse vm line
        :param line: given vm line
        :param output_ds: assembly ds to write assembly commands to
        :return:
        """
        t = line.split(' ')
        label = t[1]
        output_ds.append("(" + label + ")")

