from PushPopParser import PushPopParser


class PointerParser(PushPopParser):
    '''

    '''

    def __init__(self):
        """
        """
        self.ID = "pointer"

    def __parse_pop(self,num,output_ds):
        '''
        :param num:
        :param output_ds:
        :return:
        '''
        # go to last stuck arg
        path = "THAT"
        if num == "0":
            path = "THIS"
        output_ds.append("@SP")
        output_ds.append("A=M-1")
        # remember the value in D
        output_ds.append("D=M")
        output_ds.append("@" + path)
        #update the memorey
        output_ds.append("M=D")
        #update the sp pos
        output_ds.append("@SP")
        output_ds.append("M=M-1")



    def __parse_push(self,num,output_ds):
        '''
        :param num:
        :param output_ds:
        :return:
        '''
        path = "THAT"
        if num == "0":
            path = "THIS"

        output_ds.append("@" + path)
        #Remember this value in D
        output_ds.append("D=M")
        #go to the stuck last pos
        output_ds.append("@SP")
        output_ds.append("A=M")
        #update the stuck
        output_ds.append("M=D")
        #update the suck pointer
        output_ds.append("@SP")
        output_ds.append("M=M+1")

    def parse(self,line,output_ds):
        t = line.split(' ')
        if t[0] == "pop":
            self.__parse_pop(t[2],output_ds)
        else:
            self.__parse_push(t[2],output_ds)

if __name__ == "__main__":
    pass