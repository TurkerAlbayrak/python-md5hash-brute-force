# Python MD5 Hash Brute Force

> **Uyari:** Bu proje yalnizca **egitim amaclidir**. Kisisel veya kurumsal sistemlerde izinsiz kullanim yasaktir ve yasal sorumluluk dogurur. Siber guvenlik kavramlarini ogrenmeye yonelik kontrollü bir ortamda kullanin.

---

## Icindekiler

- [Proje Hakkinda](#proje-hakkinda)
- [MD5 Nedir](#md5-nedir)
- [Brute Force Nedir](#brute-force-nedir)
- [Nasil Calisir](#nasil-calisir)
- [Kurulum](#kurulum)
- [Kullanim](#kullanim)
- [Dosya Yapisi](#dosya-yapisi)
- [Sinirlamalar ve Guvenlik Notu](#sinirlamalar-ve-guvenlik-notu)
- [Lisans](#lisans)

---

## Proje Hakkinda

Bu proje, Python programlama dilinin standart kutuphanesi olan `hashlib` modulu kullanilarak MD5 hash degerleri uzerinde **sozluk tabanli kaba kuvvet (dictionary-based brute force)** saldirilarinin nasil calistigini gostermek amaciyla gelistirilmistir.

Proje; hash algoritmalarinin temel mantigi, sifre guvenligi ve kaba kuvvet saldirilarina karsi alinabilecek onlemler hakkinda pratik bir anlayis kazandirmak isteyen ogrenciler ve gelistiriciler icin tasarlanmistir.

---

## MD5 Nedir

MD5 (Message Digest Algorithm 5), bir girdi metnini sabit uzunlukta (128-bit / 32 karakter hexadecimal) bir cikti degerine donusturan tek yonlu bir hash algoritmasidir. Orijinal olarak veri butunlugu dogrulamak icin tasarlanmis olsa da gunumuzde sifre saklama amaciyla **guvenli kabul edilmemektedir**.

Ornek:

```
"admin123"  -->  MD5  -->  0192023a7bbd73250516f069df18b500
```

Teorik olarak MD5 geri dondurulemez. Ancak sozluk saldirilari ve rainbow table yontemleriyle zayif sifrelerin karsiligi bulunabilir.

---

## Brute Force Nedir

Kaba kuvvet (brute force) saldirisi, bir sifreyi veya anahtari bulmak icin tum olasiliklarin sistematik olarak denendigi bir yontemdir. Bu projede uygulanan yontem daha ozelde **sozluk saldirisi (dictionary attack)** olarak siniflandirilir: onceden hazirlanmis bir kelime listesindeki her bir girdi MD5 ile hashlenerek hedef hash ile karsilastirilir.

---

## Nasil Calisir

`hash.py` dosyasindaki temel akis asagidaki gibidir:

1. Hedef MD5 hash degeri tanimlanir.
2. Bir wordlist (kelime/sifre listesi) dosyasi satirlari tek tek okunur.
3. Her satirdaki deger `hashlib.md5()` ile hashlenir.
4. Elde edilen hash, hedef hash ile karsilastirilir.
5. Eslesme bulunursa sifre ekrana yazdirilir; bulunamazsa bilgi mesaji gosterilir.

```python
import hashlib

def brute_force_hash(target_hash, wordlist_file):
    print("[*] Brute Force islemi baslatiliyor...")
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                password = line.strip()
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    print(f"\n[+] Sifre Bulundu!: {password}")
                    return password
        print("\n[-] Maalesef sifre listede bulunamadi.")
        return None
    except FileNotFoundError:
        print(f"[-] Hata: '{wordlist_file}' dosyasi bulunamadi!")
```

---

## Kurulum

Projenin calisabilmesi icin herhangi bir dis kutuphane kurulumuna gerek yoktur. Python 3.x standart kutuphanesi yeterlidir.

**Gereksinimler:**

- Python 3.6 veya uzeri

**Depoyu klonlayin:**

```bash
git clone https://github.com/TurkerAlbayrak/python-md5hash-brute-force.git
cd python-md5hash-brute-force
```

---

## Kullanim

### 1. Wordlist hazirlayin

Calisma dizininde `passwords.txt` adinda bir dosya olusturun ve satirlara sifre adaylarini yazin:

```
123456
password
admin
admin123
qwerty
letmein
```

> Gercek dunya testlerinde `rockyou.txt` gibi kapsamli wordlist'ler kullanilabilir. Bu dosyalari [SecLists](https://github.com/danielmiessler/SecLists) deposundan edinebilirsiniz.

### 2. Hedef hash'i ayarlayin

`hash.py` dosyasini acin ve `hedef_hash` degiskenini kirmayi denemek istediginiz MD5 hash degeriyle guncelleyin:

```python
hedef_hash = "0192023a7bbd73250516f069df18b500"  # "admin123" sifresinin MD5 hashi
sifre_listesi = "passwords.txt"
```

### 3. Scripti calistirin

```bash
python hash.py
```

### Ornek cikti

Sifre bulunursa:
```
[*] Brute Force islemi baslatiliyor...

[+] Sifre Bulundu!: admin123
```

Sifre bulunamazsa:
```
[*] Brute Force islemi baslatiliyor...

[-] Maalesef sifre listede bulunamadi.
```

---

## Dosya Yapisi

```
python-md5hash-brute-force/
|
|-- hash.py          # Ana brute force scripti
|-- passwords.txt    # Kullanici tarafindan saglanmasi gereken wordlist (repoya dahil degil)
|-- README.md        # Proje dokumantasyonu
|-- LICENSE          # MIT Lisans
```

---

## Sinirlamalar ve Guvenlik Notu

Bu proje bilerek **basit ve anlasilir** tutulmustur; uretim ortaminda kullanima uygun degildir.

**Teknik sinirlamalar:**

- Yalnizca MD5 algoritmasi desteklenmektedir. SHA-1, SHA-256 gibi diger algoritmalar icin `hashlib` modulu genisletilebilir.
- Salt (tuz) eklenmis hashleri kirmayi desteklememektedir. Modern sifre saklama sistemleri (bcrypt, argon2) bu nedenle bu tur saldirilardan onemli olcude korunmaktadir.
- Performans optimize edilmemistir; buyuk wordlist dosyalarinda isleme suresi uzayabilir.

**Etik ve yasal uyari:**

Bu arac yalnizca **kendi sistemlerinizde veya izin verilmis ortamlarda** egitim amacli kullanilmalidir. Izinsiz sistemlere karsi kullanmak bircok ulkede yasalara aykiridir. Gelistirici bu arakin kotu amacli kullanimlarindan sorumluluk kabul etmez.

---

## Lisans

Bu proje [MIT Lisansi](./LICENSE) ile lisanslanmistir. Dilediginiz gibi kullanabilir, degistirebilir ve dagitabilirsiniz; ancak lisans metnini koruyunuz.
