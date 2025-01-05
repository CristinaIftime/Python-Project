import string 
from utils2 import generate_passwords

class ZipCracker:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.charset = string.ascii_letters + string.digits  # Alfanumeric
        self.max_length = 10

    def crack_password(self):
    #    Metodă temporară pentru a testa generatorul de parole.
        for password in generate_passwords(self.charset, self.max_length):
            print(f"Încerc parola: {password}")
            # Aici va fi logica de testare a parolei
        return None
