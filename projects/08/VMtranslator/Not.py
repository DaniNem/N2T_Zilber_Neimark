from OneOperandArithmetic import OneOperandArithmetic as OOA


class Not(OOA):
    """
    a parser that convert vm negation command to assembly
    """

    def __init__(self):
        """
        initiate operation
        """
        self.OPERATION = "not"
        self.op = "!"
