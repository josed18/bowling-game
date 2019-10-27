import unittest
from api.score.services import calculate_score

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calculate_score('XXXXXXXXXXXX'), 300)
        self.assertEqual(calculate_score('5/5/5/5/5/5/5/5/5/5/5'), 150)
        self.assertEqual(calculate_score('9-9-9-9-9-9-9-9-9-9-'), 90)


if __name__ == '__main__':
    unittest.main()
