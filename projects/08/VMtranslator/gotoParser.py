class GotoParser(object):
    def __init__(self):
        """
        """
        self.file_name = ""
        self.function_name = ""
        self.ID = "goto"

    def is_triggered(self,line):
        '''

        :return:
        '''
        return line.startswith(self.ID)


    def set_params(self,file_name,func_name):
        self.file_name  = file_name
        self.function_name  = func_name

    def parse(self,line,output_ds):
        t = line.split(' ')
        label = self.file_name + "." + self.function_name +"$"+ t[1]
        output_ds.append("@" + label)
        output_ds.append(";JMP")

if __name__ == "__main__":
    pass