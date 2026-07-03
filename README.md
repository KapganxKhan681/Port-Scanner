# 📡 Advanced Port Scanner & Banner Grabber (CLI & GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Red_Team-red?style=for-the-badge&logo=hackthebox)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 🌍 English

A highly optimized, multi-threaded network security tool developed in Python. Designed for rapid port discovery and reconnaissance, this repository features both a lightweight **Command Line Interface (CLI)** and a modern **Graphical User Interface (GUI)** version. 

### 🚀 Technical Features
* **Multi-Threading Architecture:** Utilizes `concurrent.futures.ThreadPoolExecutor` to scan ports concurrently, drastically reducing execution time.
* **Modern GUI Engine:** Includes a sleek, dark-mode user interface powered by `customtkinter`, preventing GUI-freezes using background `threading`.
* **Banner Grabbing (CLI):** Employs socket data retrieval (`recv`) to extract service banners in the terminal version.
* **Robust Exception Handling:** Features layered `try-except` blocks to handle timeouts, DNS resolution failures, and prevents spam-clicking in the GUI.

### 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KapganxKhan681/Port-Scanner.git
   cd Port-Scanner
   ```

2. **Install GUI requirements (Only needed for the GUI version):**
   ```bash
   pip install customtkinter
   ```

3. **Run the tools:**
   * **For Terminal (CLI) Version:**
     ```bash
     python port_scanner.py -t scanme.nmap.org -p 20-80
     ```
   * **For Interface (GUI) Version:**
     ```bash
     python gui_port_scanner.py
     ```

---

## TR Türkçe

Python ile geliştirilmiş, yüksek düzeyde optimize edilmiş ve çoklu iş parçacığı (multi-threading) destekli bir ağ güvenliği aracıdır. Hızlı port keşfi için tasarlanan bu depo, hem hafif bir **Terminal (CLI)** hem de modern bir **Arayüz (GUI)** versiyonu içerir.

### 🚀 Teknik Özellikler
* **Çoklu İş Parçacığı (Multi-Threading):** Portları eşzamanlı olarak taramak için `ThreadPoolExecutor` kullanır ve çalışma süresini büyük ölçüde azaltır.
* **Modern Arayüz Motoru:** `customtkinter` ile güçlendirilmiş koyu temalı bir arayüz sunar. Arka plan `threading` yapısı sayesinde arayüz donmalarını (GUI-freeze) engeller.
* **Banner Grabbing (CLI):** Terminal versiyonunda kritik keşif verilerini sağlamak amacıyla servis karşılama metinlerini yakalamak için `recv` kullanır.
* **Kapsamlı Hata Yönetimi:** Zaman aşımlarını ve DNS çözüme hatalarını güvenle atlatır; arayüzde spam tıklamaları önleyici güvenlik mekanizmasına sahiptir.

### 💻 Kurulum ve Kullanım

1. **Depoyu bilgisayarınıza indirin:**
   ```bash
   git clone https://github.com/KapganxKhan681/Port-Scanner.git
   cd Port-Scanner
   ```

2. **Arayüz gereksinimlerini kurun (Sadece GUI versiyonu için):**
   ```bash
   pip install customtkinter
   ```

3. **Araçları çalıştırın:**
   * **Terminal (CLI) Versiyonu İçin:**
     ```bash
     python port_scanner.py -t scanme.nmap.org -p 20-80
     ```
   * **Arayüz (GUI) Versiyonu İçin:**
     ```bash
     python gui_port_scanner.py
     ```

---

### ⚠️ Disclaimer / Yasal Uyarı
**EN:** This tool is developed for educational purposes and authorized penetration testing only. Scanning networks or hosts without explicit written permission is strictly prohibited.
**TR:** Bu araç yalnızca eğitim amaçlı ve yetkili sızma testleri için geliştirilmiştir. Açık izin olmadan ağları veya sistemleri taramak yasa dışıdır.
