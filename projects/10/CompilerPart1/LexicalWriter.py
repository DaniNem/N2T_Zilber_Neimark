import xml.etree.cElementTree as ET


class LexicalWriter(object):
    def __init__(self):
        self.root = ET.Element("class")
        self.subElements = [self.root]
        self.keywords = ['char','int','boolean','void']

    def write(self, token, key = ''):
        if token in self.keywords:
            key = "keyword"
        else:
            key = "identifier"
        ET.SubElement(self.subElements[len(self.subElements)-1],
                      key).text = token
        return

    def openSub(self,name):
        self.subElements.append(ET.SubElement(self.subElements//
                                              [len(self.subElements)-1],name))
    def closeSub(self):
        self.subElements.pop();

    def writeXML(self,path):
        tree = ET.ElementTree(self.root)
        #print(tree.getroot().items())
        self.indent(self.root)
        tree.write(path)
    def indent(self,elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

if __name__ == "__main__":
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")

    ET.SubElement(doc, "field1", name="blah").text = "some value1"
    ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

    tree = ET.ElementTree(root)
    #indent(root)
    tree.write("filename.xml")