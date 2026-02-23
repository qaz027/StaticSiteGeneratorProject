from enum import Enum

class TextType(Enum):
    PLAIN = "plain" #text (plain)
    BOLD = "bold" #**Bold text**
    ITALICS = "italics" #_Italic text_
    CODE = "code" #`Code text`
    LINKS = "links" #Links, in this format: [anchor text](url)
    IMAGES = "images" #Images, in this format: ![alt text](url)

class TextNode(text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

    def __eq__(self, other):
        if self.text == other.text & self.text_type == other.text_type & self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text.upper()}, {self.text_type.upper()}, {self.url.upper()})"
