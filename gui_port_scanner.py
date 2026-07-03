import customtkinter as ctk
import socket 
import threading
import concurrent.futures

# 1. Kütüphane ayarlerı ve tema seçimi.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# 2. Ana pencere objesini oluşturuyoruz.
app = ctk.CTk()
app.title("Advanced Port Scanner v1.0")
app.geometry("600x500")

# Başlık Metni
title_label = ctk.CTkLabel(app , text= "🚀 Advanced Port Scanner", font=("Helvetica", 24 , "bold"))
title_label.pack(pady=20)

# Hedef IP Bilgi Metni
target_Label = ctk.CTkLabel(app , text="Target IP or Domain:")
target_Label.pack(pady=5)

# Hedef IP Giriş Alanı (Entry)
target_entry = ctk.CTkEntry(app , width=300 , placeholder_text="e.g., scanme.nmap.org")
target_entry.pack(pady=10)

# Port Aralığı Bilgi Metni
port_Label = ctk.CTkLabel(app , text="Port Range (e.g., 1-1024):")
port_Label.pack(pady=5)
port_entry = ctk.CTkEntry(app , width=300 , placeholder_text="1-1024")
port_entry.pack(pady=10)

# Tetikleyici Fonksiyon
def start_scan():
    
    scan_button.configure(state="disabled")

    target = target_entry.get()
    ports = port_entry.get()

    try:
        start_port = int(ports.split('-')[0])
        end_port = int(ports.split('-')[1])
    except:
        result_box.insert("end", "[-] Error: Enter the port range in the correct format (e.g., 1-100)\n")
        return
    
    result_box.delete("0.0", "end")
    result_box.insert("end", f"[*] Target: {target}\n")
    result_box.insert("end", f"[*] Scanning ports {start_port} to {end_port}...\n\n")

    scan_thread = threading.Thread(target=background_scan, args=(target , start_port , end_port))
    scan_thread.daemon = True
    scan_thread.start()

# --- PORT KONTROL İŞÇİSİ ---
def check_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            result_box.insert("end", f"[+] Port {port} is OPEN!\n")
        s.close()
    except:
        pass

# --- ARKA PLAN YÖNETİCİSİ (HIZ MOTORU) ---
def background_scan(target, start_port, end_port):
    # 50 işçiyi aynı anda sahaya sürüyoruz (Multi-threading)
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(check_port, target, port)
            
    # Tarama bittiğinde mesajı yazdır ve BUTONUN KİLİDİNİ AÇ
    result_box.insert("end", "\n[🚀] Scan Completed!\n")
    scan_button.configure(state="normal")

# Tarama Butonu
scan_button = ctk.CTkButton(app , text="Start Scan",command=start_scan)
scan_button.pack(pady=15)

# Sonuç Ekranı
result_box = ctk.CTkTextbox(app , width=500 , height=200 , font=("Consolas",12))
result_box.pack(pady=10)

# 3. Pencerenin ekranda açık kalmasını sağlayan döngü.
app.mainloop()