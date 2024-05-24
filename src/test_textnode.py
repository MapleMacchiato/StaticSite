import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is a text node", "bold", "www.test.com")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a first text node", "bold")
        node2 = TextNode("This is a second text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_style(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "normal")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
          unittest.main()
      
      
     
    
