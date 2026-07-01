# --- IMPORTS ---
import socket
import time
import concurrent.futures
import argparse

# --- STEP 1: CLI Arguments Setup ---
# EN: Initialize the argument parser for terminal inputs
# TR: Terminal girdileri için argüman yakalayıcıyı başlatıyoruz
parser = argparse.ArgumentParser(description="Professional Network Port Scanner & Banner Grabber")
parser.add_argument("-t", "--target", required=True, help="Target IP or Domain (e.g., scanme.nmap.org)")
parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan (e.g., 20-80)")
args = parser.parse_args()

target_host = args.target

# EN: Split the port range string into mathematical integers
# TR: Port aralığı metnini matematiksel tam sayılara bölüyoruz
try:
    port_split = args.ports.split('-')
    start_port = int(port_split[0])
    end_port = int(port_split[1])
except Exception:
    print("❌ Error: Enter the port range in the correct format (e.g., 1-100)")
    exit()

# --- STEP 2: Main Execution & DNS Resolution ---
# EN: Outer try block catches DNS resolution failures (socket.gaierror)
# TR: Dış try bloğu DNS çözümleme hatalarını yakalar
try:
    # EN: Convert target domain to IPv4 address
    # TR: Hedef domain adresini IPv4 adresine dönüştür
    target_ip = socket.gethostbyname(target_host)

    # EN: Print scan metadata to the terminal
    # TR: Tarama meta verilerini terminale yazdır
    print("\n" + "="*60)
    print(f"📡 Target: {target_host} ({target_ip})")
    print(f"📊 Scan Range: {start_port} - {end_port}")
    print("🚀 Mode: Multi-Threading & Banner Grabbing")
    print("="*60 + "\n")

    # --- STEP 3: Core Scanning Function ---
    # EN: Define the function that will be executed by each thread
    # TR: Her bir iş parçacığı tarafından çalıştırılacak fonksiyonu tanımlıyoruz
    def scan_port(port):
        # EN: Create an IPv4/TCP socket object
        # TR: IPv4/TCP soket nesnesi oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # EN: Set a 1.0s timeout to avoid hanging on closed ports
        # TR: Kapalı portlarda asılı kalmamak için 1.0sn zaman aşımı koy
        s.settimeout(1.0)
        
        # EN: Attempt connection. Returns 0 if successful
        # TR: Bağlantıyı dene. Başarılı olursa 0 döndürür
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            try:
                # EN: Drop timeout to 0.5s for fast banner grabbing
                # TR: Hızlı banner yakalama için zaman aşımını 0.5sn'ye düşür
                s.settimeout(0.5)
                
                # EN: Receive up to 1024 bytes and decode to text
                # TR: 1024 byte'a kadar veri al ve metne dönüştür
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                
                # EN: Clean up carriage returns and newlines for clean output
                # TR: Temiz bir çıktı için satır atlamalarını temizle
                banner = banner.replace('\r', '').replace('\n', ' ')

                if banner:
                    print(f"🔓 Port {port}: OPEN | 📝 Service: {banner[:60]}")
                else:
                    print(f"🔓 Port {port}: OPEN")
            except Exception:
                # EN: If port is silent, just mark it as open
                # TR: Eğer port sessiz kalırsa, sadece açık olarak işaretle
                print(f"🔓 Port {port}: OPEN")
                
        # EN: Always close the socket to free OS resources
        # TR: İşletim sistemi kaynaklarını boşaltmak için soketi her zaman kapat
        s.close()

    # --- STEP 4: Multi-Threading Execution ---
    # EN: Start the performance timer
    # TR: Performans kronometresini başlat
    start_time = time.time()

    # EN: Inner try block catches user interrupts (Ctrl+C)
    # TR: İç try bloğu kullanıcı kesintilerini (Ctrl+C) yakalar
    try:
        # EN: Initialize a thread pool with up to 100 concurrent workers
        # TR: Maksimum 100 eşzamanlı işçi ile bir iş parçacığı havuzu başlat
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            # EN: Map the port range to the scanning function
            # TR: Port aralığını tarama fonksiyonuna dağıt
            executor.map(scan_port, range(start_port, end_port + 1))
    
    except KeyboardInterrupt:
        print("\n⚠️ Scan interrupted by user! (CTRL+C)")

    # --- STEP 5: Final Metrics ---
    # EN: Stop the timer and calculate total duration
    # TR: Kronometreyi durdur ve toplam süreyi hesapla
    end_timer = time.time()
    total_duration = end_timer - start_time

    print("\n" + "="*60)
    print("🏁 Concurrent scan completed!")
    print(f"⏱️ Total Scan Time: {total_duration:.2f} seconds")
    print("="*60)

# EN: Catch unresolvable domains gracefully
# TR: Çözümlenemeyen domainleri çökmeksizin yakala
except socket.gaierror:
    print("\n" + "="*40)
    print("❌ ERROR: Invalid IP Address or Domain Address")
    print("📡 Please check the target and try again.")
    print("="*40)