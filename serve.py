"""Servidor local para probar la lista sin caché: python serve.py"""
import functools
import http.server
import os

PORT = 8080


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


handler = functools.partial(NoCacheHandler, directory=os.path.dirname(os.path.abspath(__file__)))
print(f'Lista en http://127.0.0.1:{PORT}')
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), handler).serve_forever()
