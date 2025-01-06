import string
import unittest
import os
from creare_zip import create_test_zip
from zip_cracker import ZipCracker

class TestZipCracker(unittest.TestCase):
    def setUp(self):
        self.zip_path = 'test.zip'
        self.password = 'ab'  

        # Asigură că arhiva nu există înainte de test
        if os.path.exists(self.zip_path):
            os.remove(self.zip_path)

        # Creează arhiva ZIP de test cu parola "ab"
        self.success = create_test_zip(self.zip_path, self.password)

    def tearDown(self):
        # Șterge arhiva ZIP după teste
        if os.path.exists(self.zip_path):
            os.remove(self.zip_path)

    def test_crack_password_success(self):
        # Testează dacă parola corectă este găsită.
        if not self.success:
            self.fail("Crearea arhivei ZIP a eșuat. Testul nu poate fi efectuat.")

        cracker = ZipCracker(self.zip_path, charset=string.ascii_letters + string.digits, max_length=2)
        found_password = cracker.crack_password()
        self.assertEqual(found_password, self.password)

    def test_crack_password_failure(self):
        # Testează cazul în care parola nu este găsită.
        if not self.success:
            self.fail("Crearea arhivei ZIP a eșuat. Testul nu poate fi efectuat.")

        # Creează o instanță a ZipCracker cu charset-ul 'xyz' și max_length=1
        # Deci nu va putea găsi parola 'ab'
        cracker = ZipCracker(self.zip_path, charset='xyz', max_length=1)
        found_password = cracker.crack_password()
        self.assertIsNone(found_password)

if __name__ == '__main__':
    unittest.main()
