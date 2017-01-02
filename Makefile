PYTHON_SERVER_SRC := ./catan_engine/native/game_engine/serve/Server.py
NODE_SERVER_SRC := ./catan/native/server_system/main_server.js
PYTHON_SERVER_SCRIPT := ./catan_engine/native/game_engine/serve/start_engine.sh

PYTHON_IP := python3

NODE_IP := node

BROWSER_f := firefox
BROWSER_s := chromium-browser
ACCESS_PATH := http://localhost:12345/

CLOSE_SIGNAL_HANDLER = ./catan/native/control/sighandle

MY_SHELL := fish
CLEANUP_SCRIPT := ./testtool/killnodes.sh

all:
	#$(PYTHON_IP) $(PYTHON_SERVER_SRC) &
	#$(PYTHON_SERVER_SCRIPT) &
	$(NODE_IP) $(NODE_SERVER_SRC) &
	sleep 2
	$(BROWSER_f) $(ACCESS_PATH) &
	sleep 2
	$(BROWSER_s) $(ACCESS_PATH) &
	sleep 300
	$(MY_SHELL) $(CLEANUP_SCRIPT)
	ps
