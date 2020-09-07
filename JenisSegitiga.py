#python 3.8.5
#coding: utf-8
import os
import sys
import time
import random
def viper(s):
	for c in s+'\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random()*0.1)
os.system('clear')
hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
print
time.sleep(2)
print
print
print '\x1b[1;94m'
logo = """
   _______         __            __  ______                                    
  |   |   |.-----.|  |--..-----.|  ||   __ \.---.-..-----..-----..-----..-----.
  |       ||  -__||    < |  -__||  ||    __/|  _  ||     ||__ --||  _  ||__ --|
  |___|___||_____||__|__||_____||__||___|   |___._||__|__||_____||_____||_____|"""
print(logo)
print
print
viper("\x1b[1;93m           Program Menentukan Jenis Segitiga             ")
print("\x1b[1;91m=========================================================")
viper("\x1b[1;95m[+]Author  : ./Dark<<Viper>>")
viper("[+]Support : MR.HYPER || Risky ID")
viper("[+]Github  : https://github.com/HekelPansos")
viper("[+]Team    : Dark Cyber Team ")
print("\x1b[1;91m=========================================================")
print
print
sisiA=int(input("\x1b[1;94mMasukkan Sisi A : "))
sisiB=int(input("Masukkan Sisi B : "))
sisiC=int(input("Masukkan Sisi C : "))
x=(sisiC)**2
y=(sisiA)**2+(sisiB)**2
print
print("\x1b[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print
viper("\x1b[1;95m                  Hasil Jenis Segitiga                   ")
print
print("\x1b[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
time.sleep(2)
print
print
if(x<y):
	print("\x1b[1;92mMerupakan Jenis Segitiga Lancip")
elif(x==y):
	print("\x1b[1;92mMerupakan Jenis Segitiga Siku-Siku")
else:
	print("\x1b[1;92mMerupakan Jenis Segitiga Tumpul")
print '\x1b[1;97m'