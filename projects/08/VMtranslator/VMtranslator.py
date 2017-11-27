#imports
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



#the main
if __name__ == "__main__":
    #empty file list
    files = []
    #The results
    retVal = []
    funcName = ''
    if os.path.isfile(sys.argv[1]):  # check if file or directory
        files.append(sys.argv[1])
        #determine the output name
        outPutName =sys.argv[1].replace(".vm",".asm")
    else:
        files = [os.path.join(sys.argv[1], dir) for dir in
                 os.listdir(sys.argv[1]) if dir.endswith(".vm")]
        # determine the output name
        outPutName = os.path.join(sys.argv[1]
                                  , os.path.basename(sys.argv[1]).strip(
                ".vm") + ".asm")
    for fileName in files:  # go over the files and convert them
        onlyFileName = os.path.basename(fileName).strip(".vm")
        #init every parser
        parserLst = [cp(),ap(),lp(),sp(),tp(),Thisp(),Thatp()
            ,add(),sub(),eq(),gt(),lt(),ba(),bo(),nt(),ng(),pp()] #
        file = fr(fileName)  # open file
        lines = file.get_file()  # get file's lines
        CommentHandler(lines)
        #parse and translate!
        for line in lines:
            #TODO add function parser
            #TODO add return parser
            for parser in parserLst:
                if parser.is_triggered(line):
                    parser.set_params(onlyFileName,funcName)
                    parser.parse(line,retVal)
                    break
    saver = fs(outPutName, retVal)  # save