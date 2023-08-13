import unittest
from exercise2 import DynCircularQueue

class TestQueue(unittest.TestCase):
    """ Tests for the above class."""
    def test_expand(self) -> None:
        queue = DynCircularQueue()
        for i in range(queue.DEFAULT_MAX_CAPACITY+1):
            queue.append(i)
        for i in range(queue.DEFAULT_MAX_CAPACITY+1):
            self.assertEqual(queue.serve(), i)

if __name__ == '__main__':
    testtorun = TestQueue()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)
