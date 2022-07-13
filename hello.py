def process_http_request(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content_type', 'text/plain')
    ]
    body = 'Hello'.encode('utf-8')
    start_response(status, response_headers)
    return [body]

