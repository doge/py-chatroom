'''

    py-chatroom
    client.py

'''

import socket, time, config


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def initialize_connection():
    while True:
        try:
            s.connect((config.ipv4, config.port))
            break
        except:
            print("attempting to connect to %s:%s" % (config.ipv4, config.port))
            time.sleep(1)


initialize_connection()

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
