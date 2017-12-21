class JackTokenizer(object):
    def __init__(self, path):
        self.currentIndex = 0
        self.data = []
        ftokens = []
        with open(path, 'r') as f:
            for line in f.readlines():
                if ('"' in line):
                    flag = True
                    while flag:
                        idx = line.find('"')
                        ftokens.extend(line[:idx].split(' '))
                        line = line[idx:]
                        idx = line.find('"',1) + 1
                        if(idx == 0 ):
                            #this can happen only in a comment
                            ftokens.extend(line.split(' '))
                            break;
                        ftokens.append(line[:idx])
                        line = line[idx:]
                        if line.find('"') == -1:
                            flag = False
                            ftokens.extend(line[:idx].split(' '))
                else:
                    ftokens.extend(line.split(' '))
        symbols = ['{', '}', '.', '(', ')', '[', ']', ',', ';', '+', '-', '*',
                   '&', '<', '>', '=', '~', '\n', '\t','/']

        splitTok = []
        for t in ftokens:
            temp = list(t)
            indices = []
            for s in symbols:
                indices.extend([i for i, x in enumerate(temp) if x == s])
            indices.sort()
            if len(indices) > 0 and '"' not in t:
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
        i = 0
        while i < len(splitTok):
            if (splitTok[i] == '/' ):
                if (splitTok[i+1] == '/'):
                    i += 2
                    f1 = True
                    continue
                if (splitTok[i+1] == '*'):
                    i += 2
                    f2 = True
                    continue
            if (f1 and splitTok[i] == '\n'):
                f1 = False
                i += 1
                continue
            if (f2 and splitTok[i] == '*'):
                if (splitTok[i+1] == '/'):
                    f2 = False
                    i += 2
                    continue

            if (not f1 and not f2 and splitTok[i] != '' and splitTok[i] != '\t' and splitTok[i] != '\n'):
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


if __name__ == '__main__':
    # file = r'C:\Users\Admin\Desktop\nand2tetris\projects\10\danielTest\Main.jack'
    file = r"C:\Users\Admin\Desktop\nand2tetris\projects\10\Square\SquareGame.jack"
    file = r"C:\Users\Admin\Desktop\nand2tetris\projects\10\tests\1\Cannon.jack"
    test = JackTokenizer(file)
    print(test.get_token())
    test.next()
    print(test.get_token())
    print(test.data)

