import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is another text node", TextType.IMAGES, url="www.bubbles.com")
        node2 = TextNode("This is another text node", TextType.LINKS, url="www.bubbles2.com")
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is another text node", TextType.IMAGES)
        node2 = TextNode("This is another text node", TextType.IMAGES, url="www.bubbles2.com")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
