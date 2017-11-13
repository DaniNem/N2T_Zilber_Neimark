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
    """
    :return: a pre define symbols dictionary
    """
    return {"SP": "0", "LCL": "1", "ARG": "2", "THIS": "3", "THAT": "4",
            "R0": "0"
        , "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5"
        , "R6": "6", "R7": "7", "R8": "8", "R9": "9", "R10": "10",
            "R11": "11",
            "R12": "12", "R13": "13", "R14": "14", "R15": "15",
            "SCREEN": "16384",
            "KBD": "24576"}


if __name__ == "__main__":
    files = []
    if os.path.isfile(sys.argv[1]):  # check if file or directory
        files.append(sys.argv[1])
    else:
        files = [os.path.join(sys.argv[1],dir) for dir in os.listdir(sys.argv[1]) if dir.endswith(".asm")]
                 if dir.endswith(".asm")]
    for fileName in files:  # go over the files and convert them to binary
        # form
        symbols = initSymbols()  # get pre define symbols
        file = fr(fileName)  # open file
        commentH = cm()
        whiteSpaceH = wsh()
        jumpStat = js()
        varAlloc = va()
        a = ai()
        c = ccp()
        lines = file.get_file()  # get file's lines
        commentH.run(lines, symbols)  # remove comments
        whiteSpaceH.run(lines, symbols)  # remove white spaces
        jumpStat.run(lines, symbols)  # remove jump statements and add them
        # to the symbols dictionary
        varAlloc.run(lines, symbols)  # convert the variable names to
        # appropriate registers
        a.run(lines, symbols)  # convert a instructions to binary form
        c.run(lines, symbols)  # convert c instructions to binary form
        saver = fs(os.path.splitext(fileName)[0] + ".hack", lines)  # save
        # the binary code as .hack file
