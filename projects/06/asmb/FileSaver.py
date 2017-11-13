class FileSaver:
    def __init__(self, lines):
        self.out_file = open("output.txt", "w")
        for i in range(len(lines)):
            self.out_file.write(lines[i] + "\n")
        self.out_file.close()
