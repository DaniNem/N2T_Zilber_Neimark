class PushPopParser(object):
    """
    a base class of push and pop command conversion to assembly
    """
    def is_triggered(self, line):
        """
        :param line: line of vm code
        :return: true if the line belongs to a certain memory segment
        """
        return self.ID in line
    def set_params(self,file_name,func_name):
        pass
    def __parse_pop(self, num, output_ds):
        """
        convert pop command in vm code to assembly
        :param num: number of line in order to give appropriate jump
        statement
        :param output_ds: post translation code
        :return: null
        """

        output_ds.append("@" + self.pos)
        output_ds.append("D=M")
        output_ds.append("@" + str(num))
        output_ds.append("D=A+D")

        # remember the address in R13
        output_ds.append("@R13")
        output_ds.append("M=D")

        # go to last stuck arg
        output_ds.append("@SP")
        output_ds.append("A=M-1")
        # remember the value in D
        output_ds.append("D=M")
        output_ds.append("@R13")
        output_ds.append("A=M")
        # update the memorey
        output_ds.append("M=D")
        # update the sp pos
        output_ds.append("@SP")
        output_ds.append("M=M-1")

    def __parse_push(self, num, output_ds):
        """
         convert push command in vm code to assembly
         :param num: number of line in order to give appropriate memory
         variable name
         statement
         :param output_ds: post translation code
         :return: null
        """
        output_ds.append("@" + self.pos)
        output_ds.append("D=M")
        output_ds.append("@" + str(num))
        output_ds.append("A=A+D")
        # Remember this value in D
        output_ds.append("D=M")
        # go to the stuck last pos
        output_ds.append("@SP")
        output_ds.append("A=M")
        # update the stuck
        output_ds.append("M=D")
        # update the suck pointer
        output_ds.append("@SP")
        output_ds.append("M=M+1")

    def parse(self, line, output_ds):
        """
        translate pop/push command in vm language to assembly
        :param line: a given vm line
        :param output_ds: post translation code
        :return: null
        """
        t = line.split(' ')
        if t[0] == "pop":
            self.__parse_pop(t[2], output_ds)
        else:
            self.__parse_push(t[2], output_ds)
