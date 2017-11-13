class FileSaver:
    def __init__(self, name,lines):
        self.out_file = open(name, "w")
        for i in range(len(lines)):
            self.out_file.write(lines[i] + "\n")
        self.out_file.close()
