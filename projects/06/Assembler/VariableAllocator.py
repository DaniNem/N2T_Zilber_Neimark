class VariableAllocator(object):
    '''
    This class is responsible  for allocating variables and replacing the symbols
    '''
    def __init__(self):
        self.AT = "@"
        self.NextFreeMemory = 16
    def run(self,lst,table):
        templst = []
        for line in lst:
            if self.AT in line and not line[1:].isdigit():
                addr = line[1:]
                if not addr in table:
                    table[addr] = self.NextFreeMemory;
                    self.NextFreeMemory+=1
                templst.append("@" + str(table[addr]))
            else:
                templst.append(line)
        lst.clear()
        lst.extend(templst)

if __name__ == "__main__":
    lst = ["D=D+1","@58","@i","@R1","@Re3"]
    dic = {"R1":"8"}
    vA = VariableAllocator()
    print(lst)
    vA.run(lst,dic)
    print(lst)
    print(dic)