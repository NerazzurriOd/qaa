from xml.etree import ElementTree


class XMLProcessor:
    def __init__(self):
        self.root = None

    def to_string(self, root):
        return ElementTree.tostring(root, encoding="unicode")

    def from_string(self, xml_string):
        return ElementTree.fromstring(xml_string)

    def update_all_elements(self, root, tag, value):
        for element in root.iter():
            if element.tag == tag:
                element.text = value
        return root

    def add_new_element(self, root, parent_elem, new_elem, elem_value):
        for element in root.findall(parent_elem):
            new_element = ElementTree.Element(new_elem)
            new_element.text = elem_value
            element.append(new_element)
        return root


if __name__ == '__main__':
    processor = XMLProcessor()
    tree = ElementTree.parse('example.xml')
    root = tree.getroot()
    string_root = processor.to_string(root)
    print(string_root)
