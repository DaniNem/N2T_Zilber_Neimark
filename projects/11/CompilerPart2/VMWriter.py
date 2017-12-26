class VMwriter(object):
    def __init__(self,file):
        '''

        :param file: text
        '''
        self._f = open(file,'w')
        self._labelIndex = 0
    def getLabelIndex(self):
        '''

        :return:
        '''
        return self._labelIndex
    def incLabelIndex(self):
        '''

        :return:
        '''
        self._labelIndex += 1
    def writePush(self,segment,idx):
        '''

        :param segment:
        :param idx:
        :return:
        '''
        self._f.write("push "+segment+" "+str(idx) + "\n")

    def writePop(self,segment,idx):
        '''

        :param segment:
        :param idx:
        :return:
        '''
        self._f.write("pop " + segment + " " + str(idx) + "\n")

    def writeAritmetic(self,command):
        '''

        :param command:
        :return:
        '''
        self._f.write(command + "\n")

    def writeLabel(self,lable):
        '''

        :param lable:
        :return:
        '''
        self._f.write("lable " + lable +"\n")
    def writeGoTo(self,label):
        '''

        :param label:
        :return:
        '''
        self._f.write("goto " + label + "\n")
    def writeIf(self,label):
        '''

        :param label:
        :return:
        '''
        self._f.write("if-goto " + label + "\n")
    def writeCall(self,name,nArgs):
        '''

        :param name:
        :param nArgs:
        :return:
        '''
        self._f.write("call " + name + " " + str(nArgs) + "\n")
    def writeFunction(self,name,nLocals):
        '''

        :param name:
        :param nLocals:
        :return:
        '''
        self._f.write("function " + name + " " + str(nLocals) + "\n")

    def writeReturn(self):
        '''

        :return:
        '''

        self._f.write("return"+"\n")
    def close(self):
        '''

        :return:
        '''
        self._f.close();


if __name__ == '__main__':
    wr = VMwriter('test.vm')
    wr.writePush("CONST","1")
    wr.writePop("LOCAL","3")
    wr.writeAritmetic("ADD")
    wr.writeLabel("label1")
    wr.writeGoTo("label2")
    wr.writeIf("label3")
    wr.writeCall("pipi","2")
    wr.writeFunction("kaki","2")
    wr.writeReturn()
    wr.close()