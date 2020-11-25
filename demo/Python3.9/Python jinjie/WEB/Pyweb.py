

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>my, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # return [b'<h1>my pyweb</h1>']
    return [body.encode('utf-8')]