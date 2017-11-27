from BasicArithmeticOp import BasicArithmeticOp as BAO


class Addition(BAO):
    """
    a parser that convert vm addition command to assembly
    """
    def __init__(self):
        """
        initiate operation
        """
        self.OPERATION = "add"
        self.op = "+"
