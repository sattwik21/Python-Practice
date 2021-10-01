#client
import socket, pickle
def read_string():
 string = input("Enter String: ")
 return string
HOST = 'localhost'
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
mystring = read_string()
data_string = pickle.dumps(mystring)
s.send(data_string)
data = s.recv(4096)
data_mystring = pickle.loads(data)
s.close()
print('Letter count: ', repr(data_mystring)) 

#server
import socket, pickle
HOST = 'localhost'
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print("Connected: ", addr)
while True:
 data = conn.recv(4096)
 data = pickle.loads(data)
 if not data:
 break
 print(data)
 d = {}
 for i in data:
 if i in d:
 d[i]+=1
 else:
 d[i] = 1
 conn.send(pickle.dumps(d))
conn.close()