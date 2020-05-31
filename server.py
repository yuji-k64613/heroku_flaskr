import os
from gevent.pywsgi import WSGIServer
from flaskr import create_app

app = create_app()
ip = '0.0.0.0'
port = int(os.environ['PORT'])

http_server = WSGIServer((ip, port), app)
http_server.serve_forever()
