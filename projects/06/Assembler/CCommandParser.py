'''
This class is responsible  for parsing C commands
'''
class CCommandParser(object):

    def __init__(self):
        self.EQUAL = "="
        self.SEMICOLON = ";"
        self.BARKER = "1"
        self.comp = {"0":"110101010","1":"110111111","-1":"110111010",
                     "D":"110001100","A":"110110000","M":"111110000",
                     "!D":"110001101","!A":"110110001","!M":"111110001",
                     "-D":"110001111","-A":"110110011","-M": "111110011",
                     "D+1":"110011111","A+1":"110110111","M+1":"111110111",
                     "D-1":"110001110","A-1":"110110010","M-1":"111110010",
                     "D+A":"110000010","D+M":"111000010","D-A":"110010011",
                     "D-M":"111010011","A-D":"110000111","M-D":"111000111",
                     "D&A":"110000000","D&M":"111000000","D|A":"110010101",
                     "D|M":"111010101","D<<":"010110000","D>>":"010010000",
                     "A<<":"010100000","A>>":"010000000","M<<":"011100000",
                     "M>>":"011000000"
                     }
        self.dest = {"null":"000","":"000","M":"001","D":"010","MD":"011",
                     "A":"100","AM":"101","AD":"110","AMD":"111"}
        self.jump = {"null":"000","":"000","JGT":"001","JEQ":"010","JGE":"011",
                     "JLT":"100","JNE":"101","JLE":"110","JMP":"111"}
    def run(self,lst,table = {}):
        for lineIdx in range(len(lst)):
            if self.EQUAL in lst[lineIdx] or self.SEMICOLON in lst[lineIdx]:
                if self.EQUAL in lst[lineIdx] and \
                                self.SEMICOLON in lst[lineIdx]:
                    #in case
                    t = lst[lineIdx].split(self.EQUAL)
                    dest = t[0]
                    t2 = t.split(self.SEMICOLON)
                    comp = t2[0]
                    jump = t2[1]
                elif self.EQUAL in lst[lineIdx]:
                    jump = "null"
                    t = lst[lineIdx].split(self.EQUAL)
                    dest = t[0]
                    comp = t[1]

                else:
                    t = lst[lineIdx].split(self.SEMICOLON)
                    dest = "null"
                    comp = t[0]
                    jump = t[1]
                lst[lineIdx] = self.BARKER + self.comp[comp] +\
                               self.dest[dest] + self.jump[jump]

if __name__ == "__main__":
    pass