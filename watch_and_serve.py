#!/usr/bin/env python3

# INSTALL: pip install livereload

from os.path import dirname
import webbrowser
from livereload import Server

PORT = 8000
SCRIPT_DIR = dirname(__file__)

SERVER = Server()
SERVER.watch(SCRIPT_DIR + '/index.html')
webbrowser.open(f'http://localhost:{PORT}')
SERVER.serve(root=SCRIPT_DIR, port=PORT)
