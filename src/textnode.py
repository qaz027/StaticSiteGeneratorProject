from enum import Enum

class TextType(Enum):
    PLAIN = "text" #text (plain)
    BOLD = "bold" #**Bold text**
    ITALICS = "italic" #_Italic text_
    CODE = "code" #`Code text`
    LINKS = "link" #Links, in this format: [anchor text](url)
    IMAGES = "images" #Images, in this format: ![alt text](url)

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text & self.text_type == other.text_type & self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
