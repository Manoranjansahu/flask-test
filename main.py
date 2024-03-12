import socket

obj = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
obj.bind(("",3456))	
obj.listen(4)
clientobj,address = obj.accept()

conn = True
while conn:
    gotmsg = clientobj.recv(1024)
    gotmsg.decode('utf-8')
    if len(gotmsg) == 0:
        conn = False
        obj.close()
