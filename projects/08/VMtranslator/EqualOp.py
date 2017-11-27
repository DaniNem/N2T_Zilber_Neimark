from ConditionsOp import ConditionsOp as CO


class EqualOp(CO):
    """
    a parser that convert vm == command to assembly
    """

    def __init__(self):
        """
        initiate operation
        """
        self.jump_condition = "JNE"
        self.OPERATION = "eq"
