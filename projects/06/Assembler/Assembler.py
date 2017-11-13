
import sys
import os
from FileReader import FileReader as fr
from JumpStatements import JumpStatements as js
from AInstruction import AInstruction as ai
from FileSaver import FileSaver as fs
from CommentHandler import CommentHandler as cm
from WhiteSpaceHandler import WhiteSpaceHandler as wsh
from VariableAllocator import VariableAllocator as va
from CCommandParser import CCommandParser as ccp


def initSymbols():
    return {"SP":"0","LCL":"1","ARG":"2","THIS":"3","THAT":"4","R0":"0"
        , "R1": "1","R2":"2","R3":"3","R4":"4","R5":"5"
        , "R6": "6","R7":"7","R8":"8","R9":"9","R10":"10","R11":"11",
            "R12":"12","R13":"13","R14":"14","R15":"15","SCREEN":"16384",
            "KBD":"24576"}

if __name__ == "__main__":
    files = []
    if os.path.isfile(sys.argv[1]):
        files.append(sys.argv[1])
    else:
        files = [sys.argv[1]+"\\"+dir for dir in os.listdir(sys.argv[1]) if dir.endswith(".asm")]
    for fileName in files:
        #print("!!!!!!")
        #print(os.path.splitext(fileName)[0])
        #print(os.path.splitext(fileName)[1])
        #print(fileName)
        #sprint("@@@@@@")
        symbols = initSymbols()
        file = fr(fileName)
        commentH = cm()
        whiteSpaceH = wsh()
        jumpStat = js()
        varAloc = va()
        a = ai()
        c = ccp()
        lines = file.get_file()
        commentH.run(lines,symbols)
        whiteSpaceH.run(lines,symbols)
        jumpStat.run(lines,symbols)
        varAloc.run(lines,symbols)
        a.run(lines,symbols)
        c.run(lines,symbols)
        saver = fs(os.path.splitext(fileName)[0]+".hack",lines)
