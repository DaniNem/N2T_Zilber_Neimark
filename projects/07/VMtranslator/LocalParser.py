from PushPopParser import PushPopParser
class LocalParser(PushPopParser):


    def __init__(self):
        """
        """
        self.pos = "LCL"
        self.ID = "local"


if __name__ == "__main__":
    a = LocalParser()
    print(a.is_triggered("pop argument 5"))
    b = []
    a.parse("pop argument 5",b)
    print(b)