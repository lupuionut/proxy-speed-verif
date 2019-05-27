#!/usr/bin/env python
from urllib import request, error
import socket
import os, sys
import time
import math

socket.setdefaulttimeout(15)
mirror = 'http://speedtest.tele2.net/1MB.zip'
filename = '1.zip'
start = time.time()
try:
    proxy_ip = sys.argv[1]
    proxy = request.ProxyHandler({'http': proxy_ip})
    opener = request.build_opener(proxy)
    request.install_opener(opener)
    request.urlretrieve(mirror, filename)
    delta = time.time() - start
    filesize = os.path.getsize(filename)
    ratio = filesize/(delta*1024)
    print('Proxy {} has download speed:{} KB/s'.format(proxy_ip, math.floor(ratio)))
except error.URLError:
    print('Invalid ip or timeout for {}'.format(proxy_ip))
except ConnectionResetError:
    print('Could not connect to {}'.format(proxy_ip))
except IndexError:
    print('You must provide a testing IP:PORT proxy in the cmd line')
finally:
    if os.path.isfile(filename):
        os.remove(filename)