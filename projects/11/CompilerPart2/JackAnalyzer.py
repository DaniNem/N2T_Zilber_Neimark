from ClassParser import ClassParser as cp
from LexicalWriter import LexicalWriter as lw
from JackTokenizer import JackTokenizer as JT

import sys
import os
if __name__ == "__main__":
    #empty file list
    files = []
    #The results
    retVal = []
    if os.path.isfile(sys.argv[1]):  # check if file or directory
        files.append(sys.argv[1])
    else:
        files = [os.path.join(sys.argv[1], dir) for dir in
                 os.listdir(sys.argv[1]) if dir.endswith(".jack")]
    for fileName in files:  # go over the files and convert them
        writer = lw()
        tokenizer = JT(fileName)
        a = cp(tokenizer, writer)
        a.run()
        writer.writeXML(fileName.replace(".jack",".xml"))
