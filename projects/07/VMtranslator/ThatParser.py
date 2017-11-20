from PushPopParser import PushPopParser
class ThatParser(PushPopParser):


    def __init__(self):
        """
        """
        self.pos = "THAT"
        self.ID = "that"


if __name__ == "__main__":
    a = ThatParser()
    print(a.is_triggered("pop argument 5"))
    b = []
    a.parse("pop argument 5",b)
    print(b)