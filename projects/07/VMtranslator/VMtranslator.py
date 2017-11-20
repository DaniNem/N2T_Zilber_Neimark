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



if __name__ == "__main__":
    files = []
    if os.path.isfile(sys.argv[1]):  # check if file or directory
        files.append(sys.argv[1])
    else:
        files = [os.path.join(sys.argv[1], dir) for dir in
                 os.listdir(sys.argv[1]) if dir.endswith(".vm")]
    for fileName in files:  # go over the files and convert them to binary
        # form
        print(fileName)
        parserLst = [cp(),ap(),lp(),sp(fileName),tp(),Thisp(),Thatp(),add(),sub()]
        file = fr(fileName)  # open file
        lines = file.get_file()  # get file's lines
        retVal = []
        for line in lines:
            for parser in parserLst:
                if parser.is_triggered(line):
                    parser.parse(line,retVal)
                    break

        saver = fs(os.path.splitext(fileName)[0] + ".asm", retVal)  # save
        # the binary code as .hack file