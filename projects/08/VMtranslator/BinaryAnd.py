from BasicArithmeticOp import BasicArithmeticOp as BAO


class BinaryAnd(BAO):
    """
    a parser that convert vm bitwise and command to assembly
    """

    def __init__(self):
        """
        initiate operation
        """
        self.OPERATION = "and"
        self.op = "&"
