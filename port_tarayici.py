import socket
import threading
hedef = input("Hedef IP: ")
print(f"{hedef} taranıyor...\n")
def tara(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        sonuc = s.connect_ex((hedef,port))
        if sonuc == 0:
            print(f'Port {port} açık')
        s.close()
    except:
        pass
for port in range(1,1015):
    t = threading.Thread(target = tara, args=(port,))
    t.start()

