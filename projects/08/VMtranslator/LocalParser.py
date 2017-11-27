from PushPopParser import PushPopParser


class LocalParser(PushPopParser):
    """
        convert a pop and pop operations of local memory from vm language
        to assembly
    """

    def __init__(self):
        """
            set parameters
        """
        self.pos = "LCL"
        self.ID = "local"
