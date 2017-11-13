from FileReader import FileReader as fr


class JumpStatements(object):
    OPEN_BRACKETS = "("

    def __init__(self, lines, symbols):
        self.symbols = symbols
        self.file_lines = lines

    def run(self):
        res = []
        for i in range(len(self.file_lines)):
            a = self.file_lines[i]
            if a.startswith(self.OPEN_BRACKETS):
                line = self.file_lines[i].strip('()')
                self.symbols[line] = i
            else:
                res.append(self.file_lines[i])
        self.file_lines.clear()
        self.file_lines.extend(res)
        return
