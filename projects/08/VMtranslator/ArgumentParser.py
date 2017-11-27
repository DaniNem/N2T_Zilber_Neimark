from PushPopParser import PushPopParser
class ArgumentParser(PushPopParser):


    def __init__(self):
        """
        """
        self.pos = "ARG"
        self.ID = "argument"


if __name__ == "__main__":
    a = ArgumentParser()
    print(a.is_triggered("pop argument 5"))
    b = []
    a.parse("pop argument 5",b)
    print(b)