import socket
import signal, sys, time
import argparse

parser = argparse.ArgumentParser(description='calculation descrription')
parser.add_argument('--host', action="store", dest="host", required=True, help="joblist as dict")
args = parser.parse_args()

server = socket.socket()


def signal_handler(signal, frame):
    print ('Ctrl+C ')
    server.close()
    time.sleep(1)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

try:
    server.connect((args.host, 4444))
    while True:
        string = input("Problem Girin:")
        server.send(string.encode())
        result = server.recv(1024).decode()
        print("Cevap:", result)
except(Exception):
    server.send("Hata".encode())



