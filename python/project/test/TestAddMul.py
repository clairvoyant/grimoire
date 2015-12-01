#!/usr/bin/python


import unittest
import addmul


class TestAddMul(unittest.TestCase):
    """Unit tests for add mul, an example project."""

    def test_basic(self):
        """test the basic result of add/mul."""
        result = addmul.AddMul([1,2],[3,4])
        self.assertEqual(result.do(), [3,8])

if __name__ == "__main__":
    unittest.main()



