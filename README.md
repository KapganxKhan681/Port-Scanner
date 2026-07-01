# 📡 Advanced Network Port Scanner & Banner Grabber

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Security-Networking-red?style=for-the-badge" alt="Security Badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status Badge">
</div>

## 🌍 English
A highly optimized, multi-threaded network security tool developed in Python. Designed for rapid port discovery and service identification, this CLI-based application emulates core Nmap functionalities. It leverages concurrent execution for high-speed scanning and implements banner grabbing to identify active services behind open ports.

### 🚀 Technical Features
* **Multi-Threading Architecture:** Utilizes `concurrent.futures.ThreadPoolExecutor` to scan ports concurrently, drastically reducing execution time (e.g., scanning 1024 ports drops from ~8 minutes to ~11 seconds).
* **CLI Integration:** Fully controllable via terminal arguments using the `argparse` library, allowing dynamic target and port range assignments.
* **Banner Grabbing:** Employs socket data retrieval (`recv`) to extract and display service banners, providing crucial reconnaissance data.
* **Robust Exception Handling:** Features layered `try-except` blocks to handle DNS resolution failures (`socket.gaierror`) and graceful exits on user interrupts (`KeyboardInterrupt`).

### 💻 Installation & Usage

1. Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```

2. Run the scanner:
```bash
# Scan default standard ports (1-1024)
python port_scanner.py -t scanme.nmap.org

# Scan a specific custom port range
python port_scanner.py -t scanme.nmap.org -p 20-80
```

---

## 🇹🇷 Türkçe
Python ile geliştirilmiş, yüksek düzeyde optimize edilmiş ve çoklu iş parçacığı (multi-threading) destekli bir ağ güvenliği aracıdır. Hızlı port keşfi ve servis tespiti için tasarlanan bu CLI tabanlı uygulama, Nmap'in temel işlevlerini simüle eder. Yüksek hızlı tarama için eşzamanlı yürütme mimarisini kullanır ve açık portların arkasındaki aktif servisleri belirlemek için "banner grabbing" işlemi uygular.

### 🚀 Teknik Özellikler
* **Çoklu İş Parçacığı (Multi-Threading):** Portları eşzamanlı olarak taramak için `ThreadPoolExecutor` kullanır ve çalışma süresini büyük ölçüde azaltır (Örn: 1024 port taraması ~8 dakikadan ~11 saniyeye düşer).
* **CLI Entegrasyonu:** `argparse` kütüphanesi sayesinde tamamen terminal argümanları üzerinden kontrol edilebilir; dinamik hedef ve aralık atamasına olanak tanır.
* **Banner Grabbing:** Kritik keşif verilerini sağlamak amacıyla servis karşılama metinlerini yakalamak ve görüntülemek için soket veri alımını (`recv`) kullanır.
* **Kapsamlı Hata Yönetimi:** DNS çözümleme hatalarını yönetmek ve kullanıcı kesintilerinde programı güvenle sonlandırmak için katmanlı `try-except` blokları içerir.

### 💻 Kurulum ve Kullanım

1. Depoyu bilgisayarınıza indirin:
```bash
git clone [https://github.com/KULLANICI_ADINIZ/DEPO_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/DEPO_ADINIZ.git)
cd DEPO_ADINIZ
```

2. Tarayıcıyı çalıştırın:
```bash
# Varsayılan standart portları (1-1024) taramak için
python port_scanner.py -t scanme.nmap.org

# Özel bir port aralığı taramak için
python port_scanner.py -t scanme.nmap.org -p 20-80
```

---

### ⚠️ Disclaimer / Yasal Uyarı
**EN:** This tool is developed for educational purposes and authorized penetration testing only. Scanning networks or hosts without explicit written permission is strictly prohibited and illegal. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

**TR:** Bu araç yalnızca eğitim amaçlı ve yetkili sızma testleri için geliştirilmiştir. Açık ve yazılı izin olmadan ağları veya sistemleri taramak kesinlikle yasaktır ve yasa dışıdır. Geliştirici, bu programın kötüye kullanılması veya neden olduğu herhangi bir zarardan sorumlu tutulamaz.