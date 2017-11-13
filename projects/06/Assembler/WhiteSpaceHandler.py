class WhiteSpaceHandler(object):
    '''
    This class is responsible  for white space handling
    '''
    def __init__(self):
        self.WhiteSpace = " "
    def run(self,lst,table = {}):
        templst = []
        for line in lst:
            line = line.replace(" ","")
            if line != "":
                templst.append(line)
        lst.clear()
        lst.extend(templst)

if __name__ == "__main__":
    lst = ["D=D+1 ","","@15","@R1   "]
    cH = WhiteSpaceHandler()
    print(lst)
    cH.run(lst)
    print(lst)