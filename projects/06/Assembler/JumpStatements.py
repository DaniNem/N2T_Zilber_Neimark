class JumpStatements(object):
    OPEN_BRACKETS = "("

    def __init__(self):
        pass
    def run(self,lines,symbols):
        res = []
        c = 0
        for line in lines:
            if line.startswith(self.OPEN_BRACKETS):
                line = line.strip('()')
                symbols[line] = c
            else:
                res.append(line)
                c+=1
        lines.clear()
        lines.extend(res)
        return
