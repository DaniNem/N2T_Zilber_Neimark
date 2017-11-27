from PushPopParser import PushPopParser


class ThatParser(PushPopParser):
    """
        convert a pop and pop operations of that memory from vm language
        to assembly
    """

    def __init__(self):
        """
            set initial parameters
        """
        self.pos = "THAT"
        self.ID = "that"
