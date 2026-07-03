import customtkinter as ctk
import socket
import threading
import concurrent.futures

# --- THEME AND APPEARANCE SETTINGS / TEMA VE GÖRÜNÜM AYARLARI ---
ctk.set_appearance_mode("dark")      # Set dark mode / Koyu temayı ayarla
ctk.set_default_color_theme("blue")  # Set blue accent color / Mavi vurgu rengini ayarla

# --- MAIN WINDOW SETUP / ANA PENCERE KURULUMU ---
app = ctk.CTk()
app.title("Advanced Port Scanner v1.0")
app.geometry("600x500")

# --- WIDGETS / ARAYÜZ ARAÇLARI ---

# Main Title / Ana Başlık
title_label = ctk.CTkLabel(app, text="🚀 Advanced Port Scanner", font=("Helvetica", 24, "bold"))
title_label.pack(pady=20)

# Target IP Input Section / Hedef IP Giriş Kısmı
target_label = ctk.CTkLabel(app, text="Target IP or Domain:")
target_label.pack(pady=5)
target_entry = ctk.CTkEntry(app, width=300, placeholder_text="e.g., scanme.nmap.org")
target_entry.pack(pady=10)

# Port Range Input Section / Port Aralığı Giriş Kısmı
port_label = ctk.CTkLabel(app, text="Port Range (e.g., 1-1024):")
port_label.pack(pady=5)
port_entry = ctk.CTkEntry(app, width=300, placeholder_text="1-1024")
port_entry.pack(pady=10)

# --- SCANNING FUNCTIONS / TARAMA FONKSİYONLARI ---

# Port checking worker / Port kontrol işçisi
def check_port(target, port):
    try:
        # Create socket motor / Soket motorunu oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Wait 0.5s for response / Yanıt için 0.5sn bekle
        
        # Try to connect / Bağlanmayı dene
        result = s.connect_ex((target, port))
        if result == 0:
            result_box.insert("end", f"[+] Port {port} is OPEN!\n")
            result_box.see("end") # Auto-scroll / Otomatik kaydırma
        s.close()
    except:
        pass

# Background manager (Speed Motor) / Arka plan yöneticisi (Hız Motoru)
def background_scan(target, start_port, end_port):
    # Use 50 concurrent workers / Aynı anda 50 işçi kullan (Multi-threading)
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(check_port, target, port)
            
    # Print completion message and UNLOCK button / Bitiş mesajı yazdır ve BUTON KİLİDİNİ AÇ
    result_box.insert("end", "\n[🚀] Scan Completed!\n")
    result_box.see("end")
    scan_button.configure(state="normal")

# Button trigger function / Buton tetikleyici fonksiyonu
def start_scan():
    # 1. LOCK THE BUTTON to prevent spam clicks / Spam tıklamayı önlemek için BUTONU KİLİTLE
    scan_button.configure(state="disabled")
    
    # 2. Get data from user inputs / Kullanıcıdan gelen verileri al
    target = target_entry.get()
    ports = port_entry.get()
    
    # 3. Parse port range / Port aralığını parçala
    try:
        start_port = int(ports.split('-')[0])
        end_port = int(ports.split('-')[1])
    except:
        result_box.insert("end", "[-] Error: Invalid port format (e.g., 80-443)\n")
        scan_button.configure(state="normal") # Unlock if error occurs / Hata varsa kilidi aç
        return

    # 4. Clear screen and show start message / Ekranı temizle ve başlama mesajı ver
    result_box.delete("0.0", "end")
    result_box.insert("end", f"[*] Target: {target}\n")
    result_box.insert("end", f"[*] Scanning ports {start_port} to {end_port}...\n\n")

    # 5. START SCAN IN BACKGROUND THREAD / TARAMAYI ARKA PLAN THREAD'İNDE BAŞLAT
    scan_thread = threading.Thread(target=background_scan, args=(target, start_port, end_port))
    scan_thread.daemon = True # Close thread when app closes / Uygulama kapanırsa thread'i de kapat
    scan_thread.start()

# --- SCAN BUTTON / TARAMA BUTONU ---
scan_button = ctk.CTkButton(app, text="🚀 Start Scan", command=start_scan)
scan_button.pack(pady=15)

# --- TERMINAL OUTPUT BOX / TERMİNAL ÇIKTI KUTUSU ---
result_box = ctk.CTkTextbox(app, width=500, height=200, font=("Consolas", 12))
result_box.pack(pady=10)

# --- START EVENT LOOP / ANA DÖNGÜYÜ BAŞLAT ---
app.mainloop()
