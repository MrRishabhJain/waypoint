import socket, time,os, random, cv2, base64

class Server():
	def __init__(self,Adress=('',5001),MaxClient=1):
		self.s = socket.socket()
		self.s.bind(Adress)
		self.s.listen(MaxClient)
	def WaitForConnection(self):
		self.Client, self.Adr=(self.s.accept())
		print('Got a connection from: '+str(self.Client)+'.')
		return self.Client
	def Receive(self):
		tm=self.s.recv(2048)
		return tm.decode('ascii')

def TakePhoto():
	cap = cv2.VideoCapture(0)
	print 'Press Space bar to click a Photograph'
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret==True:	
			cv2.imshow('Faces', frame)	
			if cv2.waitKey(1) & 0xFF == ord(' '):
				cap.release()
				return frame

s = Server()
cli=s.WaitForConnection()	
img=TakePhoto()
cv2.imwrite('mypic.jpeg',img)
with open("mypic.jpeg", "rb") as imageFile:
	strt = base64.b64encode(imageFile.read())
den=len(strt)
poll=den%2048
poll=(2048-poll)+den

strt=strt.ljust(poll,'0')
#print strt
#print len(strt)%2048	
input = str(den)
#print input
cli.send((input).encode('ascii'))

time.sleep(2)
#a=0
chunks, chunk_size = len(strt), 2048
for i in range(0, chunks, chunk_size):
	#a+=1
	cli.send((strt[i:i+chunk_size]).encode('ascii'))
	#print a
	time.sleep(.01)

print 'Press "q" to Exit'
while(1):
	cv2.imshow('Faces', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):		
		break

cv2.destroyAllWindows()	





