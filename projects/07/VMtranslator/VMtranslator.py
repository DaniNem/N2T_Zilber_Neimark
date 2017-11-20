import os
import sys

from FileReader import FileReader as fr
from FileSaver import FileSaver as fs
from ArgumentParser import ArgumentParser as ap
from LocalParser import LocalParser as lp
from StaticParser import StaticParser as sp
from TempParser import TempParser as tp
from ThisParser import ThisParser as Thisp
from ThatParser import ThatParser as Thatp
from Addition import Addition as add
from Subtraction import Subtraction as sub
from ConstantParser import ConstantParser as cp
from EqualOp import EqualOp as eq
from GTop import GTop as gt
from LTop import LTop as lt
from BinaryAnd import BinaryAnd as ba
from BinaryOr import BinaryOr as bo
from Not import Not as nt
from Negation import Negation as ng
from CommentHandler import CommentHandler
from PointerParser import PointerParser as pp




if __name__ == "__main__":
    files = []
    if os.path.isfile(sys.argv[1]):  # check if file or directory
        files.append(sys.argv[1])
    else:
        files = [os.path.join(sys.argv[1], dir) for dir in
                 os.listdir(sys.argv[1]) if dir.endswith(".vm")]
    for fileName in files:  # go over the files and convert them to binary
        # form
        onlyFileName = os.path.basename(fileName).strip(".vm")
        parserLst = [cp(),ap(),lp(),sp(onlyFileName),tp(),Thisp(),Thatp()
            ,add(),sub(),eq(),gt(),lt(),ba(),bo(),nt(),ng(),pp()] #
        file = fr(fileName)  # open file
        lines = file.get_file()  # get file's lines
        CommentHandler(lines)
        retVal = []
        for line in lines:
            for parser in parserLst:
                if parser.is_triggered(line):
                    parser.parse(line,retVal)
                    break

        saver = fs(os.path.splitext(fileName)[0] + ".asm", retVal)  # save
        # the binary code as .hack file