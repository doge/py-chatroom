'''

    py-chatroom
    client.py

'''

import socket, time

ipv4 = "0.0.0.0"
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def init_connection():
    while True:
        try:
            s.connect((ipv4, port))
            break
        except:
            print("attempting to connect to %s:%s" % (ipv4, port))
            time.sleep(1)


init_connection()

print("connected to the server as %s:%s" % (s.getsockname()[0], s.getsockname()[1]))
print("to quit please type \"quit\" or \"exit\"")

alias = input("what is your name?: ")

while True:
    user_input = input("message: ")
    if user_input == "quit" or user_input == "exit":
        s.close()
        break
    else:
        s.send(str.encode("%s: %s" % (alias, user_input)))
        from_server = s.recv(4096)
        print(from_server.decode("utf-8"))
