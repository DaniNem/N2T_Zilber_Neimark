from FileReader import FileReader as fr
from JumpStatements import JumpStatements as js
from AInstruction import AInstruction as ai
from FileSaver import FileSaver as fs



if __name__ == "__main__":
    file = fr("./test1.txt")
    lines = file.get_file()
    file = js(lines, {})
    file.run()
    print(file.symbols)
    a = ai(lines)
    a.run()
    a.print_it()
    fs(a.lines)
