class FileReader(object):


    def __init__(self, file_name):
        self.file_list = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.file_list = [line.rstrip() for line in lines]


    def get_file(self):
        return self.file_list

