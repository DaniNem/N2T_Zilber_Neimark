from ConditionsOp import ConditionsOp as CO


class GTop(CO):
    """
    a parser that convert vm > command to assembly
    """

    def __init__(self):
        """
        initiate operation
        """
        self.jump_condition = "JLT"
