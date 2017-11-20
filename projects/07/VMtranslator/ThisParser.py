from PushPopParser import PushPopParser
class ThisParser(PushPopParser):


    def __init__(self):
        """
        """
        self.pos = "THIS"
        self.ID = "this"


if __name__ == "__main__":
    a = ThisParser()
    print(a.is_triggered("pop argument 5"))
    b = []
    a.parse("pop argument 5",b)
    print(b)