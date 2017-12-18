import xml.etree.ElementTree as ET

import xml.dom.minidom as minidom


class LexicalWriter(object):
    def __init__(self):
        self.root = ET.Element("class")
        self.subElements = [self.root]
        self.keywords = ['char', 'int', 'boolean', 'void']

    def write(self, token, key = ''):
        if key == '':
            if token in self.keywords:
                key = "keyword"
            else:
                key = "identifier"
        token = " " + token + " "
        ET.SubElement(self.subElements[len(self.subElements)-1],
                      key).text = token
        return

    def openSub(self,name):
        self.subElements.append(ET.SubElement(self.subElements
                                              [len(self.subElements)-1],name))
    def closeSub(self):

        t = self.subElements.pop()
        # patch to support the bug in the origin
        if (not len(list(t))):
            t.append(ET.Element(""))


    def writeXML(self, path):
        tree = ET.ElementTree(self.root)
        self.__indent(self.root)
        a = ET.tostring(self.root, short_empty_elements=False).decode("utf-8")
        #patch to support the bug in the origin
        while (a.find('<></>') != -1):
            idx = a.find('<></>');
            first = a.rfind(">",0,idx)+1
            last = a.find("/>",idx)+2
            a = a.replace(a[first:last],'')

        with open(path,'w') as f:
            f.write(a)


    '''
    copy and paste from http://effbot.org/zone/element-lib.htm#prettyprint
    it basically walks your tree and adds spaces and newlines so the tree is
    printed in a nice way
    '''

    def __indent(self,elem, level=0):
        z = elem.tag
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.__indent(elem, level + 1)
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
    # indent(root)
    tree.write("filename.xml")
