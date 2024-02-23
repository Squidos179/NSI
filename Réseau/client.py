import socket, sys

HOST = '192.168.20.72'

PORT = 50000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")

msgServeur = mySocket.recv(1024).decode("Utf8")

while 1:
    if msgServeur.upper() == "FIN":
        break
    print("S>", msgServeur)
    msgClient = input("C> ")
    mySocket.send(msgClient.encode("Utf8"))
    msgServeur = mySocket.recv(1024).decode("Utf8")

print("Connexion interrompue.")
mySocket.close()