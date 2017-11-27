from PushPopParser import PushPopParser


class ThisParser(PushPopParser):
    """
        convert a pop and pop operations of this memory from vm language
        to assembly
    """

    def __init__(self):
        """
            set initial parameters
        """
        self.pos = "THIS"
        self.ID = "this"

