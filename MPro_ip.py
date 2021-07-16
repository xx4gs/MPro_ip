from geoip import geolite2
import sys as p
import time as mp
def slow(m2):
	for m1 in m2 + '\n':
		p.stdout.write(m1)
		p.stdout.flush()
		mp.sleep(1. / 120)
slow("""
__________________________________
|                                |
|    __________________          |
|   |  Telegram:xx4gs  |         |
|   |  Instagram:xx4gs |         |
|   |__________________|         |
|     _________________          |
|    |  MohammedPro💉  |         |
|    |  MPro_ip.py💉   |         |
|    | _______________ |         |
|________________________________|
""")

ip = input("[MPro ip Enter] >> ")
mpro= geolite2.lookup(ip)
if mpro is None:
	print('ip Unknown')
else:
	print('\n','[IP information]')
	slow('\n _________________________')
	print('\n',[mpro.country])
	slow('\n _________________________')
	print('\n',[mpro.timezone])
	slow('\n _________________________')
	print('\n',[mpro.location])
	slow('\n _________________________')
	print('\n',[mpro.ip])
	slow('\n _________________________')
	input('exit Enter: ')
	slow('\n _________________________')
	exit()
