class JackTokenizer(object):
    def __init__(self, path):
        self.currentIndex = 0
        self.data = []
        ftokens = []
        # split by lines
        with open(path, 'r') as f:
            for line in f.readlines():
                ftokens.append(line)
        symbols = ['{', '}', '.', '(', ')', '[', ']', ',', ';', '+', '-', '*',
                   '&', '<', '>', '=', '~', '\n', '\t', '/', '"', ' ']
        # split by symbols
        splitTok = []
        for t in ftokens:
            temp = list(t)
            indices = []
            for s in symbols:
                indices.extend([i for i, x in enumerate(temp) if x == s])
            indices.sort()
            if len(indices) > 0:
                i = 0
                for n in indices:
                    if (t[i:n] != ''):
                        splitTok.append(t[i:n])
                    if (t[n:n + 1] != ''):
                        splitTok.append(t[n:n + 1])
                    i = n + 1
                if (t[i:] != ''):
                    splitTok.append(t[i:])
            else:
                splitTok.append(t)
        f1 = False
        f2 = False
        strF = False
        strData = ''
        i = 0
        # remove comments and parse the data to tokens
        while i < len(splitTok):
            if (not f1 and not f2 and not strF and splitTok[i] == '/'):
                if (splitTok[i + 1] == '/'):
                    i += 2
                    f1 = True
                    continue
                if (splitTok[i + 1] == '*'):
                    i += 2
                    f2 = True
                    continue
            if (not strF and f1 and splitTok[i] == '\n'):
                f1 = False
                i += 1
                continue
            if (f2 and splitTok[i] == '*'):
                if (splitTok[i + 1] == '/'):
                    f2 = False
                    i += 2
                    continue

            if (not f1 and not f2 and splitTok[i] == '"'):
                strData += splitTok[i]
                if (strF):
                    self.data.append(strData)
                    strData = ''
                    strF = False
                else:
                    strF = True
                i += 1
                continue
            if (strF):
                strData += splitTok[i]
                i += 1
                continue
            if (not strF and not f1 and not f2 and splitTok[i] != '' and splitTok[
                i] != '\t' and splitTok[i] != '\n' and splitTok[i] != ' '):
                self.data.append(splitTok[i])
            i += 1

    def hasNext(self):
        return self.currentIndex == len(self.data) - 1

    def next(self):
        self.currentIndex += 1

    def prev(self):
        self.currentIndex -= 1
        return self

    def get_token(self):
        return self.data[self.currentIndex]
