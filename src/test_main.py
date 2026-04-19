import unittest
from main import main, extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        matches = extract_title('# Hello, World!')
        self.assertEqual('Hello, World!', matches)

if __name__ == "__main__":
    unittest.main()

