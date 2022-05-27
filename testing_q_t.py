import unittest

class TestEmptyNode(unittest.TestCase):
    def test_n_empty(self):
        self.assertTrue(self.tail(None))