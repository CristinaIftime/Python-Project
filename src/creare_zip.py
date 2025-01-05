import subprocess
import shutil
import os
import platform
import tempfile

def create_test_zip(zip_path, password, file_to_add='test.txt'):
    # Creează o arhivă ZIP protejată cu parolă folosind 7z.
    # Returnează True dacă arhiva a fost creată cu succes, altfel False.

    # Creează fișierul de test
    with open(file_to_add, 'w', encoding='utf-8') as f:
        f.write("Acesta este un fișier de test.")

    system = platform.system()
    if system == 'Windows':
        seven_z_path = r"C:\Program Files\7-Zip\7z.exe"
    else:
        seven_z_path = '7z'

    if system == 'Windows' and not os.path.isfile(seven_z_path):
        print(f"Eroare: Utilitarul '7z.exe' nu a fost găsit la calea specificată: {seven_z_path}")
        return False

    command = [seven_z_path, 'a', f'-p{password}', '-mem=AES256', zip_path, file_to_add]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Eroare la crearea arhivei ZIP: {result.stderr}")
        return False
    else:
        print("Arhiva ZIP a fost creată cu succes.")
        # Șterge fișierul de test
        os.remove(file_to_add)
        return True

def manual_check(zip_path, password):
    
    #  Verifică manual dacă parola funcționează corect prin extragerea arhivei

    system = platform.system()
    if system == 'Windows':
        seven_z_path = r"C:\Program Files\7-Zip\7z.exe"
    else:
        seven_z_path = '7z'

    if system == 'Windows' and not os.path.isfile(seven_z_path):
        print(f"Eroare: Utilitarul '7z.exe' nu a fost găsit la calea specificată: {seven_z_path}")
        return

    temp_dir = tempfile.mkdtemp()

    try:
        command = [seven_z_path, 'x', f'-p{password}', zip_path, f'-o{temp_dir}', '-y']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("Parola a funcționat corect.")
        else:
            print(f"Eroare la extragere: {result.stderr}")
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    # Creează arhiva ZIP cu parola "ab"
    success = create_test_zip('test.zip', 'ab')

    if success:
        # Verifică manual extragerea arhivei
        manual_check('test.zip', 'ab')
    else:
        print("Crearea arhivei ZIP a eșuat. Nu se poate efectua verificarea manuală.")
