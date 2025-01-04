import sys
from zip_cracker import ZipCracker

def main():
    if len(sys.argv) != 2:
        print("Utilizare: python main.py <cale_catre_arhiva_zip>")
        sys.exit(1)
    
    zip_path = sys.argv[1]
    cracker = ZipCracker(zip_path)
    
    password = cracker.crack_password()
    
    if password:
        print(f"Parola gasita: {password}")
    else:
        print("Parola nu a fost gasita.")

if __name__ == "__main__":
    main()
