import unittest
from src.utils2 import generate_passwords

class TestZipCracker(unittest.TestCase):
    def test_generate_passwords(self):
        charset = 'ab'
        max_length = 2
        expected_passwords = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
        generated_passwords = list(generate_passwords(charset, max_length))
        self.assertEqual(generated_passwords, expected_passwords)

    def test_initial_cracker(self):
        from src.zip_cracker import ZipCracker
        cracker = ZipCracker("dummy.zip")
        self.assertIsNone(cracker.crack_password())

if __name__ == '__main__':
    unittest.main()
