from lxml import etree

from constants import XML_TAG, XML_TAG_ATTRIBUTE

class LexicalResourceModel:
    def __init__(self):
        self.path = ""
        # self.schema = etree.XMLSchema("")
        self.tree = None
        self._element_index = {}

    def open(self, path=None):
        if path:
            self.tree = etree.parse(path)
            
            # self.schema.assert_(etree)

            self.path = path
        elif path == "":
            return
        else:
            root = etree.Element(XML_TAG.LEXICAL_RESOURCE)

            root.set(XML_TAG_ATTRIBUTE.LEXICAL_RESOURCE.TITLE, 'Sin título')

            self.tree = etree.ElementTree(root)

            self.path = ""

        self._build_element_index()

    def get_entries_count(self):
        if self.tree is None:
            return 0
        return sum(1 for _ in self.tree.iter(XML_TAG.ENTRY))

    def get_element_by_id(self, id):
        return self._element_index.get(id)

    def get_root_element(self):
        return self.tree.getroot() if self.tree is not None else None

    def write(self, path=None):
        if self.tree is None:
            return
        
        path = path if path else self.path
        self.tree.write(
            path,
            encoding="utf-8",  # Fixed typo
            xml_declaration=True,
            pretty_print=True)

    def close(self):
        self.path = ""
        self.tree = None
        self._element_index.clear()
        
    def _build_element_index(self):
        self._element_index.clear()

        if self.tree is not None:
            for element in self.tree.iter():
                self._element_index[id(element)] = element
