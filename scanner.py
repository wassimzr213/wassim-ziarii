import socket
import sys
from datetime import datetime

# ------------------------------------------------------------
# Scanner de ports TCP simple - par Wassim Ziari
# ------------------------------------------------------------

print("=== Scanner de ports TCP - Projet GitHub ===\n")

# Demande à l'utilisateur l'adresse IP à scanner
target = input("Entrez l'adresse IP ou le nom de domaine à scanner : ")

# Plage de ports à scanner
start_port = 1
end_port = 1024

print(f"\nScan de {target} de {start_port} à {end_port}...\n")
start_time = datetime.now()

try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} ouvert")
        sock.close()
except KeyboardInterrupt:
    print("\nScan interrompu par l'utilisateur.")
    sys.exit()
except socket.gaierror:
    print("Erreur : hôte inconnu.")
    sys.exit()
except socket.error:
    print("Erreur : le serveur ne répond pas.")
    sys.exit()

end_time = datetime.now()
print(f"\nScan terminé en : {end_time - start_time}")
print("=== Fin du programme ===")
