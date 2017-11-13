class FileReader(object):
    file_list = []
    length = 0

    def __init__(self, file_name):
        self.file = open(file_name, 'r')
        lines = self.file.readlines()
        self.length = len(lines)
        self.file_list = [line.rstrip() for line in lines]

    def get_file(self):
        return self.file_list

    def print_lines(self):
        for line in self.file_list:
            print(line)
        return

