class AInstruction:
    AT = "@"

    def __init__(self, lines):
        self.lines = lines

    def run(self):
        for i in range(len(self.lines)):
            if self.lines[i].startswith(self.AT):
                jump = self.lines[i].strip(self.AT)
                self.__symbols_look_up(jump, i)

    def __symbols_look_up(self, name, line_num):
        if name.isdigit():
            reg = str(bin(int(name)))[2:]
            self.lines[line_num] = "0" + "0" * (15 - len(reg)) + reg
            return True

    def print_it(self):
        for line in self.lines:
            print(line)
