# py-chatroom
client/server chatroom written in python

## why i made this
i wanted to expand my knowledge and learn more about sockets. [this documentation](https://docs.python.org/2/library/socket.html) was very helpful to me.

## notes
you don't see the messages sent from clients come up in real time on the client simply because it uses the input method. if you start the server and look at the logs, you can see the live demo there.

## setup

open config.py and change
```py
ipv4 = "0.0.0.0"
port = 55555
```
to your ipv4 address and port (make sure its open).
