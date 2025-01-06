import string
import subprocess
import shutil
import os
import platform
import tempfile
from utils2 import generate_passwords

class ZipCracker:
    def __init__(self, zip_path, charset=None, max_length=10):
        # Inițializează ZipCracker cu calea către arhiva ZIP, setul de caractere și lungimea maximă a parolei.
        self.zip_path = zip_path
        self.charset = string.ascii_letters + string.digits
        self.max_length = max_length

    def crack_password(self):
        # Încearcă să găsească parola arhivei ZIP folosind brute-force.
        # Returnează parola găsită sau None dacă nu a fost găsită nicio parolă validă.
        system = platform.system()
        if system == 'Windows':
            seven_z_path = r"C:\Program Files\7-Zip\7z.exe"
            if not os.path.isfile(seven_z_path):
                print(f"Eroare: Utilitarul '7z.exe' nu a fost găsit la calea specificată: {seven_z_path}")
                return None
        else:
            seven_z_path = '7z'
            if not shutil.which(seven_z_path):
                print("Eroare: Utilitarul '7z' nu este instalat sau nu este în PATH.")
                return None

        for password in generate_passwords(self.charset, self.max_length):
            with tempfile.TemporaryDirectory() as temp_dir:
                command = [seven_z_path, 'x', f'-p{password}', '-y', self.zip_path, f'-o{temp_dir}']
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    extracted_files = os.listdir(temp_dir)
                    if extracted_files:
                        print(f"Parola găsită: {password}")
                        return password
        print("Nicio parolă validă găsită.")
        return None
