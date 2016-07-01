# **************************************************************************************************************************
# Version:     2016.06.30 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + Websocket Python + WoT
# **************************************************************************************************************************
# 
# 1. update opkg & install wget & disable bridge
# 	 opkg update
# 	 opkg install wget
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#
# 2. install setuptools
#	 curl https://bootstrap.pypa.io/ez_setup.py -k -o - | python
#
# 3. install six
# 	 wget --no-check-certificate https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz
# 	 tar zxvf six-1.10.0.tar.gz
#	 cd six-1.10.0
#	 python setup.py install
#
# 4. install Websocket
#	 wget --no-check-certificate https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz
#	 tar zxvf websocket_client-0.32.0.tar.gz
#	 cd websocket_client-0.32.0
#	 python setup.py install
#
# **************************************************************************************************************************

import time
import sys  
import websocket
import datetime

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/56fa911c36b24acd62000058/send")

while True:
	print value.get('dirtyVal') 
	h0 = value.get('EARTH') 
	t0 = value.get("h")
	l0 = value.get("t")
	
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	
	vals = "{\"date\":\""+date+"\",\"temperature\":"+t0+",\"h\":"+l0+",\"soil\":"+h0+"}"
	
	time.sleep(1);
	ws.send(vals);
	print vals;