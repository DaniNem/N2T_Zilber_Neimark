class FileReader(object):
    """
    a class that read a file and save a list of it's lines
    """

    def __init__(self, file_name):
        """
        a constructor: saves the file lines
        :param file_name: the name of the file
        """
        self.file_list = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.file_list = [line.rstrip() for line in lines]

    def get_file(self):
        """
        :return: a list of the file lines
        """
        return self.file_list
