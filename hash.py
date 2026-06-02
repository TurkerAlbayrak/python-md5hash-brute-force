import hashlib

def brute_force_hash(target_hash, wordlist_file):
    print("[*] Brute Force işlemi başlatılıyor...")
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # Satır sonundaki boşlukları ve yeni satır karakterlerini temizle
                password = line.strip()
                
                # Şifrenin MD5 hash'ini al
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                
                # Hedef hash ile eşleşiyor mu kontrol et
                if hashed_password == target_hash:
                    print(\n[+] Şifre Bulundu!: {password})
                    return password
                    
        print("\n[-] Maalesef şifre listede bulunamadı.")
        return None
        
    except FileNotFoundError:
        print(f"[-] Hata: '{wordlist_file}' dosyası bulunamadı!")

# --- KULLANIM ---
# Denemek için 'admin123' şifresinin MD5 hash'i: 0192023a7bbd73250516f069df18b500
hedef_hash = "0192023a7bbd73250516f069df18b500" 
sifre_listesi = "passwords.txt" # Çalıştığın dizinde bu isimde bir dosya olmalı

brute_force_hash(hedef_hash, sifre_listesi)
