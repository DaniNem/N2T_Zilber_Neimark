from BaiscArithmeticOp import BaiscArithmeticOp as BAO


class Subtraction(BAO):
    """
    a parser that convert vm subtraction command to assembly
    """

    def __init__(self):
        """
        initiate operation
        """
        self.OPERATION = "sub"
        self.op = "-"
