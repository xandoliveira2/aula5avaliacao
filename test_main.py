
import unittest
from main import fatorial

class TestCalculadora(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(5), 120)



if __name__ == "__main__":
    unittest.main()
