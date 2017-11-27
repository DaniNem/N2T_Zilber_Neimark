class StaticParser(object):


    def __init__(self):
        """
        """
        self.fileName = ""
        self.ID = "static"

    def is_triggered(self,line):
        '''

        :return:
        '''
        return self.ID in line

    def set_params(self,file_name):
        self.fileName  = file_name

    def parse_pop(self,num,output_ds):
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
        # Go to static var NUM
        output_ds.append("@" +self.fileName + '.' + str(num) )
        #update the memorey
        output_ds.append("M=D")
        #update the sp pos
        output_ds.append("@SP")
        output_ds.append("M=M-1")



    def parse_push(self,num,output_ds):
        '''

        :param num:
        :param output_ds:
        :return:
        '''
        # Go to static var NUM
        output_ds.append("@" +self.fileName + '.' + str(num) )
        #Remember this value in D
        output_ds.append("D = M")
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
            self.parse_pop(t[2],output_ds)
        else:
            self.parse_push(t[2],output_ds)



if __name__ == "__main__":
    pass