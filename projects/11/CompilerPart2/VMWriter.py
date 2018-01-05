class VMwriter(object):
    """
    write vm code
    """
    def __init__(self, file):
        '''

        :param file: given text file
        '''
        self._f = open(file, 'w')
        self._labelIndex = 0

    def getLabelIndex(self):
        '''

        :return: current index
        '''
        return self._labelIndex

    def incLabelIndex(self):
        '''
        increase index by one
        :return: none
        '''
        self._labelIndex += 1

    def writePush(self, segment, idx):
        '''

        :param segment: given memory segment
        :param idx: index of variable
        :return: none
        '''
        self._f.write("push " + segment + " " + str(idx) + "\n")

    def writePop(self, segment, idx):
        '''

        :param segment: given memory segment
        :param idx: index of variable
        :return: none
        '''
        self._f.write("pop " + segment + " " + str(idx) + "\n")

    def writeAritmetic(self, command):
        '''

        :param command: arithmetic command
        :return: none
        '''
        self._f.write(command + "\n")

    def writeLabel(self, lable):
        '''
        write a vm label
        :param lable: given label
        :return: none
        '''
        self._f.write("label " + lable + "\n")

    def writeGoTo(self, label):
        '''
        write go to command
        :param label: given label
        :return: none
        '''
        self._f.write("goto " + label + "\n")

    def writeIf(self, label):
        '''
        write if command
        :param label: given label
        :return: none
        '''
        self._f.write("if-goto " + label + "\n")

    def writeCall(self, name, nArgs):
        '''
        write function call command
        :param name: given function name
        :param nArgs: number of arguments
        :return: none
        '''
        self._f.write("call " + name + " " + str(nArgs) + "\n")

    def writeFunction(self, name, nLocals):
        '''
        declare a function
        :param name: function's name
        :param nLocals: number of local variables
        :return: none
        '''
        self._f.write("function " + name + " " + str(nLocals) + "\n")

    def writeReturn(self):
        '''
        write return statement
        :return: none
        '''

        self._f.write("return" + "\n")

    def close(self):
        '''
        close vm file
        :return: none
        '''
        self._f.close()


if __name__ == '__main__':
    wr = VMwriter('test.vm')
    wr.writePush("CONST", "1")
    wr.writePop("LOCAL", "3")
    wr.writeAritmetic("ADD")
    wr.writeLabel("label1")
    wr.writeGoTo("label2")
    wr.writeIf("label3")
    wr.writeCall("pipi", "2")
    wr.writeFunction("kaki", "2")
    wr.writeReturn()
    wr.close()
