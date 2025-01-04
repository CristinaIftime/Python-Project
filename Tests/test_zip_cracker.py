import unittest
from src.zip_cracker import ZipCracker

class TestZipCracker(unittest.TestCase):
    def test_initial(self):
        # Test inițial
        cracker = ZipCracker("dummy.zip")
        self.assertIsNone(cracker.crack_password())

if __name__ == '__main__':
    unittest.main()
