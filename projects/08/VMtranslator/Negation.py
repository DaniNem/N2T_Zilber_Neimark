from OneOperandArithmetic import OneOperandArithmetic as OOA


class Negation(OOA):
    """
    a parser that convert vm negation command to assembly
    """

    def __init__(self):
        """
        initiate operation
        """
        self.OPERATION = "neg"
        self.op = "-"
