from PushPopParser import PushPopParser


class TempParser(PushPopParser):
    '''

    '''

    def __init__(self):
        """
        """
        self.map = ["R5","R6","R7","R8","R9","R10","R11","R12"]
        self.ID = "temp"

    def __parse_pop(self,num,output_ds):
        '''
        :param num:
        :param output_ds:
        :return:
        '''
        # go to last stuck arg
        output_ds.append("@SP")
        output_ds.append("A=M-1")
        # remember the value in D
        output_ds.append("D=M")
        output_ds.append("@" + self.map[int(num)])
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
        output_ds.append("@" + self.map[int(num)])
        #Remember this value in D
        output_ds.append("D=M")
        #go to the stuck last pos
        output_ds.append("@SP")
        output_ds.append("A=M")
        #update the stuck
        output_ds.append("M=D")
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
    a = TempParser()
    print(a.is_triggered("pop temp 5"))
    b = []
    a.parse("pop temp 7",b)
    print(b)