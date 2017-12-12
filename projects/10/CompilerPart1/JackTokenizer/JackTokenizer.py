class JackTokenizer(object):
    def __init__(self,path):
        self.currentIndex = 0
        self.data = []
        ftokens = []
        with open(path,'r') as f:
            for line in f.readlines():
                ftokens.extend(line.split(' '))
        f = False
        nextInter = []
        symbols = ['{' , '}' ,'.','(' , ')' , '[' , ']' , ',' , ';' , '+' , '-' , '*' , '/' , '&' , ',' , '<' , '>' , '=' , '~','\n']
        for token in ftokens:
            #remove comments
            if (token == ' ' or token == '' or token == '\n'):
                continue
            if (token.startswith('/*')):
                f = True
                continue
            if (token.startswith('*/')):
                f = False
                continue
            if (token == r'//'):
                f = True
                continue
            if (f and '\n' in token ):
                f = False
                continue
            if (not f):
                nextInter.append(token)
        nextIter1 = []
        for t in nextInter:
            temp = list(t)
            indices = []
            for s in symbols:
                indices.extend([i for i, x in enumerate(temp) if x == s])
            indices.sort();
            if len(indices) > 0:
                i = 0
                for n in indices:
                    nextIter1.append(t[i:n])
                    nextIter1.append(t[n:n+1])
                    i = n+1
            else:
                nextIter1.append(t)

        for i in nextIter1:
            if (i != '' and i != '\n'):
                self.data.append(i)

    def hasNext(self):
        return (self.currentIndex == len(self.data)-1)
    def next(self):
        self.currentIndex+=1
    def prev(self):
        self.currentIndex += 1
    def get_token(self):
        return self.data[self.currentIndex];

if __name__ == '__main__':
    file = r'C:\Users\Admin\Desktop\nand2tetris\projects\10\danielTest\Main.jack'
    test = JackTokenizer(file)
    print(test.get_token())
    test.next()
    print(test.get_token())