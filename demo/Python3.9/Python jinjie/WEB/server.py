from wsgiref.simple_server import make_server
from WEB.Pyweb import application

httpd = make_server('', 8889, application)
print('Serving HTTP on port 8889...')
httpd.serve_forever()