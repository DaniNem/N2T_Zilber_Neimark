class JumpStatements(object):
    """
    a class that remove jump statements and save them in the symbols
    dictionary
    """
    OPEN_BRACKETS = "("

    def __init__(self):
        """
        default constructor
        """
        pass

    def run(self, lines, symbols):
        """
        :param lines: file lines
        :param symbols: a dictionary of pre defined symbols
        """
        res = []  # file lines after removing jump statements
        c = 0  # line number counter
        for line in lines:  # go over the lines, remove jump statements and
            # and them to the symbols dictionary
            if line.startswith(self.OPEN_BRACKETS):
                line = line.strip('()')
                symbols[line] = c
            else:  # if not a jump statement add to the result lines
                res.append(line)
                c += 1
        lines.clear()
        lines.extend(res)
