from PushPopParser import PushPopParser


class ArgumentParser(PushPopParser):
    """
        parse a constant push/pop command to assembly
    """
    def __init__(self):
        """
            initiate arguments
        """
        self.pos = "ARG"
        self.ID = "argument"
