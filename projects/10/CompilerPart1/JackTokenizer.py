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
        f1 = False
        f2 = False
        nextInter = []
        symbols = ['{', '}', '.', '(', ')', '[', ']', ',', ';', '+', '-', '*',
                   '&', '<', '>', '=', '~', '\n', '\t']
        for token in ftokens:
            # remove comments
            if (token == ' ' or token == '' or token == '\n'):
                continue
            if (token.startswith('/*')):
                f1 = True
                continue
            if (token.startswith('*/')):
                f1 = False
                continue
            if (token == r'//'):
                f2 = True
                continue
            if (f2 and '\n' in token):
                f2 = False
                continue
            if (not f1 and not f2):
                nextInter.append(token)
        nextIter1 = []
        for t in nextInter:
            temp = list(t)
            indices = []
            for s in symbols:
                indices.extend([i for i, x in enumerate(temp) if x == s])
            indices.sort()
            if len(indices) > 0:
                i = 0
                for n in indices:
                    nextIter1.append(t[i:n])
                    nextIter1.append(t[n:n + 1])
                    i = n + 1
                nextIter1.append(t[i:])
            else:
                nextIter1.append(t)

        for i in nextIter1:
            if (i != '' and i != '\n' and i != '\t'):
                self.data.append(i)

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
    test = JackTokenizer(file)
    print(test.get_token())
    test.next()
    print(test.get_token())
    print(test.data)
