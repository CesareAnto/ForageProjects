import sys
import os
import unittest

# Add src directory to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from forage_module.greetings import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
