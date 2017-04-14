import socket,cv2,base64,time

class Client():
	def __init__(self,Adress=("192.168.43.217",5001)):   # ip of server computer  172.16.214.112
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(Adress)
		print('connected')
	def receive(self):
		tm = self.s.recv(2049)
		strn=tm.decode('ascii') 
		return strn


# attempt cnnection to server
res=''
c= Client()
length1=c.receive()
time.sleep(2)
length1=int(length1)
#print length1
#a=0
#time.sleep(2)
for len in range (0,length1,2048):
	#a+=1
	string1=c.receive()
	res+=string1
	#print string1
	#print a
res=res[:length1]
#print string1

fh = open("imageToSave.png", "wb")
fh.write(res.decode('base64'))
fh.close()
img = cv2.imread('imageToSave.png',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

socket.close()

#Server will send a Photo


#Enable user to make changes on photo Opencv


# Every instance of time get the Changed info in photo and send it to server

#fh = open()