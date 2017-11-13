class CommentHandler(object):
    '''
    This class is responsible  for Comment handling
    '''

    def __init__(self):
        self.COMMENT = "//"
    def run(self,lst,table = {}):
        templst = []
        for line in lst:
            if self.COMMENT in line:
                pos = line.find(self.COMMENT)
                if  pos != 0:
                    templst.append(line[0:pos])
            else:
                templst.append(line)
        lst.clear()
        lst.extend(templst)

if __name__ == "__main__":
    lst = ["D=D+1 //test","//remove me","@15","@R1"]
    cH = CommentHandler()
    print(lst)
    cH.run(lst)
    print(lst)