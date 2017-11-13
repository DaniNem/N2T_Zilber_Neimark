class AInstruction:
    AT = "@"

    def __init__(self):
        pass

    def run(self,lines,symbols):
        for i in range(len(lines)):
            if lines[i].startswith(self.AT):
                jump = lines[i].strip(self.AT)
                self.__symbols_look_up(lines,jump, i)

    def __symbols_look_up(self,lines, name, line_num):
        if name.isdigit():
            reg = str(bin(int(name)))[2:]
            lines[line_num] = "0" + "0" * (15 - len(reg)) + reg

