import unittest
from __init__ import list_to_df, null_check, simple_func


class FuncTests(unittest.TestCase):
    """
    tests functions found int __init__.py
    """
    def test_one(self):
        self.assertEqual(simple_func(-5), 5)
        self.assertEqual(simple_func(6), 6)


if __name__ == '__main__':
    unittest.main()
