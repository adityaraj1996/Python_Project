import unittest
# importing the testing module
import cap

class TestCap(unittest.TestCase):

    def test_cap(self):
        text = 'aditya raj'
        result = cap.cap(text)
        self.assertEqual(result,'Aditya Raj')


if __name__ ==  '__main__':
    unittest.main()

