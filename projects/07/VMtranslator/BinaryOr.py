from BaiscArithmeticOp import BaiscArithmeticOp as BAO


class BinaryOr(BAO):
    """
    a parser that convert vm bitwise or command to assembly
    """
    def __init__(self):
        """
        initiate operation
        """
        self.OPERATION = "or"
        self.op = "|"
