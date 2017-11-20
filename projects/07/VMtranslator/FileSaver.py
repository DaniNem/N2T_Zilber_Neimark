class FileSaver:
    """
    a class that receive a list of lines and saves them (one by one) in a
    file with a given name
    """

    def __init__(self, name, lines):
        """
        saves the lines in a .hack file
        :param name: name of the file
        :param lines: file lines
        """
        self.out_file = open(name, "w")
        for i in range(len(lines)):
            self.out_file.write(lines[i] + "\n")
        self.out_file.close()
